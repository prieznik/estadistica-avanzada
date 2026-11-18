# =====================================================================
#  1. CONSIGNA
# =====================================================================
#  [Nombre del ejercicio]
#
#  [Pegá o resumí la consigna acá]
#
#  a)
#  b)
#  c)


# =====================================================================
#  2. AYUDA: qué hace cada función y qué datos le pasás
# =====================================================================
#
#  CADA BLOQUE SALE EN ESTE ORDEN (copialo así en la hoja):
#    Hipótesis -> Justificación -> Muestra -> Valor crítico -> CR -> RD -> Decisión
#    CR = condición de rechazo (la cuenta: "si d ≥ dc se rechaza H0")
#    RD = regla de decisión (qué se hace: "si se rechaza, se compra B")
#
#  REGLAS PARA ESCRIBIR LOS DATOS
#    Decimales con PUNTO (0.05). Porcentajes entre 0 y 1 (7% -> 0.07).
#    cola = "derecha" (H1 >) | "izquierda" (H1 <) | "bilateral" (H1 ≠, solo promedios)
#    tipo = "bilateral" (estimar entre cuánto y cuánto) | "minimo" | "maximo"
#    Tabla: [(desde, hasta, frecuencia), ...]
#        tablaA = [(20, 30, 8), (30, 40, 25), (40, 50, 34)]
#
#  ---------------------------------------------------------------------
#  PASO 1: SACAR n, MEDIA Y DESVÍO DE CADA GRUPO
#  ---------------------------------------------------------------------
#  n, x, s = resumen_tabla(tabla, "nombre")
#      Qué hace: calcula n, x̄ y S de una tabla y los imprime con fórmulas.
#      Le pasás: la tabla y un nombre para el título.
#      Te devuelve: n, x, s (guardalos en variables para usarlos después).
#      Ej:  nA, xA, sA = resumen_tabla(tablaA, "Línea A")
#
#  n, x, s = resumen_lista(lista, "nombre")
#      Igual que resumen_tabla pero para valores sueltos ("109 - 108 - 107 ...").
#      Ej:  manana = [109, 108, 108, 107]
#           nM, xM, sM = resumen_lista(manana, "Turno mañana")
#  Si la consigna YA te da n, media y desvío: nA, xA, sA = 20, 4.6, 0.55
#
#  ---------------------------------------------------------------------
#  COMPARAR PROMEDIOS DE DOS GRUPOS (A vs B)
#  ---------------------------------------------------------------------
#  Grupo 1 = el que nombra la frase ("B produce más que A" -> 1 = B, 2 = A).
#  El orden de los datos siempre es: n1, x1, s1, n2, x2, s2.
#  nombres=("B", "A") es opcional: hace que el bloque escriba μB y μA
#  en vez de μ1 y μ2.
#
#  metodo = metodo_para_medias(n1, x1, s1, n2, x2, s2)
#      Qué hace: el PASO PREVIO. Fisher con α = 10% para ver si las
#      varianzas son iguales. Imprime el bloque para la hoja.
#      Te devuelve: "pool" (iguales) o "welch" (distintas).
#      Ej:  metodo = metodo_para_medias(nB, xB, sB, nA, xA, sA, nombres=("B", "A"))
#
#  ensayo_medias(metodo, delta0, alfa, n1, x1, s1, n2, x2, s2, cola, h=1)
#      Qué hace: el ensayo "¿se puede asegurar que 1 produce más que 2?".
#      Le pasás:
#        metodo  -> lo que te dio metodo_para_medias
#                   ("conocidos" si te dan los σ: usa Z, sin paso previo)
#        delta0  -> el número de la hipótesis escrita como resta.
#                   Si la consigna NO da una cantidad ("B produce más que A")
#                   -> delta0 = 0.  Solo si da una cantidad fija
#                   ("5 unidades más") -> delta0 = 5.
#        alfa    -> el riesgo de la consigna (0.05)
#        cola    -> el signo de H1
#        h       -> solo con porcentaje: "10% más" -> h=1.10; "10% menos" -> h=0.90
#      Ej:  ensayo_medias(metodo, 0, 0.05, nB, xB, sB, nA, xA, sA, "derecha", nombres=("B", "A"))
#      Ej:  ensayo_medias(metodo, 0, 0.05, nB, xB, sB, nA, xA, sA, "derecha", h=1.10, nombres=("B", "A"))
#
#  intervalo_diferencia(metodo, confianza, n1, x1, s1, n2, x2, s2, tipo)
#      Qué hace: estima la diferencia μ1 - μ2.
#      Le pasás: confianza (0.90) y tipo ("minimo" para "diferencia mínima").
#      Ej:  intervalo_diferencia(metodo, 0.90, nB, xB, sB, nA, xA, sA, "minimo", nombres=("B", "A"))
#
#  h_limite(metodo, alfa, n1, x1, s1, n2, x2, s2, cola)
#      Qué hace: "¿qué porcentaje mínimo se puede garantizar?"
#
#  ---------------------------------------------------------------------
#  MUESTRAS APAREADAS (los MISMOS individuos medidos dos veces)
#  ---------------------------------------------------------------------
#  "antes y después", "cada empleado con y sin", "el mismo zapato tratado y sin
#  tratar" -> NO hay Fisher. Se restan los pares y se hace t de Student, gl = n - 1.
#  ensayo_apareadas(lista1, lista2, delta0, alfa, cola, nombres=("1", "2"))
#      Ej: "¿la capacitación reduce el tiempo en más de 10 minutos?"
#          ensayo_apareadas(sin, con, 10, 0.05, "derecha", nombres=("Sin", "Con"))
#  intervalo_apareadas(lista1, lista2, confianza, tipo, nombres)
#
#  ---------------------------------------------------------------------
#  FISHER COMO PREGUNTA ("¿más regular?", "¿menor variabilidad?")
#  ---------------------------------------------------------------------
#  ensayo_varianzas(phi0, alfa, n_arriba, s_arriba, n_abajo, s_abajo, cola)
#      Le pasás: phi0 = 1 (o 0.8 si "reduce más de un 20%"), el α de la
#      consigna, y arriba el grupo que nombra la frase.
#      Ej:  ensayo_varianzas(1, 0.05, nB, sB, nA, sA, "derecha", nombres=("B", "A"))
#
#  ---------------------------------------------------------------------
#  PROPORCIONES (un porcentaje: fallas, defectuosas, buenas...)
#  ---------------------------------------------------------------------
#  r = cuántos cumplen lo que cuenta p (si p = fallas, r = las fallas).
#
#  ensayo_proporcion(p0, n, r, alfa, cola)
#      "¿Cumple la especificación?" Te da rc, regla y decisión.
#      Ej: "fallas máximo 7%, 8 de 95, riesgo 5%"
#           ensayo_proporcion(0.07, 95, 8, 0.05, "derecha")
#  intervalo_proporcion(r, n, confianza, tipo)
#      "Estimar el porcentaje". Ej: intervalo_proporcion(8, 95, 0.95, "bilateral")
#  beta_proporcion(rc, n, p1, cola)
#      "Prob. de NO detectar si en realidad es p1". Detectar = 1 - β.
#  n_para_error_proporcion(p_hat, e, confianza)      "¿cuántas unidades?" (error)
#  n_para_relacion_proporcion(p_hat, R, confianza)   "¿cuántas unidades?" (relación)
#  reducir(valor, porcentaje)      "reducir un 30%" -> reducir(R, 0.30)
#  contar_debajo(tabla, valor)     r = cuántos quedan por debajo de un valor
#  contar_encima(tabla, valor)     r = cuántos quedan por encima
#
#  ---------------------------------------------------------------------
#  CHI CUADRADO ("¿sigue un modelo...?")
#  ---------------------------------------------------------------------
#  bondad_ajuste(tabla, modelo, alfa)
#      modelo: "normal", "lognormal", "gamma", "weibull", "gumbel_min", "gumbel_max"
#      Si te dan los parámetros: bondad_ajuste(tabla, "normal", 0.05, {"mu": 20, "sigma": 2.5})
#      Ej:  bondad_ajuste(tablaB, "normal", 0.05)
#  bondad_proporciones(categorias, observados, probabilidades=None, alfa)
#      Sin intervalos, con probabilidades DADAS o iguales ("¿el dado está
#      cargado?", "¿igualmente distribuidas?", "históricamente el 40%...").
#      Ej:  bondad_proporciones([1, 2, 3, 4, 5, 6], [14, 6, 6, 13, 16, 5], None, 0.05)
#      Ej:  bondad_proporciones(['24"', '36"', '40"'], [85, 65, 50], [0.40, 0.40, 0.20], 0.05)
#  contingencia(tabla_doble_entrada, alfa)     "¿depende de...?"
#      También sirve para COMPARAR DOS PROPORCIONES (prueba de consistencia):
#      "turno mañana 109 productos, 5 defectuosos; tarde 103, 7 defectuosos"
#           contingencia([[5, 7], [104, 96]], 0.05)
#           (fila 1 = defectuosos de cada grupo, fila 2 = buenos de cada grupo)
#
#  ---------------------------------------------------------------------
#  REGRESIÓN LINEAL SIMPLE (y = lo que se quiere explicar, x = la que explica)
#  ---------------------------------------------------------------------
#  regresion_simple(x, y, alfa, nombres=("Horas", "Minutos"))
#      recta ŷ = b0 + b1·x, S, Sb1, r, r² y validación (H0: β1 = 0)
#  ensayo_pendiente(x, y, beta10, alfa, cola)
#      "¿por cada hora más, los minutos bajan en más de 0,5?" -> beta10 = -0.5, "izquierda"
#  intervalo_pendiente(x, y, confianza)       "estimar la contribución marginal"
#  intervalo_correlacion(x, y, confianza)     "estimar la fuerza de la relación" (ρ y ρ²)
#  estimar_media_regresion(x, y, x0, confianza)  y PROMEDIO para x0 ("en promedio")
#  predecir_regresion(x, y, x0, confianza)       y de UN caso para x0 ("un empleado")

import _ruta
from formulas import *


# =====================================================================
#  3. DATOS DE CONTEXTO
# =====================================================================
#  Planteo en papel (antes de programar), para cada punto:
#    Herramienta:
#    Población 1 / qué cuenta p (éxito):
#    H0:                      H1:
#    Cola:                    α:

# Tablas y datos de la consigna:



# =====================================================================
#  4. RESOLUCIÓN
# =====================================================================

# --- a) ---


# Conclusión en palabras:
#


# --- b) ---


# Conclusión en palabras:
#
