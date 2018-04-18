class Persona(object):
    nombre = None
    apellido =  None
    fechaNac = None

    def __init__(self, nombre, apellido, fechaNac):
        self.fechaNac = fechaNac
        self.apellido = apellido
        self.nombre = nombre

class Artista(Persona):
    pass

class Autor(Persona):
    nacionalidad = None

    def __init__(self, nombre, apellido, fechaNac, nacionalidad):
        Persona.__init__(nombre, apellido, fechaNac)
        self.nacionalidad = nacionalidad