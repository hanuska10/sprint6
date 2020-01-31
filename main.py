from biblioteca import Biblioteca


class MenuLibros:

    def init(self):
        self.libro1 = Biblioteca()

    def mostrarMenu(self):

        print(30 * "-", "MENU", 30 * "-")
        print("1. Menu Option 1")
        print("2. Menu Option 2")
        print("3. Exit")
        print(67 * "-")

        menu=True

        while menu:
            #self.mostrarMenu()
            opcion = int(input(" Seleccione una opción [1-3:] "))

            if opcion == 1:
                self.libro1.consultar()
            elif opcion == 2:
                self.libro1.crearGuardar()
            elif opcion == 3:
                menu = False
            else:
                input("Wrong option selection. Enter any key to try again..")

        print("Fin")


lista = MenuLibros()
lista.mostrarMenu()