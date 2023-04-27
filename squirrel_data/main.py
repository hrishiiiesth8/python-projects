# # import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for city, temperature, condition in data:
# #         temperatures.append(temperature)
# #     temperatures.remove("temp")
# #     print(temperatures)
# # import math
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # temperatures = data["temp"]
# # print(data["temp"])
# #
# # data_dict = data.to_dict()
# # # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# # average = sum(temp_list)/len(temp_list)
# # print(average)
# # or
# # print(data["temp"].mean())
# # print(data["temp"].max())
# # print(data.condition)
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
# #
# # day = data[data.day == "Monday"]
# # print(day.condition)
# # print((9*day.temp/5)+32)
#
# marks_list = {
#     "mates": ["jayprakash", "kk", "swati", "godara"],
#     "cgpa": [8, 7, 10, 6]
#
# }
# data_new = pandas.DataFrame(marks_list)
# print(data_new)
# data_new.to_csv("marks.csv")


import pandas
data = pandas.read_csv("squirrel_data.csv")
# better direct method to count
# grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
# black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
# cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
color_list = data["Primary Fur Color"].to_list()
gray = color_list.count("Gray")
black = color_list.count("Black")
cinnamon = color_list.count("Cinnamon")
count_data = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray, black, cinnamon]
}
new_count = pandas.DataFrame(count_data)
print(new_count)
new_count.to_csv("squirrel_counts.csv")