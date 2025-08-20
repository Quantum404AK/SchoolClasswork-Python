num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("")
print("-----------------------------------------")
print("")

if num1 > num2:
    print("{0} is greater than {1}.".format(num1, num2))
elif num1 < num2:
    print ("{1} is greater than {0}.".format(num1, num2))
else:
    print ("{0} and {1} are equal.".format(num1, num2))