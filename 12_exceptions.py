### Exceptions Handling ###

def sum(number_one,number_two):
    return number_one + number_two

number_one = 5
number_two = 1
number_two = "1"
#try except
try:
    print(sum(number_one, number_two))
    print("No se ha ocurrido un error")
except:
    print("Ha ocurrido un error")

print("El programa continua...")

#try except else
try:
    print(sum(number_one, number_two))
    print("No se ha ocurrido un error")
except:
    print("Ha ocurrido un error")
else:   #These code execute if all was good, without exceptions
    print("El programa continua...")
finally: #Finally always go to execute
    print("El programa continua desde el finally...")

# Typed Exceptions
try:
    print(sum(number_one, number_two))
    print("No se ha ocurrido un error")
except TypeError:
    print("Ha ocurrido un error de tipo TypeError")
except ValueError:
    print("Ha ocurrido un error de tipo ValueError")
except:
    print("Ha ocurrido un error")

# Captured Exceptions
try:
    print(sum(number_one, number_two))
    print("No se ha ocurrido un error")
except TypeError as error:
    print(f"Ha ocurrido un error de tipo TypeError: {error} ")
except Exception as error:
    print(f"Ha ocurrido un error: {error} ")

try:
    print(sum(number_one, number_two))
    print("No se ha ocurrido un error")
except ValueError as error:
    print(f"Ha ocurrido un error de tipo ValueError: {error} ")
except Exception as error:
    print(f"Ha ocurrido un error: {error} ")