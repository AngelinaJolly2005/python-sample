



while(True):
      print("1.ADDITION,2.SUBTRACTION,3.DIVISION,4.MULTIPLICATION")
      a=int(input("Enter the first num:"))
      b=int(input("Enter the first num:"))
      ch=int(input("Enter your choice:"))
      if ch==1:
         print("sum=",a+b)
      elif ch==2:
         print("Difference=",a-b)
      elif ch==3:
         print("Qoutient=",a/b,"Remainder=",a%b)
      elif ch==4:
         print("Product=",a*b)
      else:
         print("Invalid  choice")

      y=input("Do you want to continue y/n?:")
      if(y=="n"):
         break
   



