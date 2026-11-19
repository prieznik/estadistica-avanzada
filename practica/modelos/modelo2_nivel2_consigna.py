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
#  ⚠ LOS 4 ERRORES QUE MÁS COMETO (leer antes de cada ejercicio)
#  1) ¿QUÉ TEMA ES? Mirá los DATOS, no la frase "por cada":
#     dos variables con UNIDADES DISTINTAS (horas y errores) ........ REGRESIÓN
#     misma variable, MISMOS individuos antes/después ............... APAREADAS
#     misma variable, dos GRUPOS distintos (A y B) .................. DOS PROMEDIOS
#     tabla filas × columnas con CANTIDADES de casos, "¿depende de?". CONTINGENCIA
#  2) H1 = LO QUE ME HACE ACTUAR
#     "¿se puede asegurar que X?" ............ H1 = X
#     control / recepción / "¿se acepta?" .... H1 = la ALARMA (p > p0) → "derecha"
#     cambio / inversión / "¿conviene?" ...... H1 = la MEJORA (p < p0) → "izquierda"
#  3) QUIÉN ES 1 Y QUIÉN ES 2 (promedios y apareadas)
#     1 = el que la frase dice que tiene MÁS → así la cola es "derecha"
#     "A resiste más que B" → 1 = A · "el curso aumentó" → 1 = después
#     "el curso redujo los errores" → 1 = antes (antes tenía más)
#     delta0 = el "más de N" de la frase (sin número → 0)
#  4) REGRESIÓN: QUIÉN ES x
#     x = lo que va después de "por cada" o de "en función de" · y = lo que responde
#     "por cada grado más, las ventas..." → x = temperatura, y = ventas
#     beta10 = el número con su signo: "aumenta más de 1,5" → 1.5, "derecha"
#                                      "disminuye más de 1,5" → -1.5, "izquierda"
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
ensayo_proporcion(0.08, 200, 9, 0.05, "izquierda")

# --- 2 b) ---
rc = valor_critico_proporcion(0.08, 200, 0.05, "izquierda")
beta_proporcion(rc, 200, 0.04, "izquierda")


# --- 2 c) ---
intervalo_proporcion(9, 200, 0.95, "maximo")


# --- 3 a) ---
ensayo_apareadas(antes, despues, 3, 0.05, "derecha", nombres=("Antes", "Despues"))


# --- 3 b) ---
intervalo_apareadas(antes, despues, 0.90, "bilateral", nombres=("Antes", "Despues"))

# Conclusión en palabras:
#


