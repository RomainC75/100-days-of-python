import pandas 

students_dict = {
    "students": [ "Angela", "James", "Lily" ],
    "score": [56, 76, 98]
}

students_data_frame = pandas.DataFrame(students_dict)
print(students_data_frame)

for (key,value) in students_data_frame.items():
    print(value)

#pandas loop
for (index,row) in students_data_frame.iterrows():
    print(index, "====", row)