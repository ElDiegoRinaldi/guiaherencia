from Ej1Persona import Artista
from Ej1Persona import Autor

class Cancion(object):
    titulo = None

    def __init__(self, titulo):
        self.titulo = titulo

        self.listaArtistas = []
        self.listaAutores = []

    def agregarArtista(self, unArtista):
        for item in self.listaArtistas: #Cheque si el artista ya esta en la cancion
            if item == unArtista:
                return False

        self.listaArtistas.append(unArtista)

    def agregarAutor(self, unAutor):
        for item in self.listaAutores: #Cheque si el autor ya esta en la cancion
            if item == unAutor:
                return False

        self.listaAutores.append(unAutor)



