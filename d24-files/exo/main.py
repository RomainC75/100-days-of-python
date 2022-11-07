# file = open("text.txt")
# content = file.read()
# print(content)
# file.close()


with open("text.txt", mode="a") as file:
    
    file.write("\nline3: bob")
    # print(content)

with open("new_file", mode="w") as file:
    file.write("my line")