# User Permissions

The utility management system follows the standard iviva role-based access control system.

The application defines several application roles.

Using iviva's standard authorization framework, those roles can be collected into user roles and user groups.



The following application roles are available:

| App Role                            | Description                                                                                                                                                                                                                                                                |
| ----------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Allowed to access app               | This role is required for anyone to access the application. Users with this role can view all analytics data in the application.                                                                                                                                           |
| Allowed to configure data           | This role is required to enable users to configure data - this includes configuration of meters, virtual meters, meter groups, tags, baselines and locations.                                                                                                              |
| Allowed to save filters and reports | This role gives the user the permission to create reports in the system and create new dashboard widgets using the [consumption-analysis-tool.md](operational-guide/consumption-analysis-tool.md "mention") that are permanently set in the dashboard for everyone to view |

