import unittest
import sys
import os

sys.path.append('/DS5010_course_project-main/handy_datatable')
from handy_sqlite import sqlite_data_table

class TestSqliteDataTable(unittest.TestCase):

    def test_create_table(self):
        manager = setup()[0]#manager table
        manager.create_table()
        self.assertTrue(os.path.exists(manager.table_name + '.sql'),'Create Table Failed')

    def test_check_value_column(self):
        manager = setup()[0]#manager table
        data_file = setup()[2]#manager csv file
        self.assertTrue(manager.check_value_column(data_file), 'Check_Value_Column Failed')

    def test_insert_table(self):
        employee = setup()[1]#employee table
        data_file = setup()[3]#employee csv file
        export_path = setup()[4]#employee export path
        employee.create_table()
        employee.insert_table(data_file, export_path)
        with open(export_path, 'r') as f:
            sql_statement = f.read()
            self.assertIn('INSERT INTO EMP_1 VALUES(\'1\',\'Bob\',\'123\',\'25\n\');\n', sql_statement, 'Insert Table Failed')
            f.close()

    def tearDown(self):
        os.remove(setup()[2])
        if os.path.isfile(setup()[1].table_name):#remove EMP_1.sql
            os.remove(setup()[1].table_name + '.sql')
        if os.path.isfile(setup()[0].table_name):#remove Manager.sql
            os.remove(setup()[0].table_name + '.sql')
        if os.path.isfile(setup()[4]):#remove test_export.sql
            os.remove(setup()[4])
        os.remove(setup()[3])      
       
def setup():
    """
    Initialize the test case
    """

    manager_entity = [('Manager_name','TEXT'),('Manager_ID','INTEGER')]

    employee1_entity = [('Manager_ID','INTEGER'),('Employee_name','TEXT'),('Employee_ID','TEXT'),('Employee_age','INTEGER')]



    #create objects/tables
    manager = sqlite_data_table(table_name = 'Manager', table_entity = manager_entity, primary_key='Manager_ID')
    
    employee1 = sqlite_data_table(table_name = 'EMP_1', table_entity = employee1_entity, primary_key='Employee_ID', foreign_key='Manager_ID')

    emp_data_file = 'emp_data_file.csv'
    mger_data_file = 'mger_data_file.csv'
    emp_export_path = 'test_export.sql'

    with open(emp_data_file, 'w') as f:
        f.write('1,Bob,123,25\n')
        f.close()
    with open(mger_data_file, 'w') as f:
        f.write('1,Alice\n')
        f.close()
    
    return [manager, employee1,mger_data_file, emp_data_file, emp_export_path]



if __name__ == '__main__':
    unittest.main()
    
