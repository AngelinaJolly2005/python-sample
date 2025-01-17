num = int(input("Enter the number:"))
temp = num
c = 0

while num > 0:
    a = num % 10
    c = c + a * a * a
    num = num // 10

if c == temp:
    print("Armstrong")
else:
    print("Not Armstrong")
