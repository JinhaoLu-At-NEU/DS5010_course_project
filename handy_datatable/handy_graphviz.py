import os

sqlite_dataType = ['NULL', 'INTEGER', 'REAL', 'TEXT', 'BLOB']

class viz_data_table:
    """
    Create data table for use in relational database
    Define entities of the table
    """
    mapping_relation = []

    def __init__(self, table_name, table_entity = [], primary_key = None, forign_key = []):
        #Initialize the table with given table entities (default is None)
        #The table_entity will be a list of tuples [(entity_name, entity_dataType)]
        #SQlite3 supported data type: NULL, INTEGER, REAL, TEXT, BLOB
        self.table_name = table_name
        self.table_entity = table_entity
        self.entity_list = [x[0] for x in table_entity]

    def add(self, entity_name, entity_dataType):
        #Add entity to the table by specific the datatype of the entity
        #The entity name must be unique in the data table
        table_entity = self.table_entity.copy()
        entity_list = self.entity_list.copy()
        if entity_dataType not in sqlite_dataType:
            print('Add entity fail \n')
            print('Entity data type not supported by SQLite3')
        elif entity_name not in entity_list:
            table_entity.append((entity_name,entity_dataType))
            entity_list.append(entity_name)
            self.entity_list = table_entity
            self.table_entity = table_entity
            print('Entity Added')
        else:
            print("Add entity fail \n")
            print("Entity name in the table must be unique \n")

    def drop(self, entity_name):
        #Drop entity from the table
        table_entity = self.table_entity.copy()
        entity_list = self.entity_list.copy()
        if entity_name not in entity_list:
            print("Drop entity fail \n")
            print("Entity name not found \n")
        else:
            for i in range(table_entity):
                e_name = table_entity[i]
                if e_name[0] == entity_name:
                    table_entity.remove(e_name)
                    break
            entity_list.remove(entity_name)
            self.table_entity = table_entity
            self.entity_list = entity_list
            print('Entity dropped')

    def table_status(self):
        print(self.table_name)
        table_entity = self.table_entity.copy()
        for i in range(len(table_entity)):
            entity = table_entity[i][0]
            dataType = table_entity[i][1]
            print(i+1,': ', entity,'\t', dataType)

    def __len__(self):
        #return number of entity from the table
        return len(self.entity_list)

    def get_entity(self):
        return self.entity_list

    def get_table_name(self):
        return self.table_name

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
        viz_data_table.mapping_relation.remoce(relation)
        print(relation + 'has been dropped')

    def get_relations():
        return viz_data_table.mapping_relation
