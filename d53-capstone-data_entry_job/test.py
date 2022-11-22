import re
str = "$2,249+ 1 bd"
res = re.findall(r"[0-9,]+", str)[0]
print("res : ", res)