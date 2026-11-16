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
#  media(lista), desvio(lista)       si te dan los valores sueltos
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
#  contingencia(tabla_doble_entrada, alfa)     "¿depende de...?"

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
