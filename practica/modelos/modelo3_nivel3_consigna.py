# =====================================================================
#  1. CONSIGNA
# =====================================================================
#  MODELO 3 · NIVEL 3 (integrador y más largo que un parcial real)
#  Tiempo sugerido: 2 h 30 min. Si no te alcanza, está bien: es a propósito.
#  En cada problema: justificar las hipótesis y explicar las distribuciones.
#
#  1) Se propone un nuevo método de armado (N) para reducir la variabilidad de
#     los tiempos respecto del método actual (A). Tiempos (en minutos):
#
#     Actual (A): 24,1 - 26,8 - 22,5 - 28,9 - 25,3 - 21,7 - 27,6 - 23,8 - 29,4 - 24,9 - 26,2 - 22,0
#     Nuevo (N):  24,6 - 25,3 - 23,9 - 26,1 - 24,8 - 25,7 - 23,5 - 26,4 - 25,0 - 24,2
#
#     a) El método nuevo se adopta si se puede asegurar que reduce el desvío
#        estándar de los tiempos en más de un 20%. Con un riesgo del 10%,
#        ¿se aconseja adoptarlo?
#     b) Con un riesgo del 5%, ¿puede suponerse que los tiempos medios de
#        ambos métodos difieren?
#     c) Estimar la diferencia entre ambos tiempos medios con un 95% de confianza.
#
#  2) Se sospecha que la calidad difiere entre turnos. En el turno mañana se
#     revisaron 180 productos y 9 eran defectuosos; en el turno tarde se
#     revisaron 160 y 19 eran defectuosos.
#     a) Con un riesgo del 5%, ¿se puede asegurar que el porcentaje de
#        defectuosos difiere entre los turnos?
#     b) Se clasificó la producción de los tres turnos en primera, segunda y
#        rechazo:
#                    Primera   Segunda   Rechazo
#          Mañana      150        24         6
#          Tarde       128        22        10
#          Noche        95        12        13
#        Con un riesgo del 5%, ¿la calidad depende del turno?
#
#  3) Se estudia la relación entre las horas de entrenamiento previo (x) y los
#     minutos de producción por unidad (y) de 10 empleados:
#
#       Horas (x):    30   32   35   36   38   40   42   44   45   48
#       Minutos (y): 118  117  114  115  112  110  111  108  107  104
#
#     a) Construir el modelo de regresión e interpretar los estimadores.
#     b) Validar el modelo con un 5% de riesgo.
#     c) ¿Se puede afirmar, con un 5% de riesgo, que por cada hora adicional
#        de entrenamiento los minutos de producción bajan en más de 0,6?
#     d) Estimar con un 95% de confianza la fuerza de la relación y el
#        porcentaje del tiempo de producción que explica el modelo.
#     e) Estimar con un 95% de confianza los minutos PROMEDIO de los
#        empleados con 40 horas de entrenamiento.
#     f) Un empleado nuevo tiene 40 horas de entrenamiento: ¿entre qué
#        valores estará su tiempo de producción (95%)? Explicar por qué este
#        intervalo es más ancho que el de e).
#
#  4) Un proceso se controla tomando muestras de 80 unidades y se detiene si
#     se encuentran 6 o más defectuosas. En condiciones normales el proceso
#     trabaja con un 3% de defectuosas.
#     a) ¿Cuál es la probabilidad de detener el proceso cuando funciona
#        normalmente? Plantear la hipótesis que se está ensayando.
#     b) ¿Cuál es la probabilidad de detener el proceso si el porcentaje de
#        defectuosas sube al 8%?
#
#  Cuando termines (o si te trabás), mirá modelo3_nivel3_resolucion.py


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
#  3. RESOLUCIÓN
# =====================================================================

# 1 a)


# 1 b)


# 1 c)


# 2 a)


# 2 b)


# 3 a)


# 3 b)


# 3 c)


# 3 d)


# 3 e)


# 3 f)


# 4 a)


# 4 b)


