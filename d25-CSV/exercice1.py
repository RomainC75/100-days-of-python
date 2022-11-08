# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv    

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     # print(data)
#     for row in list(data)[1:] :
#         temperature.append(int(row[1]))

#     print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
data_dict = data.to_dict()
print(data_dict)


series = data['temp'].to_list()
average_temp = sum(series)/len(series)

print(series, average_temp, data['temp'].mean())

print('=>',data['temp'].max())

print("row : ", data[data.day=="Thursday"].temp)

# get the row where the temp is at the maximum
max_index = data['temp'].argmax()

# print(data_dict['day'][max_index],data_dict['temp'][max_index], data_dict['condition'][max_index])
print('===>',data[data.temp==data['temp'].max()])

#challenge : get monday's temp in farenheit
monday = data[data.day=="Monday"]
print("monday : ", monday)
temp_F = int(monday["temp"])*9/5+32
print("monday's temp in Farenheit: ", temp_F)

#create a dataframe
data_dict = {
    "students" : [ "Any", "James", "Angela" ],
    "Scores" : [ 76, 56, 65 ]
}

data= pandas.DataFrame(data=data_dict)
data.to_csv("new_data.csv")
