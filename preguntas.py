"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


import csv

with open("data.csv",newline='')as f:
  datos = csv.reader(f, delimiter='\t')
  colums = list(datos)


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma=0
    for var in colums:
      suma+=int(var[1])
      
    return suma


def pregunta_02():
    """
        2Retorne la cantidad de registros por cada letra de la primera columna como la lista
        de tuplas (letra, cantidad), ordendas alfabéticamente.
        Rta/
        [
            ("A", 8),
            ("B", 7),
            ("C", 5),
            ("D", 6),
            ("E", 14),
        ]
    """

    dic = {}
    for letter in colums:
        if letter[0] in dic.keys():
            dic[letter[0]] = dic[letter[0]] +1 
        else:
            dic[letter[0]] = 1

    tupla = list(zip(dic.keys(), dic.values()))
    tupla.sort()

    return tupla


def pregunta_03():
    """
        3Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
        de tuplas (letra, suma) ordendas alfabeticamente.
        Rta/
        [
            ("A", 53),
            ("B", 36),
            ("C", 27),
            ("D", 31),
            ("E", 67),
        ]
    """
    
    dic1 = {}

    for sum1 in colums:
      if sum1[0] in dic1.keys():
        dic1[sum1[0]] = dic1[sum1[0]] + int(sum1[1])
      else:
        dic1[sum1[0]] = int(sum1[1])
      
    tupla1 = list(zip(dic1.keys(), dic1.values()))
    tupla1.sort()
    
    return tupla1


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.
    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
    """
    x = [i[2].split('-') for i in colums]

    dic2 = {}

    for month in x:
        if month[1] in dic2.keys():
            dic2[month[1]] = dic2[month[1]] +1 
        else:
            dic2[month[1]] = 1

    tupla2 = list(zip(dic2.keys(), dic2.values()))
    tupla2.sort()
    
    return tupla2


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    dic3 = {}

    for letter1 in colums:
      letter1[1] = int(letter1[1])
      if letter1[0] in dic3.keys():
        dic3[letter1[0]].append(letter1[1])
      else:
        dic3[letter1[0]] = [letter1[1]]

    dic3 = [(key, max(valor), min(valor)) for key, valor in dic3.items()]
    dic3.sort()
    
    return dic3


def pregunta_06():
    """
        6La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
        una clave y el valor despues del caracter `:` corresponde al valor asociado a la
        clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
        grande computados sobre todo el archivo.
        Rta/
        [
            ("aaa", 1, 9),
            ("bbb", 1, 9),
            ("ccc", 1, 10),
            ("ddd", 0, 9),
            ("eee", 1, 7),
            ("fff", 0, 9),
            ("ggg", 3, 10),
            ("hhh", 0, 9),
            ("iii", 0, 9),
            ("jjj", 5, 17),
        ]

    """
    data = [row[4].split(',') for row in colums]
    data = [item for sublist in data for item in sublist]

    dic7 = {}

    for letter7 in data:

      codigo = letter7.split(':')[0]
      numero = int(letter7.split(':')[1])

      if codigo in dic7.keys():
        dic7[codigo].append(numero)

      else:
        dic7[codigo] = [numero]

    dic7 = [(key, min(valor), max(valor)) for key, valor in dic7.items()]
    dic7.sort()

    return dic7

  
def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.
    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]
    """

    dic4 = {}
    for num2 in colums:
      if num2[1] in dic4.keys():
        dic4[num2[1]].append(num2[0])
      else:
        dic4[num2[1]] = [num2[0]]

    tupla3 = list(zip(dic4.keys(), dic4.values()))
    tupla3.sort()
    
    return tupla3


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]
    """

    dic9 = {}

    for num3 in colums:
      if num3[1] in dic9.keys():

        if num3[0] not in dic9[num3[1]]:
          dic9[num3[1]].append(num3[0])
          
      else:
        dic9[num3[1]] = [num3[0]]

    tupla4 = [(key, sorted(valor)) for key, valor in dic9.items()]
    tupla4.sort()

    return tupla4
  

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.
    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }
    """
    data = [row[4].split(',') for row in colums]
    data = [item for sublist in data for item in sublist]

    dic8 = {}
    for letter8 in data:
      codigo = letter8.split(':')[0]

      if codigo in dic8.keys():
        dic8[codigo] = dic8[codigo] +1 
      else:
        dic8[codigo] = 1
      
    return dic8

  
def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.
    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """
    t = [len(m[3].replace(",","")) for m in colums]
    u = [len(n[4].split(",")) for n in colums]

    list3 = [f[0] for f in colums]

    listfin = list(zip(list3, t, u))
    
    return listfin


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.
    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    list4 = []
    for p in colums:
      list4.append([p[1], p[3].split(",")])

    dic6 ={}
    for row in list4:
      for p in row[1]:
        if p in dic6:
          dic6[p] += int(row[0])
        else:
          dic6[p] = int(row[0])

    tupla5 = list(zip(dic6.keys(), dic6.values()))
    tupla5.sort()

    return tupla5


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
