n1=int(input())
n2=int(input())
try:
    print(f"Division of {n1} and {n2} is {n1/n2}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
finally:
    print("Execution Completed")