# Add function
def add(n1, n2):
    return n1 + n2


# Sub function
def sub(n1, n2):
    return n1 - n2


# Multiply function
def mul(n1, n2):
    return n1 * n2


# Divide function
def div(n1, n2):
    return n1 / n2


symbols = {"+": add,
           "-": sub,
           "*": mul,
           "/": div}


num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for symbol in symbols:
    print(symbol)
operation = input("Which operations do you want to perform? ")
value = symbols[operation](num1, num2)

print("{} {} {} = {}".format(num1, operation, num2, value))
