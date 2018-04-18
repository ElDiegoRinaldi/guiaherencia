from EJ1Album import Album

class Discografica(object):
    nombre = None

    def __init__(self, nombre):
        self.nombre = nombre

        self.listaAlbums = []

    def agregarAlbum(self, unAlbum):
        for item in self.listaAlbums:
            if item == unAlbum:
                return False

        self.listaAlbums.append(unAlbum)
