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
#  tipo = "bilateral" (estimar) · "minimo" · "maximo"
#  "¿se puede asegurar que X?" → X va en H1 · decimales con punto, % entre 0 y 1
#
#  --- DATOS ---
#  tabla con intervalos ......... n, x, s = resumen_tabla(tabla, "nombre")     tabla = [(desde, hasta, frecuencia), ...]
#  valores sueltos .............. n, x, s = resumen_lista(lista, "nombre")     lista = [valor, valor, ...]
#  te dan n, x̄ y S .............. n, x, s = n_dato, media_dato, desvio_dato
#
#  --- DOS PROMEDIOS · grupo 1 = el que nombra la frase ("B más que A" → 1 = B) ---
#  paso previo Fisher (α 10%) ... metodo = metodo_para_medias(n1, x1, s1, n2, x2, s2, nombres=("1", "2"))
#  "¿1 más que 2?" .............. ensayo_medias(metodo, delta0, alfa, n1, x1, s1, n2, x2, s2, cola, nombres=("1", "2"))
#                                 delta0 = 0 si no da cantidad ("5 unidades más" → 5)
#  "¿más de un X% más?" ......... igual, agregando h=1.X   ("10% más" → h=1.10 · "10% menos" → h=0.90)
#  σ "históricos" (conocidos) ... metodo = "conocidos"  (Z, sin Fisher)
#  "diferencia mínima/máxima" ... intervalo_diferencia(metodo, confianza, n1, x1, s1, n2, x2, s2, tipo, nombres=("1", "2"))
#  "incremento % mínimo" ........ h_limite(metodo, alfa, n1, x1, s1, n2, x2, s2, "derecha", nombres=("1", "2"))
#
#  --- APAREADAS (mismos individuos, "antes y después") · sin Fisher ---
#  ensayo ....................... ensayo_apareadas(lista1, lista2, delta0, alfa, cola, nombres=("1", "2"))
#  intervalo .................... intervalo_apareadas(lista1, lista2, confianza, tipo, nombres=("1", "2"))
#
#  --- FISHER COMO PREGUNTA ("más regular", "reduce el desvío un 20%") ---
#  ensayo_varianzas(phi0, alfa, n1, s1, n2, s2, cola, nombres=("1", "2"))     phi0 = 1, o 0.8 si "más de un 20%"
#
#  --- UNA PROPORCIÓN · r = cuántos cumplen lo que cuenta p ---
#  "¿cumple?" ................... ensayo_proporcion(p0, n, r, alfa, cola)       p0 = el % de la consigna
#  "estimar el %" ............... intervalo_proporcion(r, n, confianza, tipo)
#  "% que no cumple" (tabla) .... r = contar_debajo(tabla, valor)    →    intervalo_proporcion(r, n, confianza, tipo)
#                                 (contar_encima(tabla, valor) para "por encima de")
#  "¿cuántas más?" (error e) .... n_para_error_proporcion(r / n, e, confianza)   más = n nuevo − n que tenías
#  "prob. de (no) detectar p1" .. rc = valor_critico_proporcion(p0, n, alfa, cola)
#                                 beta_proporcion(rc, n, p1, cola)                detectar = 1 − β
#
#  --- CHI CUADRADO ---
#  "¿sigue un modelo?" (tabla) .. bondad_ajuste(tabla, modelo, alfa)     modelo = "normal", "gamma", "lognormal",
#                                                                         "weibull", "gumbel_min", "gumbel_max"
#  con parámetros dados ......... bondad_ajuste(tabla, "normal", alfa, {"mu": valor, "sigma": valor})
#  probabilidades dadas/iguales . bondad_proporciones(categorias, observados, probabilidades, alfa)
#                                 probabilidades = None si son todas iguales, o [p1, p2, ...]
#  dos proporciones ............. contingencia([[r1, r2], [n1 - r1, n2 - r2]], alfa)
#  "¿depende de...?" ............ contingencia(tabla_doble_entrada, alfa)    tabla = [[fila 1], [fila 2], ...]
#
#  --- REGRESIÓN · x = la que explica, y = la que se explica ---
#  recta + validar + r² ......... regresion_simple(x, y, alfa)              x, y = listas
#  "¿baja/sube en más de V?" .... ensayo_pendiente(x, y, beta10, alfa, cola)   "baja más de 0,5" → beta10 = -0.5, "izquierda"
#  "contribución marginal" ...... intervalo_pendiente(x, y, confianza)
#  "fuerza de la relación" ...... intervalo_correlacion(x, y, confianza)
#  y PROMEDIO para x0 ........... estimar_media_regresion(x, y, x0, confianza)
#  y de UN caso con x0 .......... predecir_regresion(x, y, x0, confianza)

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


