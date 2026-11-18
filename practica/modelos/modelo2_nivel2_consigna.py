# =====================================================================
#  1. CONSIGNA
# =====================================================================
#  MODELO 2 · NIVEL 2 (parcial típico: porcentajes, Gamma, β, apareadas)
#  Tiempo sugerido: 2 h 15 min. En cada problema: justificar las hipótesis y
#  explicar las distribuciones.
#
#  1) Una empresa evalúa reemplazar el componente actual (A) de sus equipos por
#     uno nuevo (N), más caro. Se registró la duración (en miles de horas) de
#     100 componentes de cada tipo:
#
#       Duración     Actual (A)   Nuevo (N)
#        0 - 4           10            5
#        4 - 8           32           22
#        8 - 12          30           33
#       12 - 16          16           22
#       16 - 20           8           12
#       20 - 24           4            6
#
#     a) Con un riesgo del 5%, ¿se puede asegurar que el componente nuevo
#        dura en promedio más que el actual?
#     b) El reemplazo solo se justifica si el nuevo dura más de un 10% más
#        que el actual. Con el mismo riesgo, ¿se aconseja el reemplazo?
#     c) ¿Qué incremento porcentual mínimo de la duración promedio se puede
#        garantizar con el componente nuevo, con un 5% de riesgo?
#     d) Con un riesgo del 5%, ¿se puede considerar que la duración del
#        componente nuevo se ajusta a un modelo Gamma?
#     e) Si se exige una duración mínima de 8.000 horas, estimar con un 95%
#        de confianza el porcentaje de componentes nuevos que no la cumplen.
#
#  2) Un proveedor tiene actualmente un 8% de piezas defectuosas. La empresa
#     cambiará a un proveedor más caro solo si se puede asegurar que este
#     tiene un porcentaje de defectuosas menor al 8%. Se le pidieron 200
#     piezas y se encontraron 9 defectuosas.
#     a) Con un riesgo del 5%, ¿se aconseja cambiar de proveedor?
#     b) ¿Cuál es la probabilidad de cambiar de proveedor si en realidad el
#        nuevo tiene un 4% de defectuosas?
#     c) Estimar, con un 95% de confianza, el porcentaje máximo de piezas
#        defectuosas del nuevo proveedor.
#
#  3) Se capacitó a 8 operarios para reducir el tiempo de armado de un
#     equipo. Se midió el tiempo (en minutos) de cada operario antes y
#     después de la capacitación:
#
#       Operario:   1   2   3   4   5   6   7   8
#       Antes:     52  48  55  60  47  58  51  56
#       Después:   47  45  49  53  46  52  48  50
#
#     a) Con un riesgo del 5%, ¿se puede asegurar que la capacitación reduce
#        el tiempo promedio de armado en más de 3 minutos?
#     b) Estimar, con un 90% de confianza, la reducción promedio del tiempo.
#
#  Cuando termines (o si te trabás), mirá modelo2_nivel2_resolucion.py


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

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from formulas import *


# =====================================================================
#  3. DATOS DE CONTEXTO
# =====================================================================
#  Planteo en papel (antes de programar), para cada punto:
#    Herramienta:
#    Población 1 / qué cuenta p (éxito):
#    H0:                      H1:
#    Cola:                    α:

# Tablas y datos de la consigna (ya cargados):
tablaA = [(0, 4, 10), (4, 8, 32), (8, 12, 30), (12, 16, 16), (16, 20, 8), (20, 24, 4)]
tablaN = [(0, 4, 5), (4, 8, 22), (8, 12, 33), (12, 16, 22), (16, 20, 12), (20, 24, 6)]

antes   = [52, 48, 55, 60, 47, 58, 51, 56]
despues = [47, 45, 49, 53, 46, 52, 48, 50]


# =====================================================================
#  4. RESOLUCIÓN
# =====================================================================

# --- 1 a) ---
nA, xA, sA= resumen_tabla(tablaA)
nN, xN, sN= resumen_tabla(tablaN)

metodo = metodo_para_medias(nN, xN, sN, nA, xA, sA, nombres=("Nueva", "Actual"))
ensayo_medias(metodo, 0, 0.05, nN, xN, sN, nA, xA, sA, "derecha", nombres=("Nueva", "Actual"))


# --- 1 b) ---
ensayo_medias(metodo, 0, 0.05, nN, xN, sN, nA, xA, sA, "derecha", h=1.10, nombres=("Nueva", "Actual"))

# --- 1 c) ---
intervalo_diferencia(metodo, 1-0.05, nN, xN, sN, nA, xA, sA, "minimo", nombres=("N", "A"))


# --- 1 d) ---
bondad_ajuste(tablaN, "gamma", 0.05)


# --- 1 e) ---
print(contar_encima(tablaN, 8))



# --- 2 a) ---


# Conclusión en palabras:
#


# --- 2 b) ---


# Conclusión en palabras:
#


# --- 2 c) ---


# Conclusión en palabras:
#


# --- 3 a) ---


# Conclusión en palabras:
#


# --- 3 b) ---


# Conclusión en palabras:
#


