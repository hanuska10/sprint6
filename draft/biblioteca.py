import os
class Biblioteca:

    #metodo
    def crearGuardar(self):

        self.titulo = str(input("Escribe el título del libro: "))
        self.autor = str(input("Escribe el nombre del autor: "))
        self.fechaEd = str(input("Escribe el año de publicación: "))
        self.editorial = str(input("Escribe el nombre de la editoria: "))

        f = open("lista_libros.txt", "a")
        f.write(self.titulo + '\n')
        f.write(self.autor + '\n')
        f.write(self.fechaEd + '\n')
        f.write(self.editorial + '\n' + '\n')

    def consultar(self):

        prueba = os.path.isfile('C:/Users/formacion/Documents/GitHub/sprint6/lista_libros.txt')
        print(prueba)
        if os.path.isfile('C:/Users/formacion/Documents/GitHub/sprint6/lista_libros.txt'):
            print("existe")
            f = open("lista_libros.txt", "r")  # lee el archivo si existe
            for x in f:
                print(x)
        else:
            print('El no archivo existe.')