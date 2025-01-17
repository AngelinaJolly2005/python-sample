num=int(input("Enter the number:"))
for i in range(1,num+1):
 
    print(" "*(num-i),end=" ")
    for j in range(1,i+1):
        print(j,end=" ")

    print()
for m in range(num,-1,1):
    print(" "*(num-m),end=" ")
    for n in range(m,-1,1):
        print(n,end=" ")

    print()
    
    
        