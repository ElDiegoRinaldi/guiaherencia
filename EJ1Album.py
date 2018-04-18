from Ej1Cancion import Cancion

class Album(object):
    titulo = None

    def __init__(self, titulo):
        self.titulo = titulo
        self.listaCanciones = []

    def agregarCancion(self, unaCancion):
        self.listaCanciones.append(unaCancion)

    def MostrarArtistas(self):
        listaDeArtistasDeAlbum = []

        for cancion in self.listaCanciones:
            for artista in cancion.listaArtistas:
                if artista not in self.listaArtistas:
                    listaDeArtistasDeAlbum.append(artista)

        return listaDeArtistasDeAlbum


    def ArtistaMasInfluyente(self):

        listaAuxiliar = []

        for canciones in self.listaCanciones:
            for artista in canciones.listaArtistas:
                listaAuxiliar.append(artista)


        contadorTotal = 0
        artistaMasInfluyente = None

        for item in listaAuxiliar:
            contador = 0
            for item2 in listaAuxiliar:
                if item == item2:
                    contador += 1
            if contador >= contadorTotal:







                contadorTotal = contador
                artistaMasInfluyente = item


        return artistaMasInfluyente

    def CancionesPorNacionalidad(self, nacionalidad):

        listaAutoresNacionalidad = []

        for cancion in self.listaCanciones:
            for autor in cancion.listaAutores:
                if autor.nacionalidad == nacionalidad:
                    listaAutoresNacionalidad.append(autor)

        return listaAutoresNacionalidad
