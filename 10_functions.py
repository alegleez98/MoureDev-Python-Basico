### Functions ###

def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()

def sum_two_values(first_number, second_number):
    return first_number + second_number

print(sum_two_values(4,9))
print(sum_two_values(4457,1549))
print(sum_two_values(548494,323549))

def sum_two_values_with_default_value(first_number:int = 5, second_number:int = 6):  #This is not restrictive because od the language
    return first_number + second_number

print(sum_two_values_with_default_value())
print(sum_two_values_with_default_value(4))
print(sum_two_values_with_default_value(4457,1549))
print(sum_two_values_with_default_value("5","7"))

def print_name (name,surname):
    print(f"{name} {surname}")
print_name("González", "Alejandro")
print_name(surname = "González", name = "Alejandro")

def print_text_upper(*text):
    for element in text:
        print(element.upper())

print_text_upper("Hola")
print_text_upper("Hola", "Python", "AleG")