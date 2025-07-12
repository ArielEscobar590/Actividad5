class Alumno:
    def __init__(self, nombre, carne, carrera, note):
        self.nombre = nombre
        self.carne = carne
        self.carrera = carrera
        self.note = note

class Colegio:
    def __init__(self):
        self.alumnos = []

    def Registro(self, alumno):
        self.alumnos.append(alumno)

    def Mostrar(self):
        print("Lista de Alumnos: ")
        for alumno in self.alumnos:
            print(f"{a}) Nombre: {alumno.nombre}, Carne: {alumno.carne}, Carrera: {alumno.carrera}, Nota Final: {alumno.note}")