### Dictionary ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Alejandro", "Apellidos": "González", "Edad": 28, 1:"Python"}
my_dict = {
    "Nombre": "Alejandro",
    "Apellidos": "González", 
    "Edad": 28, 
    "Lenguajes": {
        "Python",
        "Java",
        "JavaScript"
    },
    1: 1.90
}
print(len(my_other_dict))
print(len(my_dict))
print(my_dict)
print(my_other_dict)

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pepe" #Change the value of a member of the dictionary
print(my_dict["Nombre"])
print(my_dict[1])

my_dict["Calle"] = "Calle La Esperanza"
print(my_dict) #Insert a new member in the dictionary

del my_dict["Calle"]
print(my_dict) #Delete a member of the dictionary

print("Apellidos" in my_dict) #It searchs for keys, it doesn't search for values
print("González" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())
print(my_dict.fromkeys(("Nombre", 1)))

my_new_dict = print(dict.fromkeys(("Nombre", 1, "Piso"))) #dict is a system variable to access some functions
print(my_new_dict)  #Creates a new dictionary with keys that you pass but without values
my_list = ["Nombre", 1, "Piso"]
my_new_dict = print(dict.fromkeys(my_list))
print(my_new_dict)
my_new_dict = print(dict.fromkeys(my_dict)) #Copy the dictionary without values
print(my_new_dict)


