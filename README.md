# DS5010_course_project
DS5010 course project repository

The main purpose of this package is to visualize the tables from relational databases and create SQL statements with Python. By importing these modules, the user can create relational mapping graphs between tables and create SQL statements without a deep understanding about SQL and relational databases.

All of the methods from 'Handy_data_table' offer a data table structure object, ‘Handy_graphviz’ and ‘Handy_sqlite are the derived class of the ‘Handy_data_table’. The objects initiated under ‘Handy_sqlite’ and ‘Handy_graphviz’ inherit the attributes and methods from ‘Handy_data_table’.

Example 
Create viz_data_table object

```Python 
#Define table entities
department_entity = [('Depart_name','TEXT'),('Depart_ID','TEXT')]

doctor_entity = [('Name','TEXT'),('Depart_ID','TEXT'),('Doc_ID','TEXT')]

patient1_entity  = [('Name','TEXT'),('PAT_ID','INTEGER'),('Doc_ID','TEXT')]
```
