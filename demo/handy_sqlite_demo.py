import handy_sqlite as hg
import csv
import sqlite3


#Define table entities
doctor_entity = [('Name','TEXT'),('Depart_ID','TEXT'),('Doc_ID','TEXT')]

#create objects/tables
doctor = hg.sqlite_data_table(table_name = 'Doctor', table_entity = doctor_entity)

#create dummy data
dummy_data = open('dummy_data.csv','w')
dummy_list = []

for i in range(20):
  dummy_list.append(['doc'+str(i),i,i%2])

with dummy_data:
  writer = csv.writer(dummy_data)
  writer.writerows(dummy_list)

dummy_data.close()

#create insert statement
doctor.insert_table('dummy_data.csv','insert_doc.sql')


#create sqlite db file
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()

doctor = open('Doctor.sql','r')
insert_doc = open('insert_doc.sql','r')

#execute create table statement
cursor.execute(doctor.read().replace('\n',''))

#execute insert table statement
for i in insert_doc.read().split(';'):
  i = i.replace('\n','')
  cursor.execute(i)

#execute select statement 
cursor.execute('select * from Doctor limit 5;')

#featch result
result = cursor.fetchall()


print(result)

doctor .close()
insert_doc.close()
cursor.close()
conn.close()
