### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # First, this is a dictionary

my_other_set = {"Alejandro", "González", 28}
print(type(my_other_set)) #Because of the inserts in the value, type changes to set

print(len(my_other_set))

my_other_set.add("AleG")
print(my_other_set)  #Sets isn't a order structure

my_other_set.add("AleG")
print(my_other_set) #Sets don't permit repeat values

print("Alejandro" in my_other_set)
print("Moure" in my_other_set)

my_other_set.remove("González")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) NameError because del deletes the variable my_other_set

my_set = {"Alejandro", "González", 28}
my_list = list(my_set)
print(my_list)
print(my_list[0]) #Don't do that because you don't know what is in the first element

my_other_set = {"Kotlin", "Swift", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_new_set).union(my_new_set)) #Sets don't repeat values

print(my_new_set.difference(my_set))