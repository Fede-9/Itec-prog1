class Empleado():
   
    def setDatosBasicos(self,nombre,sueldo): #asigna nombre y sueldo
        self.nombre = nombre
        self.sueldo = sueldo
    
    def getDatos(self):
        return self.nombre, self.sueldo

class Programador(Empleado):
    
    def __init__(self,lenguaje):
        self.lenguaje = lenguaje
    
    def setProyecto(self,proyecto):
        self.proyecto = proyecto
        
    def getProyecto(self):
        return self.proyecto, self.lenguaje
    

class Empresa():
    listaProyectos = ["Web Empresa Pollitos SA", "Sistema Empresa Gallina SRL"]
    listaLenguajes = ["Python", "JavaScript", "C#", "HTML&CSS"]
    listaProgramadores = []

    def __init__(self, nombre, rubro):
        self.nombre = nombre
        self.rubro = rubro

    def getEmpresa(self):
        return self.nombre, self.rubro

    def agEmp(self):
        leng = input("Que lenguaje maneja el candidato: ")
        prog = 0
        if leng in self.listaLenguajes:
            prog = Programador(leng)
            n = input("Nombre: ")
            if leng == "Python":
                s = 175000
            else:
                s = 115000
            prog.setDatosBasicos(n, s)
            for elemento in self.listaProyectos:
                print (elemento)
            np = int(input("Seleccione un proyecto (1 0 2): "))
            prog.setProyecto(self.listaProyectos[int(np)-1])
            self.listaProgramadores.append(prog)
        else:
            print ("No se requiere personal para ese lenguaje")
            print ("Los lenguajes requeridos son:", self.listaLenguajes)

    
    def mostrarTodo(self):
        print(self.getEmpresa())
        for pr in self.listaProgramadores:
            print(pr.getDatos(), pr.getProyecto())



empresa = Empresa("PabloKaniefsky", "Desarrollo de Software")
for x in range(3):
    empresa.agEmp()
empresa.mostrarTodo()