from classLibro import Libro


class MenuLibros:
    
    def __init__(self):
        self.libro1 = Libro()
    
    def validarNumero(self):
        correcto = False
        opcion = 0
        try:
            opcion = int(input(" Seleccione una opción [1-5:] "))
            corecto=True
        except ValueError:
            print("Oops!  valor no válido. Inténte nuevamente...")
        return opcion       
        
    def mostrarMenu(self):  
    
        salir=False
        opcion=0
        while not salir: 
            print(30 * "-", "MENÚ", 30 * "-")
            print("1.Consultar Lista de Libros")
            print("2.Consultar por título")
            print("3.Agregar nuevo libro a la lista ")            
            print("4.Eliminar un libro a la lista ")
            print("5.Exit / Salir")
            print(67 * "-")
            
            opcion = self.validarNumero()
        
            if opcion == 1:
                print("\n")
                print(20 * "-", "LISTA LIBROS",20 * "-")
                self.libro1.consultarLista()
            elif opcion == 2:
                self.libro1.consultarLibro()
            elif opcion == 3:
                self.libro1.crearGuardar()
            elif opcion == 4:
                self.libro1.eliminarLibro()
            elif opcion == 5:
                salir = True               
            else:
                input("Escribe un número entre 1 & 4...")

        print("Fin")


lista = MenuLibros()
lista.mostrarMenu()
