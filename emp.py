import pandas as pd


data = {
    'Name':['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 28],
    'Salary': [50000, 60000, 70000, 80000, 55000],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Operations'],
    'Experince': [2,3 ,4 ,5 ,1.5 ],
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)