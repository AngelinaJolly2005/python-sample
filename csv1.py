import os
import csv


def create_csv(filename,header,rows):
    file = open(filename,mode='w',newline='')
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)
    print(f"CSV File '{filename}' created successfully")

filename = "newfile.csv"
header = ["ID","Name","Age","Dept"]
rows = [
        {1,"Alice",30,"HR"},
        {2,"Bob",25,"Engg"},
        {3,"Charlie",35,"Sales"},
        {4,"Diana",28,"Marketing"}
    ]

create_csv(filename,header,rows)


def create_csv1(filename,header,num_rows):
    
    rows=[]
    for i in range(1,num_rows+1):
        current=['']*(len(header)-2)
        total=100
        row=[i]+current+[total]
        rows.append(row) 
    
    
    file=open(filename,mode='w',newline='')
    writer =csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)
    print("created succefully")

header1=["ID","Math","English","Computer","total"]

create_csv1("sample2.csv",header1,10)