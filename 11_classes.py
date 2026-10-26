### Classes ###

class Person:
    
    def __init__(self, name = "", surname = "", alias = ""):
        self.full_name = f"{name} {surname} {alias}"

    def walk(self, kilometros):
        print(f"{self.full_name} está caminando {kilometros} km")
    
my_person = Person("Alejandro", "González")
print(my_person.full_name)
my_person.walk(30);

my_other_person = Person("Pepe", "Manuele", "AleG")
my_other_person.walk(40)
my_other_person.full_name = "Juan Manual Perez"
my_other_person.walk(64)
my_person_without_parameters = Person()

