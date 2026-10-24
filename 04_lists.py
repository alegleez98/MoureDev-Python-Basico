### Lists ###

my_list = list()
my_other_list = []
print(type(my_list))
print(type(my_list))
# my_list and my_other_list is the same type <class 'list'>


print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [28, 1.90, "Alejandro", "González"]
print(type(my_other_list))

print("Mi edad es " + str(my_other_list[0]))
print("Mi altura es " + str(my_other_list[1]))
print("Mi apellido es " + my_other_list[-1]) #With -1 is the last index of the list
print("Mi nombre es " + my_other_list[-2])

#print(my_other_list[4])  #IndexError because the element 4 not exist
#print(my_other_list[-5]) #IndexError because the size is 4 and the -5 index not existe
print(my_other_list.count(28))
print(my_other_list.count("Alejandro"))
print(my_list.count(30))

age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list)

my_other_list.append("AleG")
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)  #Only will remove the first element that find

#my_list.pop()  #Delete the index element of the list and return the value. If it is () is the last one.
my_pop_element = my_list.pop()
print(my_pop_element)
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]  #del delete with index but remove delete with the value inside of the list.
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2])
print(my_new_list[1:3])

