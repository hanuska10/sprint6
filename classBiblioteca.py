import os


class Biblioteca:
    
    def __init__(self):
        self.listaLibros=[]

    #metodo
    def agregar(self):
        libro1 = Libro()

        lista=[self.titulo,self.autor,self.fechaEd,self.editorial]
        self.listaLibros.append(lista)

        
        
    
    def validarLibro(self):

        self.titulo = self.libro.titulo
        
        self.autor = str(input("Escribe el nombre del autor: "))
        self.fechaEd = str(input("Escribe el año de publicación: "))
        self.editorial = str(input("Escribe el nombre de la editoria: "))
        
        f = open("lista_libros.txt", "a" )    
        f.write("Título: "+self.titulo +'\n')
        f.write("Autor: "+ self.autor + '\n')
        f.write("Fecha edición: "+self.fechaEd + '\n')
        f.write("Editorial: "+self.editorial + '\n')
        f.write((20 * "-") + '\n')

    def consultar(self):
        if os.path.isfile('C:/Users/formacion/Documents/GitHub/sprint6/lista_libros.txt'):            
            f = open("lista_libros.txt", "r")  # lee el archivo si existe
            for x in f:
                print(x)
        else:
            print('El no archivo existe.')

