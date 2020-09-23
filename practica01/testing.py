# -*- coding: utf-8 -*-
# ESTE ARCHIVO SE QUEDA COMO ESTA, ES
# PARA EVALUACION

import sys
from procedimientos import *

def main(imagen_entrada, imagen_salida):
    imagen = cargar_imagen(imagen_entrada)
    imagen_bilinear = agrandar_imagen(imagen, 3)
    guardar_imagen(imagen_bilinear, imagen_salida)

if __name__ == "__main__":
    i_entrada = sys.argv[1]
    i_salida = sys.argv[2]
    main(i_entrada, i_salida)
