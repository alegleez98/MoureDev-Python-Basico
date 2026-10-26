### Modules ###
#import my_module
from my_module import sum

#print(my_module.sum(4,5))
#print(my_module.printValue("Hola Mundo"))

from my_module import sum, printValue

sum(7,9)
printValue("Hola Mundo")

import math

print(math.factorial(8))
print(math.pow(2,8))

from math import pi as PI_VALUE
print(PI_VALUE)
