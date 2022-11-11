import random
import re

letters="abcdefghijklmnopqrstuvwxyz"
numbers="0123456789"
symbols="!#$%&()*+"

def get_random_pass():
    needed_low_letter=letters[random.randint(0,len(letters)-1)].lower()
    needed_up_letter=letters[random.randint(0,len(letters)-1)]
    needed_number=numbers[random.randint(0,len(numbers)-1)]
    needed_symbol=symbols[random.randint(0,len(symbols)-1)]
    needed_chars=[needed_low_letter,needed_up_letter,needed_number,needed_symbol]

    rest = []
    for n in range(random.randint(8,15)):
        random_char=random.choice([c for c in (letters+numbers+symbols)])
        if re.match(r'[a-z]',random_char):
            random_char = random_char if random.randint(0,1)==1 else random_char.upper()
        rest.append(random_char)
    
    return "".join(rest+needed_chars)

get_random_pass()