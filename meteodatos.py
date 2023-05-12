#! /usr/bin/env-python
# -*- coding: utf-8 -*-

# meteodatos - librería para la consulta de datos meteorológicos obtenidos desde
# las bases de datos disponibles en https://climatologia.meteochile.gob.cl/application/index/menuTematicoEmas
# versión: 0.1
# fecha: abril de 2023
# github: cmoralesd/aprendiendo-python


def leer_archivo(nombre_archivo):
    # nombre_archivo: un archivo csv obtenido desde https://climatologia.meteochile.gob.cl/application/index/menuTematicoEmas
    # retorna: el contenido del archivo como una lista, cuyos elementos son las
    #          líneas del archivo original, sin el caracter final '\n'
    contenido = []
    try:
        with open(nombre_archivo) as archivo:
            for linea in archivo:
                contenido.append(linea[:-1])
        print(f'El archivo fue leido correctamente: {nombre_archivo}')
    except:
        print(f'ERROR: No se pudo abrir el archivo: {nombre_archivo}')
    return contenido  
    

def datos_registrados(datos):
    # parametros:
    #   datos[], es una lista con una fila de encabezado
    # retorna:
    #   una lista con los nombres encontrados en la fila de cabecera
<<<<<<< HEAD
    datos_encontrados = []
    for dato in datos[0].split(';'):
        datos_encontrados.append(dato)
=======
    datos_encontrados = datos[0].split(';')[0]
>>>>>>> ff042ba392f665b07770e784b82d6cff333586ea
    return datos_encontrados


def filtrar_cabecera(datos, filtro):
    # datos: la lista con los datos leidos desde el archivo csv
    # filtro: una variable 'str' con el nombre de cabecera que se desea filtrar
    # retorna: una lista con todas las filas de 'datos', pero conteniendo únicamente los datos bajo el nombre 'filtro'.
    #          Los datos que representan números están en formato numérico correspondiente (int o float)

    # identificamos el índice de columna para 'filtro'
    index = datos[0].split(';').index(filtro)
    datos_filtrados = []
    for fila in datos:
        valor = fila.split(';')[index]
        if valor.isnumeric():
            valor = int(valor)
        else:
            try:
                valor = float(valor)
            except:
                pass
        datos_filtrados.append(valor)     
    return datos_filtrados
        
 
def filtrar_dia(datos, dia):
    # datos: una lista cuyas filas contienen los datos agrupados como una cadena de texto
    # dia:   el día que se desea filtrar, en formato 'AAAA-MM-DD', ejemplo: '2023-03-01'
    # retorna: la misma lista 'datos', pero conteniendo únicamente las filas
    #          que coinciden con 'dia' y manteniendo la cabecera
    
<<<<<<< HEAD
    filtrados = []
    for fila in datos:
        # separamos los datos en cada fila para verificar la fecha ingresada en 'dia' está en 'momento'
        # (la fecha podría aparecer en otro campo, pero solo nos interesa 'momento')
        if dia in fila.split(';')[3]:
            filtrados.append(fila)
    # se agrega la fila de cabecera
    filtrados.insert(0, datos[0])
    return filtrados
=======
    # TODO: Escriba su código aquí
    # ---------------------------------------------
    datos_f = []
    datos_f.append(datos[0])
    for fila in datos[1:]:
        if dia in fila:
            datos_f.append(fila)
    datos_f.pop(1)
    datos_f.pop(1)
    return datos_f

    # ---------------------------------------------
    
    return []  # reemplace la lista vacía [] por el resultado de su código
>>>>>>> ff042ba392f665b07770e784b82d6cff333586ea


def estadisticas_dia(datos, dia):
    # datos: una lista con datos leidos desde la base de datos meteorológicos,
    #        mediante la función 'leer_archivo()'
    # dia:   el día que se desea reportar, en formato 'AAAA-MM-DD', ejemplo: '2023-03-01'
    # retorna: tmax, tmin, tmedia, la temperatura máxima, mínima y promedio para el día.
<<<<<<< HEAD
    
    tmax = tmin = tmedia = 0
    # primero eliminamos todas las filas que no correspondan a 'dia'
    filtro_dia = filtrar_dia(datos, dia)
    # luego filtramos para dejar solo la columna 'ts'
    filtro_t = filtrar_cabecera(filtro_dia, 'ts')
    # finalmente eliminamos la cabecera y calculamos las estadisticas
    t = filtro_t[1:]
    tmax = max(t)
    tmin = min(t)
    tmedia = round(sum(t)/len(t), 1)
=======
    tmax = tmin = tmedia = 0
    
    # TODO: Escriba su código aquí
    # ---------------------------------------------
    cabecera_ts = []
    cabecera_ts = filtrar_dia(datos,dia)
    datos_f1 = filtrar_cabecera(cabecera_ts, 'ts')
    datos_f1.remove('ts')
    tmax = max(datos_f1)
    tmin = min(datos_f1)
    tmedia = round(sum(datos_f1)/len(datos_f1),1)


    # ---------------------------------------------
    # Su código termina aquí, luego se retornan los datos calculados
>>>>>>> ff042ba392f665b07770e784b82d6cff333586ea
    
    return tmax, tmin, tmedia
    
  
