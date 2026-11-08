# =====================================================================
#  EJEMPLO DE REFERENCIA: un segundo parcial completo, resuelto
#  Guía de Problemas, Tema VI, problema 20 (págs. 48-50). Al lado de cada
#  resultado está lo que dice la guía, para comparar.
# =====================================================================
#
#  Consigna: se ensayó la duración (en miles de horas) de equipos de dos
#  marcas, A y B. [La tabla está cargada abajo.]
#
#  a) ¿Qué marca se elegiría si no hay notoria diferencia de precios?
#  b) Según el fabricante, la marca A sigue un modelo Normal con
#     μ = 20 y σ = 2,5. ¿Se verifica?
#  c) Si no, ¿la marca A sigue algún modelo Normal?
#  d) Con un mínimo de 14.000 hs, estimar (95% de confianza) el porcentaje
#     de equipos de la marca B que no cumplen.
#
#  Cómo se lee: en cada punto, primero está el PLANTEO EN PAPEL (lo que
#  decide uno leyendo la consigna) y después la línea del programa, que
#  imprime el bloque "Para la hoja" con fórmulas y decisión.
# =====================================================================

import _ruta
from formulas import *

marca_a = [(10, 12, 2), (12, 14, 6), (14, 16, 13), (16, 18, 18), (18, 20, 30),
           (20, 22, 22), (22, 24, 16), (24, 26, 5), (26, 28, 1)]
marca_b = [(12, 14, 8), (14, 16, 18), (16, 18, 32), (18, 20, 57),
           (20, 22, 39), (22, 24, 26), (24, 26, 13), (26, 28, 10)]

# --- Datos de cada marca (marcas de clase) ---
n_a, x_a, s_a = n_agrupado(marca_a), media_agrupada(marca_a), desvio_agrupado(marca_a)
n_b, x_b, s_b = n_agrupado(marca_b), media_agrupada(marca_b), desvio_agrupado(marca_b)
print(f"A: n = {n_a}, x̄ = {x_a:.4f}, S = {s_a:.4f}   (guía: 113 ; 19,0531 ; 3,2892)")
print(f"B: n = {n_b}, x̄ = {x_b:.4f}, S = {s_b:.4f}   (guía: 203 ; 19,7685 ; 3,3479)")


# ===== a) ¿Qué marca conviene? =====
# PLANTEO EN PAPEL:
#   Es un ensayo sobre PROMEDIOS de dos poblaciones, con σ desconocidos
#   -> primero Fisher (paso previo) para elegir Pool o Welch, después t.
#   La muestra de B dura más en promedio -> quiero probar que B dura más.
#   Población 1 = B.   H0: μB - μA ≤ 0   H1: μB - μA > 0   -> cola "derecha"
#   α = 0,05 (no lo dan; se adopta 5%).
print("\n===== a) =====")
metodo = metodo_para_medias(n_b, x_b, s_b, n_a, x_a, s_a)          # guía: Pool
ensayo_medias(metodo, 0, 0.05, n_b, x_b, s_b, n_a, x_a, s_a, "derecha")
#                                                                    guía: dc = 0,6442, se rechaza
# CONCLUSIÓN: se puede asegurar que la marca B dura más -> se elige la marca B.


# ===== b) ¿Normal con los parámetros del fabricante? =====
# PLANTEO EN PAPEL:
#   Bondad de ajuste (Chi cuadrado). H0: la duración de A sigue una Normal
#   con μ = 20 y σ = 2,5. Los parámetros los da el fabricante -> p = 0.
print("\n===== b) =====")
bondad_ajuste(marca_a, "normal", 0.05, {"mu": 20, "sigma": 2.5})   # guía: χ² = 39,13, se rechaza
# CONCLUSIÓN: la duración de A NO sigue la Normal con los parámetros del fabricante.


# ===== c) ¿Sigue alguna Normal? =====
# PLANTEO EN PAPEL:
#   Bondad de ajuste con μ y σ estimados de la tabla -> p = 2.
print("\n===== c) =====")
bondad_ajuste(marca_a, "normal", 0.05)                             # guía: χ² = 2,13, no se rechaza
# CONCLUSIÓN: la Normal (con μ y σ estimados) es un buen candidato para la marca A.


# ===== d) Porcentaje de B que no cumple el mínimo de 14 (miles de hs) =====
# PLANTEO EN PAPEL:
#   Estimación (no hay hipótesis). Éxito = equipo que dura menos de 14.
#   r = cantidad de equipos de B por debajo de 14 en la tabla; n = 203.
print("\n===== d) =====")
r = contar_debajo(marca_b, 14)
intervalo_proporcion(r, n_b, 0.95)                                 # guía: 1,71% y 7,62%
# CONCLUSIÓN: con un 95% de confianza, entre el 1,7% y el 7,6% de los equipos
# de la marca B no cumplen la duración mínima de 14.000 hs.
