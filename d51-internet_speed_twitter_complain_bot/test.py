import re
str = "https://www.speedtest.net/fr/result/"
print( re.findall(r'[0-9]',str) )

