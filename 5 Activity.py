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
        self.alumnos.append(Alumno(name, carne, carrera, note))

    def Mostrar(self):
        a = 1
        print("Lista de Alumnos: ")
        for alumno in self.alumnos:
            print(f"{a}) Nombre: {alumno.nombre}, Carne: {alumno.carne}, Carrera: {alumno.carrera}, Nota Final: {alumno.note}")
            a += 1

    def BuscarAlumno(self):
        buscarcarne = input("Ingrese el carné del alumno")
        for alumno in self.alumnos:
            if alumno.carne == buscarcarne:
                print(f"Hemos encontrado ha el Alumno: {alumno.nombre} con el carne: {alumno.carne}")
                print(f"Datos del Alumno:")
                print(f" Carrera: {alumno.alumnos}, Nota Final: {alumno.note}")

    def PromedioNotas(self):
        promedio = 0
        for alumno in self.alumnos:
            promedio += alumno.note
        print(f"El promedio de los alumnos es: {promedio/len(self.alumnos)}")


def main():
    students = Colegio()
    while True:
        try:
            print("1) Registrar Alumno")
            print("2) Mostrar Lista de Alumnos")
            print("3) Buscar Alumno por su carné")
            print("4) Promedio notas de todos los alumnos")
            print("5) Salir")

            op = input("Seleccione una opción:")

            if op == "1":
                students.Registro()
            elif op == "2":
                students.Mostrar()
            elif op == "3":
                students.BuscarAlumno()
            elif op == "4":
                students.PromedioNotas()
            elif op == "5":
                break

        except:
            print("Hubo un error ")



main()