import os

class Libro:
    
    
    def __init__(self):
        self.matriz=[]

    def crearGuardar(self):

        self.titulo = str(input("Escribe el título del libro: ")).upper()
        
        f = open("lista_libros.txt", "r") 
        f=f.read()
        consulta=f.find(self.titulo)
        if consulta < 0:
            self.autor = str(input("Escribe el nombre del autor: ")).capitalize()
            self.fechaEd = str(input("Escribe el año de publicación: ")).capitalize()                
         
            f = open("lista_libros.txt", "a")
            f.write("Título: "+self.titulo + '\n')
            f.write("Autor: " + self.autor + '\n')
            f.write("Fecha edición: "+self.fechaEd + '\n')
            f.write('\n')
        else:
            print("Libro Existe")
            
    def cargarMatriz(self):
        file = open("lista_libros.txt", "r")
        lineas=file.readlines()
        x=0
        while x <= len(lineas):
            fila=lineas[x:x+4]
            self.matriz.append(fila)
            x=x+4

    def consultarLibro(self):
        self.cargarMatriz()
        titulo=str(input("Buscar título: "))
        print()
        if os.path.isfile('C:/Users/formacion/Documents/GitHub/sprint6/lista_libros.txt'):
            for i in range(len(self.matriz)):
                for j in range(len(self.matriz[i])):
                    if self.matriz[i][0].find(titulo)>=0:
                        print(self.matriz[i][j], end="")
        else:
            print('El no archivo existe.')

    def consultarLista(self):
        if os.path.isfile('C:/Users/formacion/Documents/GitHub/sprint6/lista_libros.txt'):
            f = open("lista_libros.txt", "r")
            print(f.read())
        else:
            print('El no archivo existe.')
    
    def eliminarLibro(self):
        self.cargarMatriz()
        titulo = str(input("Buscar título: "))
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][0].find(titulo) >= 0:
                    del self.matriz[i][j]
                    """lista = self.matriz
                    f = open("lista_libros.txt", "a+")
                    for i in lista:
                        f.write(i)
                        f.close()"""
        print(self.matriz)
            
    
#libro1=Libro()
#libro1.cargarMatriz()
#libro1.consultarLibro()
#libro1.eliminarLibro()
