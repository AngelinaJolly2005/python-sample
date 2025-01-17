import csv
import os

#create new csv file
def create_csv(filename, headers, rows):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"csv file '{filename}' created successfully")

filename = "employee.csv"
headers = [ "Name", "Age","Salary", "Department","Experience"]
rows = [
    [ "Alice", 25, 50000, "HR", 2],
    ["Bob", 30, 60000,"Finance", 5],
    ["Charlie", 35, 70000,"Tech"],
    ["David", 40, 80000, "Tech"],
    ["Eva", 45, 90000, "HR"]
]

create_csv(filename, headers, rows)
