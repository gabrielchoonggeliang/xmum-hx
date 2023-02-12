import sys  # this is used for name input, remove this later
from person import Person
from database import Data

# TODO: fastapi web app

# TODO: sql database to handle all the data

# TODO: algorithm to match the data
    # people matching according to their interests
    # only 1 rerolls per day

# create a person object for every person
# and add them to the database
for name in sys.argv[1:]:
    Data.append(Person(name))

# assign every person a connection except for themselves
for i in sys.argv[1:]:
    for j in sys.argv[1:]:
        if i != j:
            Data[sys.argv[1:].index(i)].add_connection(j)

# view the database
for individual in Data:
    print(individual.name, individual.interests, individual.connections)

while True:
    print("What would you like to do?")
    print("1. Add a person")
    print("2. Add an interest")
    print("3. Add a connection")
    print("4. Remove a person")
    print("5. Remove an interest")
    print("6. Remove a connection")
    print("7. View the database")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter the name of the person: ")
        Data.append(Person(name))
    elif choice == "2":
        name = input("Enter the name of the person: ")
        interest = input("Enter the interest of the person: ")
        Data[sys.argv[1:].index(name)].add_interest(interest)
    elif choice == "3":
        name = input("Enter the name of the person: ")
        connection = input("Enter the connection of the person: ")
        Data[sys.argv[1:].index(name)].add_connection(connection)
    elif choice == "4":
        name = input("Enter the name of the person: ")
        Data.remove(Data[sys.argv[1:].index(name)])
    elif choice == "5":
        name = input("Enter the name of the person: ")
        interest = input("Enter the interest of the person: ")
        Data[sys.argv[1:].index(name)].remove_interest(interest)
    elif choice == "6":
        name = input("Enter the name of the person: ")
        connection = input("Enter the connection of the person: ")
        Data[sys.argv[1:].index(name)].remove_connection(connection)
    elif choice == "7":
        for individual in Data:
            print(individual.name, individual.interests, individual.connections)
    elif choice == "8":
        break
    else:
        print("Invalid choice")

# view final database
for individual in Data:
    print(individual.name, individual.interests, individual.connections)