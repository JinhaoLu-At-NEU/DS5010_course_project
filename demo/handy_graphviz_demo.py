from graphviz import *
import graphviz
import handy_graphviz as hg

#Define table entities
department_entity = [('Depart_name','TEXT'),('Depart_ID','TEXT')]

doctor_entity = [('Name','TEXT'),('Depart_ID','TEXT'),('Doc_ID','TEXT')]

patient1_entity  = [('Name','TEXT'),('PAT_ID','INTEGER'),('Doc_ID','TEXT')]
patient2_entity  = [('Name','TEXT'),('PAT_ID','INTEGER'),('Doc_ID','TEXT')]
patient3_entity  = [('Name','TEXT'),('PAT_ID','INTEGER'),('Doc_ID','TEXT')]

#create objects/tables
department = hg.viz_data_table(table_name = 'Department', table_entity = department_entity)
doctor = hg.viz_data_table(table_name = 'Doctor', table_entity = doctor_entity)
patient1 = hg.viz_data_table(table_name = 'PAT1', table_entity = patient1_entity)
patient2 = hg.viz_data_table(table_name = 'PAT2', table_entity = patient2_entity)
patient3 = hg.viz_data_table(table_name = 'PAT3', table_entity = patient3_entity)


#Mapping relationships between tables
hg.viz_data_table.relation_mapping(department,doctor,'Depart_ID','Depart_ID')
hg.viz_data_table.relation_mapping(doctor,patient1,'Doc_ID','Doc_ID')
hg.viz_data_table.relation_mapping(doctor,patient2,'Doc_ID','Doc_ID')
hg.viz_data_table.relation_mapping(doctor,patient3,'Doc_ID','Doc_ID')


#Convert and output the table structure into dot scripts
department.graphviz_convert_export('department.txt')
doctor.graphviz_convert_export('doctor.txt')
patient1.graphviz_convert_export('patient1.txt')
patient2.graphviz_convert_export('patient2.txt')
patient3.graphviz_convert_export('patient3.txt')

#Read the output
depart_dot = open('department.txt','r')
doc_dot = open('doctor.txt','r')
pat1_dot = open('patient1.txt','r')
pat2_dot = open('patient2.txt','r')
pat3_dot = open('patient3.txt','r')


demo_graph = graphviz.Digraph('structs', filename = 'structs.gv',
                              node_attr = {'shape':'plaintext'})

demo_graph.graph_attr['rankdir'] = 'LR'

demo_graph.node(department.get_table_name(),depart_dot.read())
demo_graph.node(doctor.get_table_name(),doc_dot.read())
demo_graph.node(patient1.get_table_name(),pat1_dot.read())
demo_graph.node(patient2.get_table_name(),pat2_dot.read())
demo_graph.node(patient3.get_table_name(),pat3_dot.read())


#Creat mapping edges 
demo_graph.edges(hg.viz_data_table.get_relations())


#export mapping graph file
demo_graph.render(filename='demo_graph', view = True)


#Files close
depart_dot.close()
doc_dot.close()
pat1_dot.close()
pat2_dot.close()
pat3_dot.close()
