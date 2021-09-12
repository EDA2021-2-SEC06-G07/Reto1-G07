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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.listnode import newSingleNode
import time
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
from datetime import date
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
#Constantes
#-------------
#Dicionario
ARTISTAS = 'Artistas'
ARTWORKS = 'Artworks'


# Construccion de modelos
def newCatalog(struture_type):
    catalog = {
        ARTISTAS: None,
        ARTWORKS: None
    }

    catalog[ARTISTAS] = lt.newList(datastructure=struture_type)
    catalog[ARTWORKS] = lt.newList(datastructure=struture_type)
    return catalog


# Funciones para agregar informacion al catalogo
def addArtist(catalog, artista):
    lt.addLast(catalog[ARTISTAS], artista)
    

def addArtwork(catalog, artwork):
    lt.addLast(catalog[ARTWORKS], artwork)
    

def listaCronologicaArtistas(catalogo, year1, year2):
    #create linked list
    artistas = lt.newList(datastructure="ARRAY_LIST")
    #look in catalogo for the relevant data
    for i in range(0, lt.size(catalogo) - 1):
        element = lt.getElement(catalogo, i)
        element_date = element['BeginDate']
        if element_date > year1 and element_date < year2:
            add_element(artistas, element)
    return artistas


def listaobras(catalogo, date1, date2):
    
    obras = lt.newList(datastructure="ARRAY_LIST")
    
    for i in range(0, lt.size(catalogo) - 1):
        element = lt.getElement(catalogo, i)
        element_dates = element['DateAcquired']
        if element_dates > date1 and element_dates < date2:
            lt.add_element(obras, element)
    return obras


def get_nationalities(catalog):
    # First we need to sort the catalog in artist to get the ConstituentID
    insertion(catalog[ARTISTAS], 0, lt.size(catalog[ARTISTAS]) - 1, 'ConstituentID')


# size is the size of the new sublist
def sublista(list, size):
    if(size > lt.size(list)):
        print("size bigger than the amount of data")
        return list
    return lt.subList(list, 0, size - 1)
# Funciones para creacion de datos

    


    
# Funciones para creacion de datos

# Funciones de consulta
def EncontrarArtista(catalogo, nombreartista):
    
    for i in range(0, lt.size(catalogo) - 1):
        element = lt.getElement(catalogo, i)
        if element['DisplayName'] == str(nombreartista):
            id = element['ConstituentID']
            
    return id
# Funciones utilizadas para comparar elementos dentro de una lista
def EncontrarID(catalogo,id):
    ida = ''
    for a in range(0, lt.size(catalogo) - 1):
        element = lt.getElement(catalogo, a)
        #obras = lt.newList(datastructure='ARRAY_LIST')
        if str(id) in str(element['ConstituentID']):
            dicc={}
            dicc['Title']= element['Title']
            dicc['DateAcquired']= element['DateAcquired']
            dicc['Medium']= element['Medium']
            dicc['Dimensions']= element['Dimensions']
            #lt.addLast(obras, dicc)
            print(dicc)

    return None
#-----------------------------------------------------------------------------------
# Funciones utilizadas para comparar elementos dentro de una lista

# Compares the artworks by date aquired
def cmp_artwork_date_acquired(aw1, aw2):
    #asume they are equal
    result = 0

    date1 = int(aw1['DateAcquired'].replace("-", ""))
    date2 = int(aw2['DateAcquired'].replace("-", ""))
    #check if they are actualy not equal an do the needed change
    if date1 < date2:
        result = -1
    elif date1 > date2:
        result = 1
    
    return result

#--------------------------------------------------------------------------------------
# Funciones de ordenamiento

def sort_artists(catalog, size, sort_method):
    sublist = sublista(catalog, size)
    sublist = sublist.copy()

    start_time = time.process_time()

    if sort_method == 1:
        ins.sort(sublist, cmp_artwork_date_acquired)
    elif sort_method == 2:
        ss.sort(sublist, cmp_artwork_date_acquired)
    elif sort_method == 3:
        qs.sort(sublist, cmp_artwork_date_acquired)
    else:
        ms.sort(sublist, cmp_artwork_date_acquired)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg


def add_element(artistas, element):
    
    size = lt.size(artistas)
    element_date = element['BeginDate']
    #si no hay elementos, agreguelo
    if size == 0:
        lt.addLast(artistas, element)
    #si solo hay un elemento
    elif size == 1:
        if lt.firstElement(artistas)['BeginDate'] < element_date:
            lt.addLast(artistas, element)
        else: 
            lt.addFirst(artistas, element)
    #si el elemento se tiene que agregar al principio
    elif lt.firstElement(artistas)['BeginDate'] > element_date:
        lt.addFirst(artistas, element)
    elif lt.lastElement(artistas)['BeginDate'] < element_date:
        lt.addLast(artistas, element)
    else:
        top_boundary = size -1
        buttom_boundary = 0
        pos = int(top_boundary / 2) + 1
        pos_found = False

        #binary search to find the position of the element
        while not pos_found:
            #print('pos:'+str(pos))
            current_date  = lt.getElement(artistas, pos)['BeginDate']
            prev_date = lt.getElement(artistas, pos-1)['BeginDate']
            element_date = element['BeginDate']
            #current position is the position we are looking for
            if prev_date <= element_date and element_date <= current_date:
                pos_found = True
            #position is to large
            elif prev_date > element_date:
                top_boundary = pos
                pos -= int((top_boundary - buttom_boundary) / 2)
            #position is to small
            elif current_date < element_date:
                buttom_boundary = pos
                pos += int((top_boundary - buttom_boundary) / 2) + 1

        #after you found the position the element will be in, add it to that position
        lt.insertElement(artistas, element, pos)



# implementing timsort 
# this implementation was done by following the video series of Gaurav Sen on Tim sort
# link: https://www.youtube.com/watch?v=emeME__917E&list=PLMCXHnjXnTntLcLmA5SqhMspm7burHi3m


# as said in part 1 and 2 we need to start by implementing insertion.
# this is because in the sortin algorithms of order O(n²) this is the fastest with a very low constant
# insertion sort is the most eficient algotithm in arrays of small sizes. (32 - 64)


# insertion() orders the elements between start and end
def insertion(list, start, end, id):
    #i is the element we are going to insert
    i = start + 1
    while i >= end :
        j = i - 1
        element = lt.getElement(list, i)
        while element[id] < (lt.getElement(list, j)[id]):
            lt.exchange(list, j, j + 1)
            j -= 1
        i += 1


# more eficient than insertion because it the search por the position is O(logn)
# but the algorithm itself is still O(n²)
def binary_insertion(list, start, end, id):
    i = start + 1
    while i >= end :
        j = i - 1
        element = lt.getElement(list, i)
        while element[id] < (lt.getElement(list, j)[id]):
            lt.exchange(list, j, j + 1)
            j -= 1
        i += 1
