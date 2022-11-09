import re

file1 = open("file1.txt","r")
list1 = [ int(re.sub("\s","",st)) for st in file1.readlines() ]
file2 = open("file2.txt","r")
list2 = [ int(re.sub("\s","",st)) for st in file2.readlines() ]


print(list1, list2)
# Write your code above 👆


result = [ n for n in list1 if n in list2 ]


print(result)


