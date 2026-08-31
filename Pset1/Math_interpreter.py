x, y, z = input("Enter two integers and an operator separated by spaces: ").split()

x = int(x)
z = int(z)

if y == '+':
    result = x + z
elif y == '-':
    result = x - z
elif y == '*':
    result = x * z
elif y == '/':
    if z == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    else:
        result = x / z
        

print(f"Result: {result:.2f}")
