import sys

# TODO: fastapi web app

# TODO: sql database to handle all the data

# TODO: algorithm to match the data
    # people matching according to their interests
    # only 1 rerolls per day

# TODO: parameter for the algorithm

class Person():
    def __init__(self, name):
        self.name = name
        self.interests = []
        self.connections = []

    def add_interest(self, interest):
        self.interests.append(interest)

    def add_connection(self, connection):
        self.connections.append(connection)

Person_database = [] 

# create a person object for every person
# and add them to the database
for name in sys.argv[1:]:
    Person_database.append(Person(name))

# assign every person a connection except for themselves
for i in sys.argv[1:]:
    for j in sys.argv[1:]:
        if i != j:
            Person_database[sys.argv[1:].index(i)].add_connection(j)

# view the database
for individual in Person_database:
    print(individual.name, individual.interests, individual.connections)