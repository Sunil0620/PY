import pandas as pd

# data = pd.read_csv("Day25/weather_data.csv")
# print(type(data))   #DataFrame (2D) Object
# print(type(data["temp"])) # Series (1D) Object


# print(data[data["day"] == "Monday" ])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# temp_f = monday_temp * 9/5 + 32
# print(temp_f)

#Create a DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pd.DataFrame(data=data_dict)
# print(data)

# data.to_csv("Day25/data.csv")

data = pd.read_csv("Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrelas_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(red_squirrels_count)
print(black_squirrels_count)
print(grey_squirrelas_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrelas_count, red_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("Day25/squirrel_count.csv")
