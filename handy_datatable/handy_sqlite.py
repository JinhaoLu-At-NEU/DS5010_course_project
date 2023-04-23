import sqlite3
import os


sqlite_dataType = ['NULL', 'INTEGER', 'REAL', 'TEXT', 'BLOB']

class sqlite_data_table:
    """
    Create data table for use in relational database
    Define entities of the table
    """

    def __init__(self, table_name, table_entity = [], primary_key = None, forign_key = []):
        #Initialize the table with given table entities (default is None)
        #The table_entity will be a list of tuples [(entity_name, entity_dataType)]
        #SQlite3 supported data type: NULL, INTEGER, REAL, TEXT, BLOB
        self.table_name = table_name
        self.table_entity = table_entity
        self.entity_list = [x[0] for x in table_entity]
        self.pk = primary_key
        self.fk = forign_key

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

    def get_fk(self):
        return self.fk 

    def file_if_exists(file):
        if os.path.exists(file):
            return True
        else:
            return False

    def check_value_column(self, datafile):
        entity_num = len(self.entity_list)
        line_num = 0
        if file_if_exists(datafile) is True:
            data_file = open(datafile)
            for line in data_file:
                value = line.split(',')
                if len(value) != entity_num:
                    print('Number of insert values not fit')
                    print('False index #', line_num)
                    return False
                else:
                    return True
        else:
            print('data file doesn\'t exist')
            return False


    def create_table(self):
        pk = self.pk 
        table_name = self.table_name
        sql_file = open(table_name+'.sql','w')
        sql_file.write('CREATE TABLE ' + table_name +'(\n')
        table_entity = self.table_entity
        num = 0
        for i in table_entity:
            name = i[0]
            dataType = i[1]
            num += 1 
            if name == pk:
                sql_file.write(name + ' ' + dataType + ' PRIMARY KEY,\n')
            elif num == len(table_entity):
                sql_file.write(name + ' ' + dataType + ');\n')
            else:
                sql_file.write(name + ' ' + dataType + ',\n')
        sql_file.close()


    def check_line_num(data_file):
        line = open(data_file,'r')
        line_num = line.readlines()
        line.close()
        return line_num

    def insert_table(self, data_file,export_path):
        table_name = self.table_name
        entity_list = self.entity_list
        sql_statement = open(export_path, 'w')
        if os.path.exists(data_file) is not True:
            print('Data file not found')
            return 0
        else:
            line_num = sqlite_data_table.check_line_num(data_file)
            data_file = open(data_file, 'r')
            num = 0
            for line in data_file:
                sql_statement.write('INSERT INTO ' + table_name + ' VALUES(' + line + '),\n')
            sql_statement.close()


