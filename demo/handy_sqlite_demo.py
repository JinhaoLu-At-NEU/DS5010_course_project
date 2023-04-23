import handy_sqlite as hg
import sqlite3


#Define table entities
doctor_entity = [('Name','TEXT'),('Depart_ID','TEXT'),('Doc_ID','TEXT')]

#create objects/tables
doctor = hg.sqlite_data_table(table_name = 'Doctor', table_entity = doctor_entity)

#convert to sql create table statement
doctor.create_table()

#create dummy data
dummy_data = open('dummy_data.csv','w')
for i in range(20):
  dummy_data.write('d'+str(i)+','+str(i)+','+str(i%2)+'\n')
dummy_data.close()

#Generate insert statement
doctor.insert_table('dummy_data.csv','insert_doc.sql')


#create sqlite database 
conn = sqlite3.connect('demo.db')
cursor = conn.cursor()

doctor = open('Doctor.sql','r')

#create data table wth the output
cursor.execute(doctor.read().replace('\n',''))


doctor.close()
cursor.close()
conn.close()
