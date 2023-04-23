import handy_data_table as h_dt 
import os
import csv

class sqlite_data_table(h_dt.data_table):

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
                line_value = line.split(',')
                value = ','.join("'"+ item + "'" for item in line_value)
                sql_statement.write('INSERT INTO ' + table_name + ' VALUES(' + value + ');\n')
            sql_statement.close()
