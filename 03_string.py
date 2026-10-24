### Strings ###

my_string = "My String"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado"
print(my_scape_string)

my_scape_string = "\\tEste es un String \n escapado"  #\ is used to reject the tab in this case. 
print(my_scape_string)

# Format
name, surname, age = "Alejandro", "González", 28

print("Mi nombre es {} {} y mi edad es {}".format(name, surname,age)) #Useful for i18n or exceptions
print("Mi nombre es %s %s y mi edad es %d" %(name, surname,age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")  #the best use for format

# Desempaquetado de caracteres
language = "Python"
a,b,c,d,e,f = language
print(a)
print(e)

#Divide

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]  #All the variable in the first range x:y and print the multiple of 2
print(language_slice)

# Reverse
reverse_language = language[::-1]
print(reverse_language)

# Functions
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())