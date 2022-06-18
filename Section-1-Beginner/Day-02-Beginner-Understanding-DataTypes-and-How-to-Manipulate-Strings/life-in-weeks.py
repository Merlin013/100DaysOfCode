# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age_number = int(age)
years_remaining = 90 - age_number
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print("You have {} days, {} weeks, and {} months left."
      "".format(days_remaining, weeks_remaining, months_remaining))