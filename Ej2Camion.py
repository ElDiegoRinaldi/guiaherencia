from Ej2Vehiculos import vehiculo

class camion (vehiculo):
    capacidad = None

    def __init__(self, petente, ruedas, fabricacion,capacidad):
        vehiculo.__init__(self,petente, ruedas, fabricacion)
        self.capacidad = capacidad