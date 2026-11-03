# =====================================================================
#  MODELO DE PARCIAL 1 (para practicar, versión fácil)
# =====================================================================
#
#  EJERCICIO 1
#  Una panadería industrial tiene dos hornos, A y B. Se quiere saber si
#  el horno B cocina más rápido que el A. Se registró el tiempo de
#  cocción (en minutos) de 100 tandas de cada horno:
#
#      Tiempo (min)    Horno "A"   Horno "B"
#        40 - 50           6           2
#        50 - 60          20          12
#        60 - 70          38          30
#        70 - 80          24          34
#        80 - 90           8          16
#        90 - 100          4           6
#
#  OJO: más tiempo = cocina más LENTO. Leé bien qué te piden.
#
#  a) Calcular n, media y desvío de cada horno.
#  b) ¿Se pueden suponer iguales las varianzas de los dos hornos?
#     (método para comparar medias)
#  c) Con un riesgo del 5%, ¿se puede afirmar que el tiempo promedio
#     del horno B es MAYOR que el del horno A?
#  d) Con un 95% de confianza, ¿cuál es la diferencia MÍNIMA esperada
#     entre el tiempo promedio de B y el de A?
#  e) ¿Se puede considerar que los tiempos del horno A siguen un
#     modelo Normal? (riesgo del 5%)
#
#  EJERCICIO 2
#  Un proceso de envasado especifica un porcentaje de envases mal
#  sellados MÁXIMO del 5%. De una muestra de 100 envases elegidos al
#  azar, 9 estaban mal sellados.
#
#  a) ¿Se considera que el proceso cumple con la especificación,
#     tomando un riesgo máximo del 5%?
#  b) Con un 95% de confianza, estimar el porcentaje de envases BIEN
#     sellados de toda la producción.
#
# =====================================================================
#  CÓMO ENCARARLO
#    1) Para cada punto, primero decidí vos (en un comentario):
#       qué población va como 1, la hipótesis, la cola y el α.
#    2) Después llamá a la función que corresponde.
#    3) Escribí la conclusión en palabras del problema.
#  Si te trabás, mirá practica/guia_tema6_ej20.py: tiene el mismo formato.
# =====================================================================

import _ruta
from formulas.hipotesis import planteo
from formulas.datos import n_agrupado, media_agrupada, desvio_agrupado
from formulas.medias import metodo_para_medias, ensayo_medias, intervalo_diferencia
from formulas.chi_cuadrado import bondad_ajuste
from formulas.proporciones import ensayo_proporcion, intervalo_proporcion

horno_a = [
    (40, 50, 6),
    (50,60,20),
    (60,70,38),
    (70,80,24),
    (80,90,8),
    (90,100,4)
]

horno_b = [
    (40, 50, 2),
    (50,60,12),
    (60,70,30),
    (70,80,34),
    (80,90,16),
    (90,100,6)
]

# ===== Ejercicio 1 =====

# a)
n_a = n_agrupado(horno_a)
n_b = n_agrupado(horno_b)

media_a = media_agrupada(horno_a)
media_b = media_agrupada(horno_b)

desvio_a = desvio_agrupado(horno_a)
desvio_b = desvio_agrupado(horno_b)

print("Horno A: n =", n_a, "media =", media_a, "desvío =", desvio_a)
print("Horno B: n =", n_b, "media =", media_b, "desvío =", desvio_b)

# b)

# c)  Decido: población 1 = ___   H1: ___   cola = ___   α = ___

# d)

# e)

# ===== Ejercicio 2 =====

# a)  Decido: éxito = ___   p0 = ___   cola = ___   α = ___
#     (pista: control de producción -> ¿optimista o pesimista?)

# b)  Ojo: te piden los BIEN sellados -> r = ___
