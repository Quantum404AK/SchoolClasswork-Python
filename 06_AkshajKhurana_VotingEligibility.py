print("~~~~~ CHECK IF YOU ARE ELIGIBLE FOR VOTING ~~~~~")
print("")
name = input("Type your name: ")
age = int(input("Enter your age: "))

print("")
print("-----------------------------------------")
print("")

if age >= 18:
    print("{0} is eligible for voting.".format(name))
else:
    print ("{0} is NOT eligible for voting.".format(name))