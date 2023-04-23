import unittest
import os
import sys

sys.path.append('C:/Users/anish/Downloads/DS5010_course_project-main/handy_datatable')

import handy_graphviz as hg


class TestVizDataTable(unittest.TestCase):

    def test_add_entity(self):
        manager = setup()[0]#manager table
        manager.add("AGE", "INTEGER")
        self.assertEqual(len(manager), 3,"test_add failed")
        check = ('AGE','INTEGER')
        self.assertIn(check, manager.entity_list,"test_add failed")

    def test_drop_entity(self):
        employee1 = setup()[1]#employee_1 table
        employee1.drop('Employee_age')
        self.assertEqual(len(employee1), 3,"test_drop failed")
        self.assertNotIn('Employee_age', employee1.entity_list,"test_drop failed")

    def test_get_entity(self):
        employee1 = setup()[1]#employee_1 table
        self.assertEqual(employee1.get_entity(), ["Manager_ID", "Employee_name","Employee_ID","Employee_age"],"test_get_entity failed")

    def test_get_table_name(self):
        employee1 = setup()[1]#employee_1 table
        self.assertEqual(employee1.get_table_name(), employee1.table_name, "test_get_table failed")
        
   # not sure if this is correct
    def test_get_relations(self):
        employee1 = setup()[1]#employee_1 table
        self.assertEqual(hg.viz_data_table.get_relations(),employee1.mapping_relation,"test_get_relations failed")

    def test_graphviz_convert_export(self):
        employee1 = setup()[1]#employee_1 table
        export_path = "employee1.txt"
        employee1.graphviz_convert_export(export_path)
        self.assertTrue(os.path.exists(export_path),"test_graphviz failed")

    def test_relation_mapping(self):
        manager = setup()[0]#manager table
        employee1 = setup()[1]#employee_1 table
        hg.viz_data_table.relation_mapping(manager, employee1, "Manager_ID", "Manager_ID")
        
        self.assertEqual(hg.viz_data_table.mapping_relation, [("Manager:Manager_ID", "EMP_1:Manager_ID")],"test_relation failed")

    def test_drop_relations(self):
        hg.viz_data_table.mapping_relation = [("Manager:Manager_ID", "EMP_1:Manager_ID"),]
        hg.viz_data_table.drop_relations(("Manager:Manager_ID", "EMP_1:Manager_ID"))
        self.assertEqual(hg.viz_data_table.mapping_relation, [])
    
    def test_len(self):
        employee1 = setup()[1]#employee_1 table
        self.assertEqual(len(employee1), 4, "test_len failed")
    

def setup():
    """
    Initialize the test case
    """

    manager_entity = [('Manager_name','TEXT'),('Manager_ID','INTEGER')]

    employee1_entity = [('Manager_ID','INTEGER'),('Employee_name','TEXT'),('Employee_ID','TEXT'),('Employee_age','INTEGER')]



    #create objects/tables
    manager = hg.viz_data_table(table_name = 'Manager', table_entity = manager_entity)
    
    employee1 = hg.viz_data_table(table_name = 'EMP_1', table_entity = employee1_entity)
    
    return [manager, employee1]
    

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
