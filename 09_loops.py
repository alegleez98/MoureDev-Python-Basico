### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("El bucle ha finalizado")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

# For
my_list = [35, 24, 62, 52, 30, 30, 17]
for element in my_list:
    print(element)

my_other_dict = {"Nombre": "Alejandro", "Apellidos": "González", "Edad": 28, 1:"Python"}
for element in my_other_dict:  #Print the keys
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")

for element in my_other_dict.values():  #Print the values
    print(element)

my_tuple = (28, 1.90, "Alejandro", "Gonzalez")
for element in my_tuple:
    print(element)

my_set = {"Alejandro", "González", 28}
for element in my_set:
    print(element)
print("La ejecución continua")