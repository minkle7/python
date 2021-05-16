import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("error: invalid input")
    sys.exit(1)
try:
    result = x / y
except ZeroDivisionError:
    print("error cannot be divide by 0.")
    sys.exit(10)    


print (f"{x} /{y} = {result} ")