import handy_sqlite as hg
import sqlite3
import csv


#Define table entities
doctor_entity = [('Name','TEXT'),('Depart_ID','TEXT'),('Doc_ID','TEXT')]

#create objects/tables
doctor = hg.sqlite_data_table(table_name = 'Doctor', table_entity = doctor_entity)

#convert to sql create table statement
doctor.create_table()

#create dummy data
dummy_data = open('dummy_data.csv','w', newline = '')
dummy_list = []
for i in range(20):
  dummy_list.append(['doc'+str(i),i,i%2])

with dummy_data:
  writer = csv.writer(dummy_data)
  writer.writerows(dummy_list)

dummy_data.close()

#Generate insert statement
doctor.insert_table('dummy_data.csv','insert_doc.sql')


#create sqlite database 
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()

doctor = open('Doctor.sql','r')
insert_doc = open('insert_doc.sql','r')

#create data table wth the output
cursor.execute(doctor.read().replace('\n',''))

for i in insert_doc.read().split(';'):
  i = i.replace('\n','')
  cursor.execute(i)

cursor.execute('select * from Doctor limit 5;')

result = cursor.fetchall()

doctor .close()
insert_doc.close()
cursor.close()
conn.close()

print(result)
