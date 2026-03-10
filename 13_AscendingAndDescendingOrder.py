a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
      
print("")
print("-----------------------------------------")
print("The Ascending order is:-")
if a>=b and a>=c:
    if b>=c:
        print (c, b, a)
    else:
        print (b, c, a)
elif b>=a and b>=c:
    if a>=c:
        print (c, a, b)
    else:
        print (a, c, b)
elif c>=a and c>=b:
    if a>=b:
        print (b, a, c)
    else:
        print (a, b, c)
        
        
print("")
print("-----------------------------------------")
print("The Descending order is:-")
if a>=b and a>=c:
    if b>=c:
        print (a, b, c)
    else:
        print (a, c, b)
elif b>=a and b>=c:
    if a>=c:
        print (b, a, c)
    else:
        print (b, c, a)
elif c>=a and c>=b:
    if a>=b:
        print (c, a, b)
    else:
        print (c, b, a)