import os


class Libro:

    #metodo
    def crearGuardar(self):

        self.titulo = str(input("Escribe el título del libro: ")).upper()
        
        f = open("lista_libros.txt", "r") 
        f=f.read()
        consulta=f.find(self.titulo)
        if consulta < 0:
            self.autor = str(input("Escribe el nombre del autor: "))
            self.fechaEd = str(input("Escribe el año de publicación: "))
            self.editorial = str(input("Escribe el nombre de la editoria: "))                  
         
            f = open("lista_libros.txt", "a")
            f.write("Título: "+self.titulo + '\n')
            f.write("Autor: " + self.autor + '\n')
            f.write("Fecha edición: "+self.fechaEd + '\n')
            f.write("Editorial: "+self.editorial + '\n')
        else:
            print("Libro Existe")

    def consultar(self):
        if os.path.isfile('C:/Users/formacion/Documents/GitHub/sprint6/lista_libros.txt'):
            f = open("lista_libros.txt", "r")  # lee el archivo si existe
            for x in f:
                print(x)
        else:
            print('El no archivo existe.')
