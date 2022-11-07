#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# get the letter template content
try:    
    lFile = open("Input/Letters/starting_letter.txt")
    content = lFile.read()
    print("content : ",content)
except:
    print("wrong letter file !")
    exit()

def create_letter(name):
    new_content = content.replace("[name]", name)
    return new_content

# get the name list and write the letters
try:
    with open("Input/Names/invited_names.txt") as file:
        for name in file:
            letter = create_letter(name.strip()).strip()
            print("======>",letter)
            with open(f'./Output/letter_to_{name.strip()}.txt',"w") as file:
                file.write(letter)
except:
    print("no names found !")
    exit()
