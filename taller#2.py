class animal:
    def __init__(self,nombre):
        self.nombre = nombre

    def __repr__(self):
        return f"el nombre es {self.nombre}"

    def moverse(self):
        print("el animal se mueve")


class perro(animal):

    def moverse(self):
        print(f"el perro {self.nombre} camina")

class pez(animal):

    def moverse(self):
        print(f"el pez {self.nombre} nada")

class reptil(animal):

    def moverse(self):
        print(f"el reptil {self.nombre} se arrastra")

    def trabajaanimal(animal):
        print(animal)
        animal.moverse()


print('que mascota quieres?')
print('1-perro, 2-pez, 3-reptil,')
opcion=int(input())

nombre=input('que nombre tiene?')

if opcion == 1:
    mimascota=perro(nombre)

elif opcion == 2:
    mimascota=pez(nombre)

else:
    mimasmota=reptil(nombre)

# invocamos a trabajoanimal para que funcione de forma polimorfica
trabajoanimal(mimasmota)
print('......')





