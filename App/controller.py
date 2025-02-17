﻿"""
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
ARTISTS_FILE = 'MoMa/Artists-utf8-small.csv'
ARTWORKS_FILE = 'MoMa/Artworks-utf8-small.csv'

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


def listaobras(catalogo, date1, date2):
    return model.listaobras(catalogo,date1,date2)


def get_nationalities(catalog):
    return model.get_nationalities(catalog)

    
# Funciones de ordenamiento
def sort_artists(atrisits, size, sort_method):
    return model.sort_artists(atrisits, size, sort_method)


def ArtistaEncontrado(catalogo, nombreartista):
    return model.EncontrarArtista(catalogo, nombreartista)


def IDencontrado(catalogo, id):
    return model.EncontrarID(catalogo, id)


def get_artist(list, id):
    return model.bin_search_ConstituentID(list, id)


def FechasObras(catalogo,año1,mes1,dia1,año2,mes2,dia2):
    return model.AgregarFechas(catalogo,año1,mes1,dia1,año2,mes2,dia2)


def ObrasDepa(catalogo,Depa):
    return model.InfoDepa(catalogo,Depa)


def sort_cost(obras):
    return model.sort_cost(obras)
