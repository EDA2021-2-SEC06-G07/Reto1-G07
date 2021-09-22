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


from App.controller import ObrasDepa
from DISClib.DataStructures.arraylist import size
from DISClib.DataStructures.listnode import newSingleNode
import time
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
import datetime
from statistics import mode 
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
    print(struture_type)
    return catalog


# Funciones para agregar informacion al catalogo
def addArtist(catalog, artista):
    lt.addLast(catalog[ARTISTAS], artista)
    

def addArtwork(catalog, artwork):
    #-------------------------------
    lt.addLast(catalog[ARTWORKS], artwork)
    

def listaCronologicaArtistas(catalogo, year1, year2):
    #create linked list
    artistas = lt.newList(datastructure="ARRAY_LIST")
    #look in catalogo for the relevant data
    for i in range(0, lt.size(catalogo) - 1):
        element = lt.getElement(catalogo, i)
        element_date = element['BeginDate']
        if element_date > year1 and element_date < year2:
            lt.addLast(artistas, element)
    
    ms.sort(artistas, cmp_artist_date)
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
    ms.sort(catalog[ARTISTAS], cmp_constituentID)


# Funciones para creacion de datos

    
# Funciones para creacion de datos


# Funciones de consulta
def EncontrarArtista(catalogo, nombreartista):
    print(nombreartista)
    for i in range(1, lt.size(catalogo) + 1):
        element = lt.getElement(catalogo, i)
        if element['DisplayName'] == str(nombreartista):
            id = element['ConstituentID']
            
    return id


# Funciones utilizadas para comparar elementos dentro de una lista

def EncontrarID(catalogo,id):
    obras = lt.newList(datastructure='ARRAY_LIST')
    medios = lt.newList(datastructure='ARRAY_LIST')
    for a in range(1, lt.size(catalogo) + 1):
        element = lt.getElement(catalogo, a)
        
        if str(id) in str(element['ConstituentID']):
            # Se guarda en un diccionario donde la llave es 'elements' y el valor es una lista de tecnicas
            lt.addLast(medios,element['Medium'])
            # Lista de diccionarios de cada obra con datos pedidos
            dicc={}
            dicc['Title']= element['Title']
            dicc['DateAcquired']= element['DateAcquired']
            dicc['Dimensions']= element['Dimensions']
            dicc['Medium']= element['Medium']
            lt.addLast(obras, dicc)
            #La lista obras contiene todos los trabajos del artista
    mas_usada = mode(medios['elements'])

    #insertaremos a una lista los datos pedidos segun metodo mas usado y el autor
    usada = lt.newList(datastructure='ARRAY_LIST')
    for a in range(1, lt.size(obras) + 1):
        element = lt.getElement(obras, a)
        if str(mas_usada) in str(element['Medium']):
            dicc={}
            dicc['Title']= element['Title']
            dicc['DateAcquired']= element['DateAcquired']
            dicc['Dimensions']= element['Dimensions']
            #lt.addLast(obras, dicc)
            dicc['Medium']= mas_usada
            lt.addLast(usada, dicc)

    print("El total de obras del autor son: ", lt.size(obras))
    print('------------------------------------')
    print("La tecnica mas usada es", mas_usada)
    print('------------------------------------')
    print("la lista de la tecnica mas usada es: ")
    return usada


def bin_search_ConstituentID(lista,id):
    element = None
    id = id.replace('[', '')
    id = id.replace(']', '')

    if(id.count(",") != 0):
        id = id.split(", ")[0]
    
    high = lt.size(lista) - 1
    low = 0
    mid = 0

    while low <= high:
        

        mid = (high + low) // 2
        element = lt.getElement(lista, mid)
        
        if element['ConstituentID'] < int(id):
            low = mid + 1
        elif element['ConstituentID'] > int(id):
            high = mid - 1
        else:
            return element

    return element

    
#-----------------------------------------------------------------------------------
# Funciones utilizadas para comparar elementos dentro de una lista
def AgregarFechas(catalogo,año1,mes1,dia1,año2,mes2,dia2):
    FechaFinal = datetime.date(año2,mes2,dia2)
    FechaInicial = datetime.date(año1,mes1,dia1)
    #Se trasformaron los datos en formato de fecha para poder comparar
    obras= lt.newList(datastructure='ARRAY_LIST')
    purchase=lt.newList(datastructure='ARRAY_LIST')
    for a in range(1, lt.size(catalogo) + 1):
        fecha = None
        element = lt.getElement(catalogo, a)
        if  element['DateAcquired'] != None and element['DateAcquired'] != '' :
            fecha= element['DateAcquired'].split('-')
            fecha2 = datetime.date(int(fecha[0]),int(fecha[1]), int(fecha[2]))

            if fecha2 < FechaFinal and fecha2 > FechaInicial:
                dicc={}
                dicc['Title']= element['Title']
                dicc['DateAcquired']= fecha2
                dicc['CreditLine']= element['CreditLine']
                lt.addLast(obras,dicc)
                if 'Purchase' in element['CreditLine'] :
                    lt.addLast(purchase,['Title'])
    print("Las fechas escritas fueron: " ,FechaInicial, "y ", FechaFinal)
    print('Los trabajos encontrados fueron ', lt.size(obras))
    print('La cantiddad de obras en purchase son ' , lt.size(purchase) )
    
    return obras
