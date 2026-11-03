# =====================================================================
#  Guía de Problemas - Tema VI, problema 20 (marcas A y B, duración)
#  EJEMPLO COMPLETO: es un "segundo parcial" entero y está resuelto en la
#  guía (págs. 48-50), así que podés comparar cada número.
# =====================================================================
#
#  a) ¿Qué marca se elegiría si no hay notoria diferencia de precios?
#  b) ¿La marca A es Normal con μ = 20 y σ = 2,5 (miles de horas)?
#  c) Si no, ¿la marca A sigue algún modelo Normal?
#  d) Con un mínimo de 14.000 hs, estimar (5% de riesgo) el porcentaje
#     de equipos de la marca B que no cumplen.
# =====================================================================

import _ruta
from formulas.hipotesis import planteo
from formulas.datos import n_agrupado, media_agrupada, desvio_agrupado, contar_debajo
from formulas.medias import metodo_para_medias, ensayo_medias
from formulas.chi_cuadrado import bondad_ajuste
from formulas.proporciones import intervalo_proporcion

marca_a = [(10, 12, 2), (12, 14, 6), (14, 16, 13), (16, 18, 18), (18, 20, 30),
           (20, 22, 22), (22, 24, 16), (24, 26, 5), (26, 28, 1)]
marca_b = [(12, 14, 8), (14, 16, 18), (16, 18, 32), (18, 20, 57),
           (20, 22, 39), (22, 24, 26), (24, 26, 13), (26, 28, 10)]

# --- Datos de cada marca ---
n_a, x_a, s_a = n_agrupado(marca_a), media_agrupada(marca_a), desvio_agrupado(marca_a)
n_b, x_b, s_b = n_agrupado(marca_b), media_agrupada(marca_b), desvio_agrupado(marca_b)
print(f"A: n = {n_a}, x̄ = {x_a:.4f}, S = {s_a:.4f}   (guía: 113 ; 19,0531 ; 3,2892)")
print(f"B: n = {n_b}, x̄ = {x_b:.4f}, S = {s_b:.4f}   (guía: 203 ; 19,7685 ; 3,3479)")

# --- a) ¿B dura más que A? ---
# Decido: quiero probar que B dura más -> B es la población 1.
print("\n===== a) =====")
metodo = metodo_para_medias(n_b, x_b, s_b, n_a, x_a, s_a)          # guía: Pool
cola = planteo("μB - μA", ">", 0)
ensayo_medias(metodo, 0, 0.05, n_b, x_b, s_b, n_a, x_a, s_a, cola)  # guía: dc = 0,6442, se rechaza
# Conclusión: se puede asegurar que B dura más -> se elige la marca B.

# --- b) Normal con los parámetros del fabricante ---
print("\n===== b) =====")
bondad_ajuste(marca_a, "normal", 0.05, {"mu": 20, "sigma": 2.5})   # guía: χ² = 39,13, se rechaza

# --- c) Normal con parámetros estimados ---
print("\n===== c) =====")
bondad_ajuste(marca_a, "normal", 0.05)                             # guía: χ² = 2,13, no se rechaza

# --- d) Porcentaje de B por debajo de 14 (miles de horas) ---
print("\n===== d) =====")
r = contar_debajo(marca_b, 14)
A, B = intervalo_proporcion(r, n_b, 0.95)
print(f"r = {r} de {n_b}  ->  entre {A:.2%} y {B:.2%}   (guía: 1,71% y 7,62%)")
