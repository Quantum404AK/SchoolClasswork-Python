num = int(input("Enter the number: "))

print("")
print("-----------------------------------------")
print("")

if num > 0:
    print("{0} is positive.".format(num))
elif num < 0:
    print ("{0} is negative.".format(num))
else:
    print ("{0} is neither positive nor negative.".format(num))