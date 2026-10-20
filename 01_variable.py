#Variables
myVariable = "My String Variable" #Anti-pattern
print(myVariable)

"""
To define variables in Python you must use SNAKE_CASE
All in lowercase and underscore
"""

my_variable = "My String Variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable) # str converts a data type into str type
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#concatenate of variables
print(my_bool_variable, my_int_to_str_variable, my_variable)
print("This is the value of my_bool_variable:", my_bool_variable)

#Some system Functions
print(len(my_variable)) #the function len calculates the lenght of the variable

"""
Variables in only one line
¡¡WARNING!! Not abuse with this sintax, it can make errors
"""
name, surname, alias, age = "Alejandro", "González", "AleG", 28
print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

#Inputs of data
#name = input("What is your name? ");
#age = input("How old are you? ")
print(name)
print(age)

print("Me llamo:", name, surname, ". Mi edad es:", age, ". Y mi alias es:", alias)

#Change dta type
name = 2123
age = 'Alejandro'
print(name)
print(age)