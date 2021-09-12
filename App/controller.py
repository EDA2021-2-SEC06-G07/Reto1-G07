"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import model
import csv


#constantes
#--------------------------
#file names
ARTISTS_FILE = 'MoMa/Artists-utf8-large.csv'
ARTWORKS_FILE = 'MoMa/Artworks-utf8-large.csv'

#Dicionario
ARTISTAS = 'Artistas'
ARTWORKS = 'Artworks'




"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog(struture_type):
    catalog = model.newCatalog(struture_type)
    return catalog


def loadCatalog():
    pass

# Funciones para la carga de datos
def loadData(catalog):
     loadArtist(catalog)
     loadArtworks(catalog)
    

def loadArtist(catalog):
    artistsfile = cf.data_dir + ARTISTS_FILE
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    i = 0
    for artist in input_file:
        artist['BeginDate'] = int(artist['BeginDate'])
        artist['ConstituentID'] = int(artist['ConstituentID'])
        model.addArtist(catalog, artist)


def loadArtworks(catalog):
    artworksfile = cf.data_dir + ARTWORKS_FILE
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    i = 0
    for artwork in input_file:
        model.addArtwork(catalog, artwork)

def listaCronologicaArtistas(catalogo, year1, year2):
    return model.listaCronologicaArtistas(catalogo, year1, year2)


def get_nationalities(catalog, size):
    return model.get_nationalities(catalog)

    
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
