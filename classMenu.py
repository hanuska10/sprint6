from classLibro import Libro


class MenuLibros:
    
    def __init__(self):
        self.libro1 = Libro()
        
        
    def mostrarMenu(self):  

        print(30 * "-", "MENU", 30 * "-")
        print("1.Consultar Lista de Libros")
        print("2.Consultar por título")
        print("3.Agregar nuevo libro a la lista ")
        print("4. Exit / Salir")
        print(67 * "-")
    
        menu=True
        while menu:
            #self.mostrarMenu()
            opcion = int(input(" Seleccione una opción [1-3:] "))
            print("\n")
        
            if opcion == 1:
                print(20 * "-", "LISTA LIBROS",20 * "-")
                self.libro1.consultarLista()
                print("\n")
                print(20 * "-")
            elif opcion == 2:
                self.libro1.consultarLibro()
            elif opcion == 3:
                self.libro1.crearGuardar()
            elif opcion == 4:
                menu = False               
            else:
                input("Wrong option selection. Enter any key to try again..")

        print("Fin")


lista = MenuLibros()
lista.mostrarMenu()
