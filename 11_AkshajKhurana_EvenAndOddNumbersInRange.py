a = int(input("Enter the starting number: "))
b = int(input("Enter the final number: "))
print ("-------------------------------------")

num = a
print()
print("Even numbers in this range are:")
while num<=b:
    if num%2 == 0:
        print (num)
    num+=1
print()
num = a
print("-------------------------------------")
print("Odd numbers in this range are:")
while num<=b:
    if num%2 == 1:
        print (num)
    num+=1