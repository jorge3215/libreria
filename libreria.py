Libro_1 = []
Libro_2 = []
Libro_3 = []
class registo_cliente:
    def __init__(self, nombre = 0, apellido= 0, edad=0,):
        self._nombre = nombre
        self._apellido = apellido
        self._edad= edad
    def set_nombre(self, nombre):
        self._nombre = nombre
    def get_nombre(self):
        return self._nombre
    def set_apellido(self, apellido):
        self._apellido = apellido
    def get_apellido(self):
        return self._apellido
    def set_edad(self, edad):
        self._edad = edad
    def get_apellido(self):
        return self._edad
    
    
class libros:
    def Menu_de_los_libros(self):
        print("/"*45)
        print("Menu de la libreria de jorgi")
        print("donde estan los mejores libros")
        print("por el momento solo contamos con estos 4 libros")
        print("prontamente abran muchos mas")
        print("/"*45)
        print("1 = 100 años de soledad ")
        print("2 = el principito ")
        print("3 = bajo la misma estrella")
        print("4 = un hombre exitoso")
        print("/"*45)
        elija = int(input("¿que libro desea ojear?: "))
        if elija == 1:
            self.libroNumero1()
        if elija == 2:
            self.libroNumero2()
        if elija == 3:
            self.libro3()
            
        
         
class jorgi(registo_cliente,libros):
    def __init__(self):
        super(jorgi,self).__init__()
        print("/"*45)
        print("bienvenido a la biblioteca de jorgi ")
        print("donde cuentan con variedad de libros")
        print("accion,ficcion y drama")
        print("escoje por favor")
        print("¿en que te podemos ayudar?")
        print("para pedir prestado marque #1 ")
        print("para salir de la biblioteca marque #2")
        print("gracias...")
        print("/"*45)
        seleccion = int(input("por favor digite la opcion deseada "))
        if seleccion == 1:
            libre = registo_cliente()
            libre.set_nombre(input("nombre:  "))
            libre.set_apellido(input("apellido: "))
            libre.set_edad(input("ingrese su edad:"))
            print("/"*45)
            print("1 = 100 años de soledad ")
            print("2 = el principito ")
            print("3 = bajo la misma estrella ")
            print("/"*45)
            seleccion = int(input(("digite el numero del libro a prestar ")))
            if seleccion == 1:
                if 1 in Libro_1:
                    print("/"*45)
                    print("libro no encontrado (ocupado)")
                    self.__init__()
                    print("/"*45)
                else:
                    print("/"*45)
                    print("100 años de soledad")
                    print("Cien años de soledad es una novela del escritor colombiano Gabriel García Márquez, ganador del Premio Nobel de Literatura en 1982. Es considerada una obra maestra de la literatura hispanoamericana y universal, así como una de las obras más traducidas y leídas en español.")
                    print("Autor: Gabriel Garcia Marquez")
                    print("Editorial: flash")
                    print("Idioma: Español")
                    print("ISB:18738197")
                    print("libro prestado correctamente ")
                    print("/"*45)
                    Libro_1.append(1)
                    self.__init__()
            if seleccion == 2:
                if 1 in Libro_2:
                    print("/"*45)
                    print("libro no encontrado (ocupado) ")
                    self.__init__()
                    print("/"*45)
                else:
                    print("Titulo : El principito")
                    print("El principito es una narración corta del escritor francés Antoine de Saint-Exupéry, que trata de la historia de un pequeño príncipe que parte de su asteroide a una travesía por el universo, en la cual descubre la extraña forma en que los adultos ven la vida y comprende el valor del amor y la amistad")
                    print("Autor: Antoine de Saint-Exupéry")
                    print("Idioma: Español")
                    print("ISB:87383719")
                    print("libro prestado correctamente ")
                    Libro_2.append(2)
                    self.__init__()
            if seleccion == 3:
                if 1 in Libro_3:
                    print("libro no encontrado (ocupado)")
                    self.__init__()
                else:
                    print("Titulo : bajo la misma estrella")
                    print("Bajo la misma estrella es una historia sobre el amor y la muerte, narrada en clave de drama y humor, en la que el cáncer aparece como fondo protagonista para alertar sobre la importancia de valorar la vida y disfrutar del presente.")
                    print("Autor: John Green")
                    print("10 de enero")
                    print("Idioma: Español")
                    print("679 Paginas")
                    print("ISB:882738")
                    print("libro prestado correctamente ")
                    Libro_3.append(1)
                    self.__init__()
            
        if seleccion == 4:
            print(" ")
            exit()
Biblioteca = jorgi()