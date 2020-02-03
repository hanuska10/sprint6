from classLibro import Libro


class MenuLibros:
    
    def __init__(self):
        self.libro1 = Biblioteca()

    def mostrarMenu(self):  

        print(30 * "-", "MENU", 30 * "-")
        print("1. Menu consultar 1")
        print("2. Menu agregar 2")
        print("3. Exit")
        print(67 * "-")
    
        menu=True
    
        while menu:
            #self.mostrarMenu()
            opcion = int(input(" Seleccione una opción [1-3:] "))
            print("\n")
           
        
            if opcion == 1:
                print(20 * "-", "LISTA LIBROS",20 * "-")
                self.libro1.consultar()                             
                print("\n")
                print(20 * "-")
            elif opcion == 2:
                self.libro1.crearGuardar()
            elif opcion == 3:
                menu = False
            else:
                input("Wrong option selection. Enter any key to try again..")

        print("Fin")


lista = MenuLibros()
lista.mostrarMenu()
