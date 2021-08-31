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


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos
def loadData(catalog):
    loadConstituentID(catalog)
    loadDisplayName(catalog)
    loadArtistBio(catalog)
    loadNationality(catalog)
    loadGender(catalog)
    

def loadConstituentID(catalog):
    ConstituentIDfile = cf.data_dir + 'Artist-utf8-small.csv'
    input_file = csv.DictReader(open(ConstituentIDfile, encoding='utf-8'))
    i = 0
    for ConstituentID in input_file:
        model.addBook(catalog, ConstituentID)

def loadDisplayName(catalog):
    DisplayNamefile = cf.data_dir + 'Artist-utf8-small.csv'
    input_file = csv.DictReader(open(DisplayNamefile, encoding='utf-8'))
    i = 0
    for DisplayName in input_file:
        model.addBook(catalog, DisplayName)
def loadArtistBio(catalog):
    ArtistBiofile = cf.data_dir + 'Artist-utf8-small.csv'
    input_file = csv.DictReader(open(ArtistBiofile, encoding='utf-8'))
    i = 0
    for ArtistBio in input_file:
        model.addBook(catalog, ArtistBio)
def loadNationality(catalog):
    Nationalityfile = cf.data_dir + 'Artist-utf8-small.csv'
    input_file = csv.DictReader(open(Nationalityfile, encoding='utf-8'))
    i = 0
    for Nationality in input_file:
        model.addBook(catalog, Nationality)

def loadGender(catalog):
    Genderfile = cf.data_dir + 'Artist-utf8-small.csv'
    input_file = csv.DictReader(open(Genderfile, encoding='utf-8'))
    i = 0
    for Gender in input_file:
        model.addBook(catalog, Gender)

def loadBeginDate(catalog):
    BeginDatefile = cf.data_dir + 'Artist-utf8-small.csv'
    input_file = csv.DictReader(open(BeginDatefile, encoding='utf-8'))
    i = 0
    for BeginDate in input_file:
        model.addBook(catalog, BeginDate)

def loadEndDate(catalog):
    EndDatefile = cf.data_dir + 'Artist-utf8-small.csv'
    input_file = csv.DictReader(open(EndDatefile, encoding='utf-8'))
    i = 0
    for EndDate in input_file:
        model.addBook(catalog, EndDate)
def loadWikiQID(catalog):
    WikiQID = cf.data_dir + 'Artist-utf8-small.csv'
    input_file = csv.DictReader(open(WikiQID, encoding='utf-8'))
    i = 0
    for EndDate in input_file:
        model.addBook(catalog, WikiQID)
def loadULAN(catalog):
    ULAN = cf.data_dir + 'Artist-utf8-small.csv'
    input_file = csv.DictReader(open(ULAN, encoding='utf-8'))
    i = 0
    for ULAN in input_file:
        model.addBook(catalog, ULAN)
    
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
