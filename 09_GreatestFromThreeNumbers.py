a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

print("")
print("-----------------------------------------")
print("")

if a > b and a > c:
    print ("Among {0}, {1} and {2}:\nThe number {0} is the greatest.".format(a, b, c))
elif b > a and b > c:
    print ("Among {0}, {1} and {2}:\nThe number {1} is the greatest.".format(a, b, c))
elif c > a and c > b:
    print ("Among {0}, {1} and {2}:\nThe number {2} is the greatest.".format(a, b, c))
elif a == b and a != c:
    print ("Among {0}, {1} and {2}:\nThe 1st and 2nd numbers are equal.".format(a, b, c))
elif b == c and b != a:
    print ("Among {0}, {1} and {2}:\nThe 2nd and 3rd numbers are equal.".format(a, b, c))
elif c == a and c != b:
    print ("Among {0}, {1} and {2}:\nThe 1st and 3rd numbers are equal.".format(a, b, c))
else:
    print("All the numbers are equal.")