# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

new_string = name1 + name2
lowercase_string = new_string.lower()

t = lowercase_string.count('t')
r = lowercase_string.count('r')
u = lowercase_string.count('u')
e = lowercase_string.count('e')

true_total = t + r + u + e

l = lowercase_string.count('l')
o = lowercase_string.count('o')
v = lowercase_string.count('v')
e = lowercase_string.count('e')

love_total = l + o + v + e

score = int(str(true_total) + str(love_total))

if (score < 10) or (score > 90):
    print("Your score is {}, you go together like coke and mentos.".format(score))
elif (score >= 40) and (score <= 50):
    print("Your score is {}, you are alright together.".format(score))
else:
    print("Your score is {}.".format(score))
