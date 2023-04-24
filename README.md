# DS5010_course_project
DS5010 course project - Handy_data_table

The main purpose of this package is to visualize the tables from relational databases and create SQL statements with Python. By importing these modules, the user can create relational mapping graphs between tables and create SQL statements without a deep understanding about SQL and relational databases.

All of the methods from 'Handy_data_table' offer a data table structure object, ‘Handy_graphviz’ and ‘Handy_sqlite are the derived class of the ‘Handy_data_table’. The objects initiated under ‘Handy_sqlite’ and ‘Handy_graphviz’ inherit the attributes and methods from ‘Handy_data_table’.

# Example Handy_graphviz

Create 'viz_data_table' object

```Python 
import handy_graphviz as hg

#Define table entities
department_entity = [('Depart_name','TEXT'),('Depart_ID','TEXT')]

doctor_entity = [('Name','TEXT'),('Depart_ID','TEXT'),('Doc_ID','TEXT')]

patient1_entity  = [('Name','TEXT'),('PAT_ID','INTEGER'),('Doc_ID','TEXT')]


#create objects/tables
department = hg.viz_data_table(table_name = 'Department', table_entity = department_entity)
doctor = hg.viz_data_table(table_name = 'Doctor', table_entity = doctor_entity)
patient1 = hg.viz_data_table(table_name = 'PAT1', table_entity = patient1_entity)
```

The user can create table without SQL but only need to initiate objects with straight forward string.

```python
#Convert and output the table structure into dot scripts
department.graphviz_convert_export('department.txt')
doctor.graphviz_convert_export('doctor.txt')
patient1.graphviz_convert_export('patient1.txt')
```
With the graphviz_convert_export method, the content of the object will be converted to the dot script into a text file.
Then the user can read the text file and apply it to graphviz for generating visualization.

```html
<<TABLE BORDARD="0" CELLBORDER="1" CELLSPACING ="0">
<TR>
<TD PORT='Name'>Name</TD>
</TR>
<TR>
<TD PORT='Depart_ID'>Depart_ID</TD>
</TR>
<TR>
<TD PORT='Doc_ID'>Doc_ID</TD>
</TR>
</TABLE>>
```
Output example of the 'Doctor' object data table dot script 


# Example Handy_sqlite

Handy_sqlite and Handy_graphviz both are the derived class of Handy_data_table.
Therefore, they have the same way to initiate the object.

```python
#Define table entities
doctor_entity = [('Name','TEXT'),('Depart_ID','TEXT'),('Doc_ID','TEXT')]

#create objects/tables
doctor = hg.sqlite_data_table(table_name = 'Doctor', table_entity = doctor_entity)

#convert to sql create table statement
doctor.create_table()
```

With the 'create_table' method, the SQL script of creating the 'Doctor'table will be generated.

```SQL
CREATE TABLE Doctor(
Name TEXT,
Depart_ID TEXT,
Doc_ID TEXT);
```

Then connect to the SQLite db file and execute this create table statement.
The table 'Doctor' will be created in the SQLite db file.
