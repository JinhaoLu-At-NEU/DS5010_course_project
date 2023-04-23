import handy_data_table as h_dt
import os

sqlite_dataType = ['NULL', 'INTEGER', 'REAL', 'TEXT', 'BLOB']

class viz_data_table(h_dt.data_table):

    mapping_relation = []

    def graphviz_convert_export(self, export_path):#convert data_table into graphviz dot file format 
        if os.path.exists(export_path) is True:
            dot_file = open(export_path, mode = 'a')
        else:
            dot_file = open(export_path, mode = 'w')
            dot_file.write('<<TABLE BORDARD=\"0\" CELLBORDER=\"1\" CELLSPACING =\"0\">\n')
        for entity in self.entity_list:
            dot_file.write('<TR>\n')
            dot_file.write('<TD PORT=\'' + entity + '\'>' + entity + '</TD>\n')
            dot_file.write('</TR>\n')
        dot_file.write('</TABLE>>\n')
        dot_file.close()


    def relation_mapping(table1, table2, table1_entity_name, table2_entity_name):
        if table1_entity_name not in table1.entity_list:
            print('Mapping relationship fail')
            print(table1_entity_name+' in '+table1+' not found')
        elif table2_entity_name not in table2.entity_list:
            print('Mapping relationship fail')
            print(table2_entity_name+' in '+table2+' not found')
        else:
            viz_data_table.mapping_relation.append((table1.table_name+':'+table1_entity_name,table2.table_name+':'+table2_entity_name))

    def relations_status():
        for i in viz_data_table.mapping_relation:
            print(i,'\n')

    def clean_relations():
        viz_data_table.mapping_relation = []

    def drop_relations(relation):
        viz_data_table.mapping_relation.remove(relation)
        print(str(relation) + 'has been dropped')

    def get_relations():
        return viz_data_table.mapping_relation
