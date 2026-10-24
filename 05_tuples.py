### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (28, 1.90, "Alejandro", "Gonzalez")
my_other_tuple = (457, 895)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4])  IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count("Alejandro"))
print(my_tuple.index("Gonzalez"))

#my_tuple[1] = 1.80 TypeError because the tuple is inmutable
print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

del my_tuple
#print(my_tuple)  NameError because del delete the variable my_tuple, it doesn't do a clear
