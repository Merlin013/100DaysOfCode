print("Wellcome to the Tip Calculator.")
total = float(input("What was the total bill? $"))
rate = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
split = float(input("How many people to split the bill? "))

overall_total = (total/split) * (1 + (rate/100))
print("Each person should pay: ${:.2f}".format(overall_total))
