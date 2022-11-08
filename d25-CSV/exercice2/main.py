import pandas
data = pandas.read_csv("Squirrel_Data.csv")

print()

dict = {
    "colors" : ["black","gray","red"],
    "count" : [ len(data[data['Primary Fur Color']=='Black']), len(data[data['Primary Fur Color']=='Gray']), len(data[data['Primary Fur Color']=='Cinnamon'])]
}

color_data = pandas.DataFrame(data=dict)

print(color_data)

color_data.to_csv("fur_data.csv")