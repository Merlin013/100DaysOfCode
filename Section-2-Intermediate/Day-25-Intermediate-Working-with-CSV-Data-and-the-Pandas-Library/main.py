# # with open("weather_data.csv") as file:
# #     data = file.readlines()
#
# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     # print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)