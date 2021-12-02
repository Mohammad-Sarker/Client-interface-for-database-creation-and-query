from document import DocumentDatabase
from neo4j import GraphDatabase
from pprint import pprint

db_url = 'http://neo4j:pass@localhost:7474/db/data'

doc = DocumentDatabase()

tsv_file = input("Enter path of nodes tsv file: ")
edges_file = input("Enter path of edges tsv file: ")


print("\n\n")

db_url = input('enter uri for neo4j: ')
graph = GraphDatabase(db_url)

print("\nPreparing to generate database\n")

if(graph.is_database_empty()):
    graph.generate_database(tsv_file, edges_file)
else:
    print('neo4j Database located!')

print("\nNeo4j database generate successfully\n")

if(doc.is_database_empty()):
    doc.generate_database(tsv_file,edges_file)
else:
    print("mongoDB database found!")

print("\mongoDB database generate successfully\n")

while True:
    print('\n\nMenu\n')
    option = input('1- Search for a disease id \n2- Search for a disease name \nPress any other button to quit: \n')
    if option == "1":
        id = input("Enter a disease id: ")
        result = doc.get_disease(id)
        print('Results: ')
        pprint(result)

    elif option == "2":
        name = input("Enter a disease name: ")
        result = graph.get_treatments(name)
        print('Results: ')
        pprint(result)
    else:
        break

print("Exit code 0")