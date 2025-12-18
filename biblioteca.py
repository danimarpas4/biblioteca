'''SISTEMA DE GESTION DE BIBLIOTECA 
Creamos un sistema de gestión de una biblioteca utilizando clases en Python. 
Implementamoss las siguientes clases:
1. “Libro”: representa un libro con atributos como título, autor y número de 
ejemplares disponibles.
2. “Usuario”: Representa a un usuario de la biblioteca con atributos como 
nombre, número de identificación y lista de libros prestados.
3. “Biblioteca”: Representa la biblioteca en sí, con métodos para agregar 
libros, prestar libros a usuarios, devolver libros y mostrar el inventario.'''


class Libro:
    def __init__(self, titulo, autor, ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares


class Usuario:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
        self.lista = []
        

class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libros(self, libro):
        self.libros.append(libro)
    
    def prestar_libros(self, usuario, titulo):
        encontrado = False # Bandera para saber si encontramos el libro
        
        for libro in self.libros:
            # Comparamos titulos (usamos .lower() para ignorar mayúsculas/minúsculas)
            if libro.titulo.lower() == titulo.lower():
                encontrado = True
                if libro.ejemplares > 0:
                    usuario.lista.append(libro)
                    libro.ejemplares -= 1
                    print(f"✅ Éxito: Libro '{libro.titulo}' prestado a {usuario.nombre}. Quedan {libro.ejemplares}.")
                    return # Salimos de la función, ya terminamos
                else:
                    print(f"❌ Error: El libro '{titulo}' no tiene ejemplares disponibles.")
                    return # Salimos de la función
        
        # Si el bucle termina y no entramos al return de arriba:
        if not encontrado:
            print(f"🔍 Info: El libro '{titulo}' no existe en la biblioteca.")
    
    def devolver_libro(self, usuario, titulo):
        for libro in usuario.lista:
            # Buscamos en la lista del USUARIO, no en la biblioteca general
            if libro.titulo.lower() == titulo.lower():
                usuario.lista.remove(libro) # Quitamos el libro al usuario
                libro.ejemplares += 1       # Aumentamos el stock en la biblioteca
                print(f" ️Devolución exitosa: {usuario.nombre} devolvió '{titulo}'. Stock actual: {libro.ejemplares}.")
                return # Terminamos la función
        
        # Si termina el bucle y no retornó, es que el usuario no tenía ese libro
        print(f"⚠️ Error: {usuario.nombre} no tiene el libro '{titulo}' en su poder.")
        
    def mostrar_inventario(self):
        cantidad = len(self.libros)
        print(f"Tienes {cantidad} libros:")
        for libro in self.libros:
            print(f"-{libro.titulo}, creado por {libro.autor}. Cantidad: {libro.ejemplares}.")  
    
biblioteca = Biblioteca()   
libro1 = Libro("El brillo de las luciernagas", "Natalia García", 13)
libro2 = Libro("El Gran Gatsby", "F. Scott Fitzgerald", 3)
biblioteca.agregar_libros(libro1)
biblioteca.agregar_libros(libro2)

usuario1 = Usuario("Nati", "2231")
usuario2 = Usuario("Carmen", "2651")

biblioteca.prestar_libros(usuario1, "El Gran Gatsby")
biblioteca.prestar_libros(usuario2, "El brillo de las luciernagas")

biblioteca.mostrar_inventario()

biblioteca.devolver_libro(usuario1, "El Gran Gatsby")

biblioteca.mostrar_inventario()

