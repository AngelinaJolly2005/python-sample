import pandas as pd
df = pd.read_csv('data.csv')

#print(df.to_string()) 

#print(df.head(10))
#print(df.head())
#print(df.tail()) 

#a = df.dropna()
#print(a.to_string())


#df.dropna(inplace = True)
#print(df.to_string())

#df = pd.read_csv('data.csv')
#df.fillna(130, inplace = True)
#print(df.to_string())



#df = pd.read_csv('data.csv')
#df["Calories"].fillna(130, inplace = True)
#print(df.to_string())

#x = df["Calories"].mean()
#df["Calories"].fillna(x, inplace = True)
#print(df.to_string())

#x = df["Calories"].median()
#df["Calories"].fillna(x, inplace = True)
#print(df.to_string())

#x = df["Calories"].mode()[0]
#df["Calories"].fillna(x, inplace = True)
#print(df.to_string())


#df["Date"]=pd.to_datetime(df['Date'])
#print(df.to_string())

#df.loc[20,"Duration"]= 35
#print(df.to_string())

for x in df.index:
    if df.loc[x,"Pulse"]>100:
        df.loc[x,"Pulse"]=777
print(df.to_string())

