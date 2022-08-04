# Reading a file
# with open("hello world.txt") as file:
#     contents = file.read()
#     print(contents)

# writing to a file

with open("hello world.txt", mode="a") as file:
    file.write("\nNew Text. This file is for practice.")
