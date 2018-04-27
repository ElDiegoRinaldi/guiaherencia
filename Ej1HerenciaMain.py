from Discografica import Discografica
from EJ1Album import Album
from Ej1Cancion import Cancion
from Ej1Persona import Artista
from Ej1Persona import Autor
import datetime

laDiscografica = Discografica('PinaRecords')

elAlbum = Album('PopurriNachones')

elArtista = Artista('Mariano', 'Lerner', datetime.date(2000, 1, 3))
elArtista2 = Artista('Roberto', 'Lerne', datetime.date(1999, 9, 1))
elArtista3 = Artista('Ricardo', 'Lern', datetime.date(1999, 8, 2))

laCancion = Cancion('Grasa')
laCancion.agregarArtista(elArtista)
laCancion.agregarArtista(elArtista2)
laCancion.agregarArtista(elArtista3)

elAutor = Autor('Duki','Duk',datetime.date(2000,1,1), 'jamaikano')
laCancion.agregarAutor(elAutor)
elAlbum.agregarCancion(laCancion)

laCancion = Cancion('EnGrasados')
laCancion.agregarArtista(elArtista)
laCancion.agregarArtista(elArtista2)

elAutor = Autor('Rodrigo','Rodri',datetime.date(2010,11,11), 'jamaikano')
laCancion.agregarAutor(elAutor)
elAlbum.agregarCancion(laCancion)



laCancion = Cancion('Bidonazo')
laCancion.agregarArtista(elArtista)

elAutor = Autor('Manuel','Richar',datetime.date(2001,3,13), 'jamaIkano')
laCancion.agregarAutor(elAutor)
elAlbum.agregarCancion(laCancion)

laDiscografica.agregarAlbum(elAlbum)

print(elAlbum.MostrarArtistas())
print(laDiscografica.ArtistaMasInfluyente(elAlbum))
print(elAlbum.AutoresPorNacionalidad('jamaikano'))