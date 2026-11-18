# =====================================================================
#  1. CONSIGNA
# =====================================================================
#  [Pegá o resumí la consigna acá]
#
#  a)
#  b)
#  c)


# =====================================================================
#  2. AYUDA: si la consigna dice... → función
# =====================================================================
#  cola = signo de H1:  >  "derecha"  ·  <  "izquierda"  ·  ≠  "bilateral"
#  "¿se puede asegurar que X?" → X va en H1
#
#  --- DATOS ---
#  tabla con intervalos ......... nA, xA, sA = resumen_tabla([(20, 30, 8), (30, 40, 25)], "A")
#  valores sueltos .............. nA, xA, sA = resumen_lista([109, 108, 107], "A")
#  te dan n, x̄ y S .............. nA, xA, sA = 20, 4.6, 0.55
#
#  --- DOS PROMEDIOS (A vs B) ·  primero el grupo que nombra la frase ---
#  paso previo Fisher (α 10%) ... metodo = metodo_para_medias(nB, xB, sB, nA, xA, sA, nombres=("B", "A"))
#  "¿B más que A?" .............. ensayo_medias(metodo, 0, 0.05, nB, xB, sB, nA, xA, sA, "derecha", nombres=("B", "A"))
#  "¿más de un 10% más?" ........ igual, agregando h=1.10   ("10% menos" → h=0.90)
#  "¿difieren?" ................. igual, con "bilateral"
#  "5 unidades más" ............. delta0 = 5 (si no da cantidad, delta0 = 0)
#  σ "históricos" (conocidos) ... metodo = "conocidos" (Z, sin Fisher)
#  "diferencia mínima/máxima" ... intervalo_diferencia(metodo, 0.90, nB, xB, sB, nA, xA, sA, "minimo", nombres=("B", "A"))
#  "incremento % mínimo" ........ h_limite(metodo, 0.05, nB, xB, sB, nA, xA, sA, "derecha", nombres=("B", "A"))
#
#  --- APAREADAS (mismos individuos, "antes y después") · sin Fisher ---
#  ensayo ....................... ensayo_apareadas(antes, despues, 0, 0.05, "derecha", nombres=("Antes", "Después"))
#  intervalo .................... intervalo_apareadas(antes, despues, 0.90, "bilateral", nombres=("Antes", "Después"))
#
#  --- FISHER COMO PREGUNTA ("más regular", "reduce el desvío un 20%") ---
#  ensayo_varianzas(1, 0.05, nB, sB, nA, sA, "derecha", nombres=("B", "A"))     phi0 = 0.8 si "más de un 20%"
#
#  --- UNA PROPORCIÓN · r cuenta lo mismo que p ---
#  "¿cumple?" ................... ensayo_proporcion(0.07, 95, 8, 0.05, "derecha")
#  "estimar el %" ............... intervalo_proporcion(8, 95, 0.95, "bilateral")     o "maximo" / "minimo"
#  "% que no cumple" (tabla) .... r = contar_debajo(tabla, 8)   →   intervalo_proporcion(r, n, 0.95, "bilateral")
#  "¿cuántas más?" (error e) .... n_para_error_proporcion(8/95, 0.04, 0.95)      más = n − el n que tenías
#  "prob. de (no) detectar p1" .. rc = valor_critico_proporcion(0.07, 95, 0.05, "derecha")
#                                 beta_proporcion(rc, 95, 0.12, "derecha")       detectar = 1 − β
#
#  --- CHI CUADRADO ---
#  "¿sigue un modelo?" (tabla) .. bondad_ajuste(tabla, "normal", 0.05)    gamma, lognormal, weibull, gumbel_min, gumbel_max
#  con parámetros dados ......... bondad_ajuste(tabla, "normal", 0.05, {"mu": 20, "sigma": 2.5})
#  probabilidades dadas/iguales . bondad_proporciones([1, 2, 3, 4, 5, 6], [14, 6, 6, 13, 16, 5], None, 0.05)
#                                 bondad_proporciones(["24", "36", "40"], [85, 65, 50], [0.4, 0.4, 0.2], 0.05)
#  dos proporciones ............. contingencia([[5, 7], [104, 96]], 0.05)    fila 1 = éxitos, fila 2 = el resto
#  "¿depende de...?" ............ contingencia([[32, 45, 23], [14, 51, 15]], 0.05)
#
#  --- REGRESIÓN · x = la que explica, y = la que se explica ---
#  recta + validar + r² ......... regresion_simple(x, y, 0.05)
#  "¿baja en más de 0,5?" ....... ensayo_pendiente(x, y, -0.5, 0.05, "izquierda")
#  "contribución marginal" ...... intervalo_pendiente(x, y, 0.95)
#  "fuerza de la relación" ...... intervalo_correlacion(x, y, 0.95)
#  y PROMEDIO para x0 ........... estimar_media_regresion(x, y, 16, 0.95)
#  y de UN caso con x0 .......... predecir_regresion(x, y, 16, 0.95)

import _ruta
from formulas import *


# =====================================================================
#  3. RESOLUCIÓN
# =====================================================================

# a)


# b)


# c)

