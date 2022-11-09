numbers = [1,2,3]
new_list= [ n+1 for n in numbers ]
print(new_list)

name="John"
new_list = [ letter for letter in name ]
print(f'name : {new_list}')


new_list = [ n*2 for n in range(1,5)]
print(f'doubled : {new_list}')

names = [ "John", "Bob", "Angela", "Jason", "Caroline" ]
new_list = [ name for name in names if len(name)<=4]
print(f'short names : {new_list}')

upperC = [ name.upper() for name in names if len(name)>5 ]
print(f'uppercase : {upperC}')

