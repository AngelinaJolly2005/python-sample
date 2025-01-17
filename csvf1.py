import csv
import random

#create new csv file
def create_csv(filename, headers, rows):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"CSV file '{filename}' created successfully")

# Function to generate random data
def generate_data(num_rows):
    names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
    departments = ["HR", "Software Developer", "Sales", "Marketing", "Finance", "IT", "Operations", "Legal"]
    
    rows = []
    for i in range(1, num_rows + 1):
        name = random.choice(names)
        age = random.randint(20, 60)  # Random age between 20 and 60
        department = random.choice(departments)
        rows.append([i, name, age, department])
    
    return rows

filename = "sample_data.csv"
headers = ["ID", "Name", "Age", "Department"]
num_rows = 1000
rows = generate_data(num_rows)

create_csv(filename, headers, rows)
