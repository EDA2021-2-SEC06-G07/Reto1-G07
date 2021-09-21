"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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



from io import DEFAULT_BUFFER_SIZE
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
#import pandas as pd
assert cf

#Dicionario
ARTISTAS = 'Artistas'
ARTWORKS = 'Artworks'


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    menu = """Bienvenido.
    0- Cargar ingormacion en el catalogo
    1- Lista Cronologica de artistas
    2- Lista cronologica adquisicion
    3- Lista de obras de un artista por tecnica
    4- Lista de obras por nacionalidad de creadores
    5- Transportar obras de un departamento
    6- Proponer nueva expocicion en el museo B
    7- Sort catalog by method indicated
    9- To exit"""
    print(menu)


catalog = None


def loadCatalog(struture_type):
    catalog = controller.initCatalog(struture_type)
    controller.loadData(catalog)
    return catalog


def listaCronologicaArtistas(year1, year2):
    artistas = controller.listaCronologicaArtistas(catalog[ARTISTAS], year1, year2)
    size = lt.size(artistas)
    result = "Numero de artistas entre " + str(year1) + " y " + str(year2) + ":" + str(size) + "\n"
    
    out = [
        lt.getElement(artistas, 0), 
        lt.getElement(artistas, 1), 
        lt.getElement(artistas, 2), 
        lt.getElement(artistas, size - 3), 
        lt.getElement(artistas, size - 2), 
        lt.getElement(artistas, size - 1)
    ]
    for artist in out:
        name = artist['DisplayName']
        birth = artist['BeginDate']
        death = artist['EndDate']
        nationality = artist['Nationality']
        gender = artist['Gender']

        result += """Name:{}, 
        Birth:{}, 
        death:{}, 
        nationality:{}, 
        gender:{}
""".format(name, birth, death, nationality, gender)
    return result


def  get_nationalities():
    return controller.get_nationalities(catalog)

"""
Menu principal
"""
if __name__ == "__main__":
    running = True
    while running:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 0:
            print("Como quieres guardar los datos? ")
            struture_type = input("Pon 1 para ArrayList, 2 para LinkedList: ")
            if struture_type == 2:
                struture_type = 'SINGLE_LINKED'
            else:
                struture_type = 'ARRAY_LIST'
            print("Cargando información de los archivos ....")
            
            catalog = loadCatalog(struture_type)

            if catalog != None:
                print("Carga de datos exitoso")
                print('Artistas cargados:' + str(lt.size(catalog[ARTISTAS])))
                print("artworks cargados: " + str(lt.size(catalog[ARTWORKS])))
                
            else:
                print("algo salio mal")

        elif int(inputs[0]) == 1:
            year1 = int(input('Año inicial:'))
            year2 = int(input('Año final:'))
            print(listaCronologicaArtistas(year1, year2))
        elif int(inputs[0]) == 2:
            año1 = int(input("Gregue el año de la fecha 1: "))
            mes1 = int(input("Gregue el año de la fecha 1: "))
            dia1 = int(input("Gregue el año de la fecha 1: "))
            año2 = int(input("Gregue el año de la fecha 2: "))
            mes2 = int(input("Gregue el año de la fecha 2: "))
            dia2 = int(input("Gregue el año de la fecha 2: "))
            print(controller.FechasObras(catalog[ARTWORKS],año1,mes1,dia1,año2,mes2,dia2))
            
    
            pass


        elif int(inputs[0]) == 3:
            nombreartista = input("Coloque el artista: ")
            print("El ID del artista es")
            print(controller.ArtistaEncontrado( catalog[ARTISTAS], nombreartista))
            print(controller.IDencontrado( controller.ArtistaEncontrado( catalog[ARTISTAS], nombreartista)))
            
            pass
        elif int(inputs[0]) == 4:
            nacionalidades = get_nationalities()
            print('nacionalidades:')
            
        elif int(inputs[0]) == 5:
            Depa=str(input('Dijite el departamento por favor: '))
            print(controller.ObrasDepa(catalog[ARTWORKS],Depa))
            pass
        elif int(inputs[0]) == 6:
            pass
        elif int(inputs[0]) == 7:
            size = int(input("what is the size of the sort?"))
            print("What sorting method do you want?")
            sort_method = int(input("1: incertion, 2: shell, 3: quick, 4: merge: "))

            result = controller.sort_artists(catalog, size, sort_method)
            print("la muestra de " + size + " elementos se demoro: " + result + "ms.")
        else:
            running = False
