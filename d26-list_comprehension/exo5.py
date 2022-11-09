
import random
names = [ 'Alex', "Beth", "Carolina", "Dave", "Eleanor", "Freddie" ]
i=0
students_scores = { name:random.randint(1,100) for name in names  }

print(students_scores)


passed_students = { name:value for (name,value) in students_scores.items() if value>=60 }
print("passed : ", passed_students)