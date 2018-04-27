class vehiculo (object):
    patente = None
    cant_ruedas = None
    fabricacion = None

    def __init__ (self, petente, ruedas, fabricacion):
        self.petente = petente
        self.cant_ruedas = ruedas
        self.fabricacion = fabricacion
