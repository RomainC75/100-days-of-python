import re
from sheety import Sheety

print("welcome to my Flight Club")
print("We'll find the best flight for you")
first_name = input("What is your first name ? ")
last_name = input("What is your last name ? ")

is_email_not_valid = True
while is_email_not_valid:
  email = input("What is your email ? ")
  verif = input("Please enter you email again... ")
  if not re.match(
      r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$",
      email):
    print("the email is not valid")
  elif email == verif:
    is_email_not_valid = False
    sheety = Sheety()
    sheety.post_new_user(first_name, last_name, email)
  else:
    print("the emails are not the same. Please do it again")

print("ok, you are in the club, wait for the good news")
