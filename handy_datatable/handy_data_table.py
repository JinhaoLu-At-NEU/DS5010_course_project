import os

sqlite_dataType = ['NULL', 'INTEGER', 'REAL', 'TEXT', 'BLOB']

class data_table:

    def __init__(self,table_name, table_entity = [], primary_key = None, foreign_key = []):
        self.table_name = table_name
        self.table_entity = table_entity
        self.entity_list = [x[0] for x in table_entity]
        self.pk = primary_key
        self.fk = foreign_key

    def add(self, entity_name, entity_dataType):
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

    def __str__(self):
        return table_status(self)

    def __len__(self):
        #return number of entity from the table
        return len(self.entity_list)


    def set_primaryKey(self, entity_name):
        if entity_name not in self.entity_list:
            print('set primary key fail \n')
            print('Specific entity does not exists in the table \n')
        else:
            self.pk = entity_name
            print('set primary key succeed')
            print('Current primary key is: ', entity_name, '\n')

    def get_entity(self):
        return self.entity_list

    def get_pk(self):
        return self.pk

    def get_table_name(self):
        return self.table_name

    def get_fk(self):
        return self.fk 
