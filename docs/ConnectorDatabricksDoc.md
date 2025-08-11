## About the connector
Query an Azure Databricks Cluster table in a catalog's schema (database). Uses Databricks SQL Connector for Python.
<p>This document provides information about the Databricks Connector, which facilitates automated interactions, with a Databricks server using FortiSOAR&trade; playbooks. Add the Databricks Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Databricks.</p>

### Version information

Connector Version: 1.0.1


Authored By: Fortinet ETAC

Certified: No

## Release Notes for version 1.0.1
The following enhancements have been made to the Databricks Connector in version 1.0.1:
<ul>
<li><p>Fixed an issue in the connector code where the server URL was not being validated correctly.</p></li>

## Installing the connector
<p>From FortiSOAR&trade; 5.0.0 onwards, use the <strong>Connector Store</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.<br>You can also use the following <code>yum</code> command as a root user to install connectors from an SSH session:</p>
`yum install cyops-connector-databricks`

## Prerequisites to configuring the connector
- You must have the URL of Databricks server to which you will connect and perform automated operations and credentials to access that server.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Databricks server.

## Minimum Permissions Required
- N/A

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Databricks</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations&nbsp;</strong> tab enter the required configuration details:&nbsp;</p>
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Databricks Server Hostname<br></td><td>The server hostname of the all-purpose compute or SQL warehouse. You can get this from the Server Hostname value in the Advanced Options > JDBC/ODBC tab for your all-purpose compute or Connection Details tab for your SQL warehouse.<br>
<tr><td>Databricks HTTP Path<br></td><td>The HTTP path of the all-purpose compute or the SQL warehouse. You can get this from the HTTP Path value in the Advanced Options > JDBC/ODBC tab for your all-purpose compute or the Connection Details tab for your SQL warehouse.<br>
<tr><td>Databricks Client ID<br></td><td>Create a Databricks service principal in your Databricks workspace, and create an OAuth secret for that service principal. This will be the service principal's UUID or Application ID value.<br>
<tr><td>Databricks Client Secret<br></td><td>Create a Databricks service principal in your Databricks workspace, and create an OAuth secret for that service principal. This will be the Secret value for the service principal's OAuth secret.<br>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function<br></th><th>Description<br></th><th>Annotation and Category<br></th></tr></thead><tbody><tr><td>Run Query<br></td><td>Executes a query on the database. You can execute any valid SQL query such as Create, Update, Delete, Insert or Select.<br></td><td>run_query <br/>Investigation<br></td></tr>
</tbody></table>

### operation: Run Query
#### Input parameters
<table border=1><thead><tr><th>Parameter<br></th><th>Description<br></th></tr></thead><tbody><tr><td>Query String<br></td><td>Query that you want to trigger on the database. You can perform all sorts of operations such as Create, Update, Delete, Insert, or Select, on the database using this query.<br>
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.
## Included playbooks
The `Sample - Databricks - 1.0.0` playbook collection comes bundled with the Databricks connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR<sup>TM</sup> after importing the Databricks connector.

- Run Query

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection, since the sample playbook collection gets deleted during connector upgrade and delete.
