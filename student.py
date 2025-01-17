import pandas as pd 
data = { 
    "student_name": ["Alice","Bob","Charlie","David","Eva"],
    "marks": [86,45,90,88,43]
    ,"grades": ['A','E','A','A','F+']
    }
myvar = pd.DataFrame(data)

print(myvar)
df= pd.DataFrame(data)
filter=df[df["marks"]>50]
print(filter)
#for i in myvar.index:
   # if myvar.loc[i,"marks"]>50:
        #print(myvar.loc[i])
    #else:
        #continue
