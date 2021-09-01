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

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


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
    6- Proponer nueva expocicion en el museo B"""
    print(menu)


catalog = None


def loadCatalog():
    catalog = controller.initCatalog()
    controller.loadData(catalog)
    return catalog

"""
Menu principal
"""
if __name__ == "__main__":
    running = True
    while running:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 0:
            print("Cargando información de los archivos ....")
            
            catalog = loadCatalog()

            if catalog != None:
                print("Carga de datos exitoso")
                print('Artistas cargados:' + str(lt.size(catalog['Artistas'])))

            else:
                print("algo salio mal")

        elif int(inputs[0]) == 1:
            pass
        elif int(inputs[0]) == 2:
            pass
        elif int(inputs[0]) == 3:
            pass
        elif int(inputs[0]) == 4:
            pass
        elif int(inputs[0]) == 5:
            pass
        elif int(inputs[0]) == 6:
            pass
        else:
            running = False
