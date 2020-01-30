from biblioteca 

def menu(self):
        #resp = True
        print("                           M E N Ú :bookmark_tabs::books:")
        x = input("Si desea consultar, escribe 'c' o si desea agregar, escribe 'a':  ")
        if x == "c":
            self.consultar()
        elif x == "a":
            self.menuAgregar()
        else:
            x = input("Debe escribir 'c' para consullar ú 'a' para agregar:  ")