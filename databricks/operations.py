"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

import json
import arrow
from datetime import datetime
from databricks.sdk.core import Config, oauth_service_principal
from databricks import sql
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('databricks')


class DatabricksSQLClient(object):
    def __init__(self, config):
        self.hostname = config.get('databricks_server_hostname')
        self.http_path = config.get('databricks_http_path')
        self.client_id = config.get('databricks_client_id')
        self.client_secret = config.get('databricks_client_secret')
        self.connection = None
        self.cursor = None

    def _credential_provider(self):
        config = Config(
            host = f"https://{self.hostname}" if not self.hostname.startswith("https://") else self.hostname,
            client_id = self.client_id,
            client_secret = self.client_secret
        )
        return oauth_service_principal(config)

    def connect(self):
        self.connection = sql.connect(
            server_hostname = self.hostname,
            http_path = self.http_path,
            credentials_provider = self._credential_provider
        )
        self.cursor = self.connection.cursor()

    def execute(self, query):
        if not self.cursor:
            raise Exception("Connection not established. Call connect() first.")
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


def handler(obj):
    if isinstance(obj, bytearray) or isinstance(obj, bytes):
        return obj.decode(encoding='utf-8')
    elif isinstance(obj, datetime):
        return str(arrow.get(obj))
    return str(obj)


def run_query(config, params):
    query = params.get('query_string')
    try:
        with DatabricksSQLClient(config) as client:
            cursor = client.cursor
            cursor.execute(query)
            columns = [col[0] for col in cursor.description or []]
            rows = cursor.fetchall()
            result = [json.loads(json.dumps(dict(zip(columns, row)), default = handler)) for row in rows]
            return result

    except Exception as e:
        logger.exception('Databricks query failed: {e}'.format(e))
        raise ConnectorError('Databricks query failed: {e}'.format(e))


def _check_health(config):
    try:
        with DatabricksSQLClient(config) as client:
            client.execute("SHOW TABLES")
        return True
    except Exception as e:
        logger.exception('Databricks query failed: {e}'.format(e))
        raise ConnectorError('Databricks query failed: {e}'.format(e))


operations = {
    'run_query': run_query
}
