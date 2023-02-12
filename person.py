'''
This module contains the Person class.
'''

class Person():
    def __init__(self, name):
        self.name = name
        self.interests = []
        self.connections = []

    def add_interest(self, interest):
        self.interests.append(interest)

    def add_connection(self, connection):
        self.connections.append(connection)

    def remove_interest(self, interest):
        self.interests.remove(interest)

    def remove_connection(self, connection):
        self.connections.remove(connection)