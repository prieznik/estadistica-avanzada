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
#  PASO 0 · ¿QUÉ ME PIDEN? (mirá el verbo de la consigna)
#   "¿se puede asegurar...?", "¿cumple?", "¿se aconseja?",
#   "¿se detiene / se cambia / se acepta?" ............ ENSAYO (H0, H1, valor crítico, decisión)
#   "estimar", "entre qué valores", "máximo / mínimo
#    esperado", "con un X% de confianza" .............. INTERVALO (no lleva H0)
#   "¿cuántas unidades más...?" ........................ TAMAÑO DE MUESTRA (n)
#   "probabilidad de ... si en realidad es ..." ........ β o 1 − β
#   "¿sigue un modelo...?", "¿se ajusta...?" ........... CHI CUADRADO (bondad de ajuste)
#   "¿depende de...?", "¿difieren los porcentajes?" .... CHI CUADRADO (contingencia)
#   "recta", "por cada ... adicional", "en función de" . REGRESIÓN
#
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
#  H0 de una proporción:
#   control de rutina / recepción ("máximo 7% de fallas")  → optimista: H0 = cumple → H1: p > p0 → "derecha"
#   cambio / inversión ("solo si es menor al 8%")           → pesimista: H0 = no mejora → H1: p < p0 → "izquierda"
#  "¿cumple?" ................... ensayo_proporcion(p0, n, r, alfa, cola)       p0 = el % de la consigna
#  "estimar el %" ............... intervalo_proporcion(r, n, confianza, tipo)
#  "% que no cumple" (tabla) .... r = contar_debajo(tabla, valor)    →    intervalo_proporcion(r, n, confianza, tipo)
#                                 (contar_encima(tabla, valor) para "por encima de")
#  "¿cuántas más?" (error e) .... n_para_error_proporcion(r / n, e, confianza)   más = n nuevo − n que tenías
#  "probabilidad de ... si en realidad es X%"  →  β o 1 − β    (p* = ese X%, en la guía p1)
#                                 rc = valor_critico_proporcion(p0, n, alfa, cola)      misma cola que el ensayo
#                                 beta_proporcion(rc, n, p_estrella, cola)
#                                 pasa al RECHAZAR H0 (detectar, detener, cambiar) → 1 − β
#                                 pasa al NO rechazar (no detectar, aceptar)        → β
#
#  --- CHI CUADRADO ---
#  "¿sigue un modelo?" (tabla) .. bondad_ajuste(tabla, modelo, alfa)     modelo = "normal", "gamma", "lognormal",
#                                                                         "weibull", "gumbel_min", "gumbel_max"
#  con parámetros dados ......... bondad_ajuste(tabla, "normal", alfa, {"mu": valor, "sigma": valor})
#  probabilidades dadas/iguales . bondad_proporciones(categorias, observados, probabilidades, alfa)
#                                 probabilidades = None si son todas iguales, o [p1, p2, ...]
#  dos proporciones "¿difieren?". contingencia([[r1, r2], [n1 - r1, n2 - r2]], alfa)
#  dos proporciones con sospecha  comparar_proporciones(r1, n1, r2, n2, alfa, "derecha", nombres=("1", "2"))
#   ("mañana tiene menos que tarde")  grupo 1 = el que debería tener el % MÁS GRANDE
#  "prob. de detectar X% más" ... potencia_dos_proporciones(r1, n1, r2, n2, alfa, "derecha", diferencia, nombres)
#  "¿es exponencial?" ........... bondad_exponencial(tabla, alfa)    clases abiertas con None: [(None, 100, 55), ..., (130, None, 15)]
#  "¿depende de...?" ............ contingencia(tabla_doble_entrada, alfa)    tabla = [[fila 1], [fila 2], ...]
#
#  --- REGRESIÓN · x = la que explica, y = la que se explica ---
#  recta + validar + r² ......... regresion_simple(x, y, alfa)              x, y = listas
#  "¿baja/sube en más de V?" .... ensayo_pendiente(x, y, beta10, alfa, cola)   "baja más de 0,5" → beta10 = -0.5, "izquierda"
#  "contribución marginal" ...... intervalo_pendiente(x, y, confianza)
#  "fuerza de la relación" ...... intervalo_correlacion(x, y, confianza)
#  y PROMEDIO para x0 ........... estimar_media_regresion(x, y, x0, confianza)
#  y de UN caso con x0 .......... predecir_regresion(x, y, x0, confianza)

import _ruta
from formulas import *


# =====================================================================
#  3. RESOLUCIÓN
# =====================================================================

# a)


# b)


# c)

