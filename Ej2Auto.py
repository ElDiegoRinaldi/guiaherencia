from Ej2Vehiculos import vehiculo

class auto (vehiculo):
    descapotable = None

    def __init__ (self, petente, ruedas, fabricacion, descapotable):
        vehiculo.__init__(self, petente, ruedas, fabricacion)
        self.descapotable = descapotable