# -*- coding: utf-8 -*-
import cv2

import numpy as np

# Método auxiliar para mostrar una imagen
def mostrar_imagen(arreglo_bidimensional, titulo_de_ventana=None):
    if not titulo_de_ventana:
        titulo_de_ventana = "%dx%d" % arreglo_bidimensional.shape[:2] 
   
    assert isinstance(titulo_de_ventana, str)

    arreglo_bidimensional = arreglo_bidimensional.astype('uint8')
    cv2.imshow(titulo_de_ventana, arreglo_bidimensional)
    
    while cv2.getWindowProperty(titulo_de_ventana, 
                                cv2.WND_PROP_VISIBLE) >= 1:
        if cv2.waitKeyEx(1000) == 27:
            cv2.destroyWindow(titulo_de_ventana)
            break

# Método donde se cargará el archivo txt
def cargar_imagen(ruta_imagen_txt):
    with open(ruta_imagen_txt, "r") as fp:
       img_contents = fp.readlines()
    
    # TODO: AQUÍ VA EL CODIGO
    
    # regrisa una matriz de enteros sin signo de 8 bits
    return img.astype('uint8')

# Método para agrandar la imágen
def agrandar_imagen(arreglo_bidimensional, tamaño):
    ''' tamaño será un número entero (en el caso del ejemplo, la función recibe un 3) '''
    
    # esto crea una imagen en blanco
    # white_img = np.ones((no_filas, no_columnas)) * 255
    
    # TODO: AQUÍ VA EL CODIGO
    return blank_img

# Método para guardar la imagen en un archivo de texto
def guardar_imagen(arreglo_bidimensional, ruta_de_salida="../resultado.txt"):
    ''' Formato: linea 1 no_filas, linea 2 no_columnas, linea 3 vector de intensidad normalizado (concatenación de columnas verticales) '''

    # TODO: AQUÍ VA EL CODIGO
    
    # aquí no vamos a guardar nada, la salida se escribe en disco
    raise NotImplementedError("No está implementado")

