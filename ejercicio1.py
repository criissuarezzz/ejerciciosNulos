#crea una clase alumno que tenga como atributos nombre y nota
#crea un objeto de la clase alumno y pide los valores por teclado
#muestra los valores de los atributos de la clase alumno
#crea una clase alumno que tenga como atributos nombre y nota


class Alumno:
    
        def __init__(self, nombre, nota):
            self.nombre = nombre
            self.nota = nota
    
        def __str__(self):
            return "Nombre: " + self.nombre + " Nota: " + str(self.nota)
    
        def getNombre(self):
            return self.nombre
    
        def getNota(self):
            return self.nota
    
        def setNombre(self, nombre):
            self.nombre = nombre
    
        def setNota(self, nota):
            self.nota = nota

nombre = input("Introduce el nombre del alumno: ")  
nota = int(input("Introduce la nota del alumno: "))

alumno = Alumno(nombre, nota)

print(alumno)

# Path: ejercicio2.py
#crea una clase alumno que tenga como atributos nombre y nota
#crea un objeto de la clase alumno y pide los valores por teclado
#muestra los valores de los atributos de la clase alumno
#crea una clase alumno que tenga como atributos nombre y nota


class Alumno:
        
            def __init__(self, nombre, nota):
                self.nombre = nombre
                self.nota = nota
        
            def __str__(self):
                return "Nombre: " + self.nombre + " Nota: " + str(self.nota)
        
            def getNombre(self):
                return self.nombre
        
            def getNota(self):
                return self.nota
        
            def setNombre(self, nombre):
                self.nombre = nombre
        
            def setNota(self, nota):
                self.nota = nota
                