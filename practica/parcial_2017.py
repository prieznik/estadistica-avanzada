# =====================================================================
#  Segundo parcial 2017 (Tema 2) - Ejercicio 1
#  Presencia de poros (en ppm) con dos procedimientos, A y B.
# =====================================================================
#
#  Resultado esperado (según la resolución manuscrita):
#    media A = 206,52   media B = 229
# =====================================================================

import _ruta  # para que Python encuentre la carpeta formulas
from formulas.datos import n_agrupado, media_agrupada, desvio_agrupado

# Datos de la consigna: (desde, hasta, frecuencia)
procedimiento_a = [
    (100, 150, 17),
    (150, 200, 51),
    (200, 250, 45),
    (250, 300, 16),
    (300, 350, 9),
]

procedimiento_b = [
    (100, 150, 15),
    (150, 200, 30),
    (200, 250, 50),
    (250, 300, 38),
    (300, 350, 17),
]

# Paso 1: sacar n, media y desvío de cada población
n_a = n_agrupado(procedimiento_a)
media_a = media_agrupada(procedimiento_a)
desvio_a = desvio_agrupado(procedimiento_a)

n_b = n_agrupado(procedimiento_b)
media_b = media_agrupada(procedimiento_b)
desvio_b = desvio_agrupado(procedimiento_b)

print(f"A: n = {n_a}, media = {media_a:.2f}, desvío = {desvio_a:.2f}")
print(f"B: n = {n_b}, media = {media_b:.2f}, desvío = {desvio_b:.2f}")
