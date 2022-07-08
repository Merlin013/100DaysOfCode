from calculator_art import logo


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


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in symbols:
        print(symbol)
    should_continue = True
    while should_continue:

        operation = input("Which operations do you want to perform? ")
        num2 = float(input("What's the next number?: "))

        answer = symbols[operation](num1, num2)

        print("{} {} {} = {}".format(num1, operation, num2, answer))
        if input("Type 'y' to continue calculating with {}, "
                 "or type 'n' to start a new calculation: ".format(answer)) == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
