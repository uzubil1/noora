import csv

def names_and_addresses(filename):
    with open('full_grades_010.csv','r') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            full_name = row[0]
            address = row[1]
            print(f"name:{full_name}, address:{address}")


names_and_addresses()