#-----------------------------------------------------------------------------------
# Funciones utilizadas para comparar elementos dentro de una lista
def InfoDepa(catalogo,Depa):
    Obras= lt.newList(cmpfunction="ARRAY_LIST")
    for a in range(1, lt.size(catalogo) + 1):
        element = lt.getElement(catalogo, a)
        if Depa in element['Department'] :
            Largo = 0
            Ancho = 0
            Alto = 0
            Peso = 0
            countLongitud=0
            countPeso=0 
            Costos= 0
            if element['Width (cm)']!= None and element['Width (cm)']!="":
                Ancho = (float(element['Width (cm)']))/100
            else:
                Ancho = 1
            if element['Height (cm)']!= None and element['Height (cm)']!="":
                Alto = (float(element['Height (cm)']))/100
            else:
                    Alto = 1
            if element['Length (cm)']!= None and element['Length (cm)']!= "":
                        Largo = (float(element['Length (cm)']))/100
            else:
                Largo=1
            countLongitud= 72*(Alto * Ancho * Largo)
            if element['Weight (kg)'] != None and element['Weight (kg)'] != "":
                Peso= float(element['Weight (kg)'])
            else: 
                Peso= 0
            countPeso= 72*(Peso)

            if countPeso > countLongitud:
                costos=countPeso
            else: 
                costos=countLongitud
            dicc={}               
            dicc['Title']= element['Title']
            dicc['Artistas']= element['ConstituentID']
            dicc['Classification']= element['Classification']
            dicc['DateAcquired']=element['DateAcquired']
            dicc['Medio']= element['Medium']
            dicc['Dimensions']= element['Dimensions']
            dicc['Costo']= costos
            lt.addLast(Obras,dicc)

            ms.sort(Obras, cmp_artwork_date_acquired)                                              
    return Obras

# Compares the artworks by date aquired
def cmp_artwork_date_acquired(aw1, aw2):
    #asume they are equal
    result = 0

    date1 = aw1['DateAcquired'].replace("-", "")
    date2 = aw2['DateAcquired'].replace("-", "")

    #check if they are actualy not equal an do the needed change
    if date1 < date2:
        result = -1
    elif date1 > date2:
        result = 1
    
    return result


def cmp_artist_date(artist1, artist2):
    result = 0
    if artist1['BeginDate'] > artist2['BeginDate']:
        result = 1
    elif artist1['BeginDate'] < artist2['BeginDate']:
        result = -1
    return result


def cmp_constituentID(art1, art2):
    result = 0
    if art1['ConstituentID'] < art2['ConstituentID']:
        result = -1
    elif art1['ConstituentID'] > art2['ConstituentID']:
        result = 1
    return result


def cmp_costos(obra1, obra2):
    return obra1['Costo'] - obra2['Costo']
#--------------------------------------------------------------------------------------
# Funciones de ordenamiento

def sort_cost(obras):
    ms.sort(obras, cmp_costos)
    return obras


def sort_artists(artists, size, sort_method):
    sublist = lt.subList(artists, 1, size)
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

def mergeSort(obras):
    ms.sort(obras, cmp_artwork_date_acquired)
    return obras

def get_nationalities(catalog):
    # First we need to sort the catalog in artist to get the ConstituentID
    ms.sort(catalog[ARTISTAS], cmp_constituentID)

    #get the nationalities that exist
    nationalities = {}
    for i in range(0, lt.size(catalog[ARTWORKS])):
        current_element = lt.getElement(catalog[ARTWORKS], i)
        artist = bin_search_ConstituentID(catalog[ARTISTAS], current_element['ConstituentID'])
        nationality = artist['Nationality']

        
        nationality_was_added = False
        for key in nationalities:
            if nationality == key:
                nationality_was_added = True
                lt.addLast(nationalities[key], current_element)
        
        if not nationality_was_added:
            nationalities.update({nationality: lt.newList(datastructure="ARRAY_LIST")})
            lt.addLast(nationalities[nationality], current_element)

    return nationalities

    