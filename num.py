import numpy
arr=numpy.array([[1,2,3],[4,5,6]])

for i in arr:
    print(i)
for i in range(0,2):
    for j in range(0,3):
        if(arr[i][j]%2==0):
            arr[i][j]=arr[i][j]*arr[i][j]
        else:
            arr[i][j]=arr[i][j]*arr[i][j]*arr[i][j]
print("after replacing with odd and even")            
for i in arr:
    print(i)            

print("sum of new array")
sum=0
for i in range(0,2):
    for j in range(0,3):
        sum=sum+arr[i][j]

print("the sum is",sum)

arr1=arr.reshape(3,2)

for i in arr1:
    print(i)


         

