from abc import ABC, abstractmethod
#Funcion
class Prestamo(ABC):
    @abstractmethod
    def prestar(self):
        pass

    @abstractmethod
    def devolver(self):
        pass

class Material(ABC):
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    @abstractmethod
    def mostrar_informacion(self):
        pass

class Libro(Material, Prestamo):
    def __init__(self, titulo, autor, año, num_paginas):
        super().__init__(titulo, autor, año)
        self.num_paginas = num_paginas
        self.prestado = False

    def mostrar_informacion(self):
        print(f"Libro: {self.titulo}, Autor: {self.autor}, Año: {self.año}, Páginas: {self.num_paginas}")

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"{self.titulo} ha sido prestado.")
        else:
            print(f"{self.titulo} ya está prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"{self.titulo} ha sido devuelto.")
        else:
            print(f"{self.titulo} no estaba prestado.")

class Revista(Material):
    def __init__(self, titulo, autor, año, numero_edicion):
        super().__init__(titulo, autor, año)
        self.numero_edicion = numero_edicion

    def mostrar_informacion(self):
        print(f"Revista: {self.titulo}, Autor: {self.autor}, Año: {self.año}, Edición: {self.numero_edicion}")

class DVD(Material, Prestamo):
    def __init__(self, titulo, autor, año, duracion):
        super().__init__(titulo, autor, año)
        self.duracion = duracion
        self.prestado = False

    def mostrar_informacion(self):
        print(f"DVD: {self.titulo}, Director: {self.autor}, Año: {self.año}, Duración: {self.duracion} mins")

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"{self.titulo} ha sido prestado.")
        else:
            print(f"{self.titulo} ya está prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"{self.titulo} ha sido devuelto.")
        else:
            print(f"{self.titulo} no estaba prestado.")

class CD(Material, Prestamo):
    def __init__(self, titulo, autor, año, duracion):
        super().__init__(titulo, autor, año)
        self.duracion = duracion
        self.prestado = False

    def mostrar_informacion(self):
        print(f"CD: {self.titulo}, Artista: {self.autor}, Año: {self.año}, Duración: {self.duracion} mins")

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"{self.titulo} ha sido prestado.")
        else:
            print(f"{self.titulo} ya está prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"{self.titulo} ha sido devuelto.")
        else:
            print(f"{self.titulo} no estaba prestado.")

class Juego(Material, Prestamo):
    def __init__(self, titulo, autor, año, plataforma):
        super().__init__(titulo, autor, año)
        self.plataforma = plataforma
        self.prestado = False

    def mostrar_informacion(self):
        print(f"Juego: {self.titulo}, Desarrollador: {self.autor}, Año: {self.año}, Plataforma: {self.plataforma}")

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"{self.titulo} ha sido prestado.")
        else:
            print(f"{self.titulo} ya está prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"{self.titulo} ha sido devuelto.")
        else:
            print(f"{self.titulo} no estaba prestado.")

class Audiolibro(Material, Prestamo):
    def __init__(self, titulo, autor, año, duracion):
        super().__init__(titulo, autor, año)
        self.duracion = duracion
        self.prestado = False

    def mostrar_informacion(self):
        print(f"Audiolibro: {self.titulo}, Narrador: {self.autor}, Año: {self.año}, Duración: {self.duracion} mins")

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"{self.titulo} ha sido prestado.")
        else:
            print(f"{self.titulo} ya está prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"{self.titulo} ha sido devuelto.")
        else:
            print(f"{self.titulo} no estaba prestado.")

def obtener_numero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():  # Verifica si el valor es numérico
            return int(valor)
        else:
            print("Por favor, ingresa un número válido.")

def menu():
    materiales = []
    while True:
        print("\n--- Menú ---")
        print("1. Agregar Libro")
        print("2. Agregar Revista")
        print("3. Agregar DVD")
        print("4. Agregar CD")
        print("5. Agregar Juego")
        print("6. Agregar Audiolibro")
        print("7. Mostrar Información de Materiales")
        print("8. Prestar Material")
        print("9. Devolver Material")
        print("10. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            titulo = input("Ingresa el título del libro: ")
            autor = input("Ingresa el autor del libro: ")
            año = obtener_numero("Ingresa el año del libro: ")
            num_paginas = obtener_numero("Ingresa el número de páginas del libro: ")
            libro = Libro(titulo, autor, año, num_paginas)
            materiales.append(libro)
            print(f"Libro '{titulo}' agregado.")

        elif opcion == '2':
            titulo = input("Ingresa el título de la revista: ")
            autor = input("Ingresa el autor de la revista: ")
            año = obtener_numero("Ingresa el año de la revista: ")
            numero_edicion = obtener_numero("Ingresa el número de edición de la revista: ")
            revista = Revista(titulo, autor, año, numero_edicion)
            materiales.append(revista)
            print(f"Revista '{titulo}' agregada.")

        elif opcion == '3':
            titulo = input("Ingresa el título del DVD: ")
            autor = input("Ingresa el director del DVD: ")
            año = obtener_numero("Ingresa el año del DVD: ")
            duracion = obtener_numero("Ingresa la duración del DVD en minutos: ")
            dvd = DVD(titulo, autor, año, duracion)
            materiales.append(dvd)
            print(f"DVD '{titulo}' agregado.")

        elif opcion == '4':
            titulo = input("Ingresa el título del CD: ")
            autor = input("Ingresa el artista del CD: ")
            año = obtener_numero("Ingresa el año del CD: ")
            duracion = obtener_numero("Ingresa la duración del CD en minutos: ")
            cd = CD(titulo, autor, año, duracion)
            materiales.append(cd)
            print(f"CD '{titulo}' agregado.")

        elif opcion == '5':
            titulo = input("Ingresa el título del juego: ")
            autor = input("Ingresa el desarrollador del juego: ")
            año = obtener_numero("Ingresa el año del juego: ")
            plataforma = input("Ingresa la plataforma del juego: ")
            juego = Juego(titulo, autor, año, plataforma)
            materiales.append(juego)
            print(f"Juego '{titulo}' agregado.")

        elif opcion == '6':
            titulo = input("Ingresa el título del audiolibro: ")
            autor = input("Ingresa el narrador del audiolibro: ")
            año = obtener_numero("Ingresa el año del audiolibro: ")
            duracion = obtener_numero("Ingresa la duración del audiolibro en minutos: ")
            audiolibro = Audiolibro(titulo, autor, año, duracion)
            materiales.append(audiolibro)
            print(f"Audiolibro '{titulo}' agregado.")

        elif opcion == '7':
            if materiales:
                for material in materiales:
                    material.mostrar_informacion()
            else:
                print("No hay materiales en la lista.")

        elif opcion == '8':
            titulo = input("Ingresa el título del material a prestar: ")
            for material in materiales:
                if material.titulo == titulo:
                    if isinstance(material, Prestamo):
                        material.prestar()
                    else:
                        print("El material no se puede prestar.")
                    break
            else:
                print("Material no encontrado.")

        elif opcion == '9':
            titulo = input("Ingresa el título del material a devolver: ")
            for material in materiales:
                if material.titulo == titulo:
                    if isinstance(material, Prestamo):
                        material.devolver()
                    else:
                        print("El material no se puede devolver.")
                    break
            else:
                print("Material no encontrado.")

        elif opcion == '10':
            print("Saliendo...")
            break

        else:
            print("Opción no válida, por favor elige otra.")

if __name__ == "__main__":
    menu()
#este mensaje solo se mostrara en la rama 2#