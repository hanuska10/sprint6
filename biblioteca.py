class Biblioteca:
    titulo=""
    autor=""
    fechaEd=""
    editorial=""


#metodo

     def menu(self):
            resp = True
            print("                           M E N Ú :bookmark_tabs::books:")
            x = input("Si desea consultar, escribe 'c' o si desea agregar, escribe 'a':  ")
                    if x == "c":
                        self.consultar()
                    elif x == "a":
                        self.menuAgregar()
                    else:
                        x = input("Debe escribir 'c' para consullar ú 'a' para agregar:  ")

    def crearGuardar(self):

        print("entro")
        self.titulo = input("introduce titulo ")
        self.autor = input("introduce autor ")
        self.fechaEd = input("introduce fecha de edicion ")
        self.editorial = input("introduce editorial ")

        f = open("mifish.txt", "a")
        f.write(self.titulo + '\n' )
        f.write(self.autor + '\n' )
        f.write(self.fechaEd + '\n' )
        f.write(self.editorial + '\n' + '\n')

    def menuAgregar(self):
        resp = True
        x = input("¿Desea agregar otro libro? Escribe si o no: ")
        while(resp):
            if x == "si":
                self.crearGuardar()
            elif x == "no":
                resp = False
                self.menu()
            else:
                x = input("¿Desea agregar otro libro? Escribe si o no: ")

    def consultar(self):

        f = open("mifish.txt", "r")
        for x in f:
            print(x)


#objeto

libro1= Biblioteca()
#libro1.crearGuardar()
#libro1.consultar()
libro1.menu()