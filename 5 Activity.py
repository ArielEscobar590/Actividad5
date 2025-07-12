class Alumno:
    def __init__(self, nombre, carne, carrera, note):
        self.nombre = nombre
        self.carne = carne
        self.carrera = carrera
        self.note = note

class Colegio:
    def __init__(self):
        self.alumnos = []

    def Registro(self):
        name = input("Nombre: ")
        carne = input("Carne: ")
        carrera = input("Carrera: ")
        note = input("Nota Final: ")
        self.alumnos.append(alumno)

    def Mostrar(self):
        print("Lista de Alumnos: ")
        for alumno in self.alumnos:
            print(f"{a}) Nombre: {alumno.nombre}, Carne: {alumno.carne}, Carrera: {alumno.carrera}, Nota Final: {alumno.note}")

    def BuscarAlumno(self):
        print("Ingrese el carné del alumno")


def main():
    students = Colegio()
    print("1) Registrar Alumno")
    print("2) Mostrar Lista de Alumnos")
    print("3) Buscar Alumno por su carné")
    print("4) Promedio notas de todos los alumnos")
    op = input("Seleccione una opción:")

    if op == "1":
        students.Registro()





main()