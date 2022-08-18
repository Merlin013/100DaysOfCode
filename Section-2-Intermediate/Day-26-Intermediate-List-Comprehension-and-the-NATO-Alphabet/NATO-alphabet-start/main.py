student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
file = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(file)
#TODO 1. Create a dictionary in this format:
new_dict = {row.letter: row.code for (index, row) in file.iterrows()}
print(new_dict)

# print(new_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():

    name = input("enter your name: ").upper()
    try:
        phonetic_list = [new_dict[letter] for letter in name]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()