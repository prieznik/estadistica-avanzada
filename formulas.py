# =====================================================================
#  FORMULAS - Kit de funciones básicas para Estadística Aplicada
# =====================================================================
#
#  Este archivo tiene SOLO funciones, sin datos de ningún ejercicio.
#  Los ejercicios van en otros archivos y las traen con un import:
#
#      from formulas import media_agrupada, desvio_agrupado
#
#  Regla: las funciones calculan, vos pensás. Ninguna función decide
#  hipótesis, colas ni qué población es cuál.
#
#  Recordatorio: en Python los decimales van con PUNTO (0.084, no 0,084).
# =====================================================================

from scipy.stats import f


# ---------------------------------------------------------------------
#  KIT 1: SACAR DATOS DE MUESTRAS
# ---------------------------------------------------------------------
#
#  Todo ejercicio necesita, para cada población: n, media y desvío.
#  Según cómo vengan los datos en la consigna:
#
#   - Valores sueltos (ej: 5,01 - 5,11 - 5,08 ...)  -> media, desvio
#   - Tabla con intervalos y frecuencias            -> *_agrupado
#   - Media y desvío ya dados ("con un desvío de...") -> no calcular nada,
#                                                      escribirlos tal cual
#
#  Ojo: estas funciones dan valores MUESTRALES (x̄, S).
#  μ y σ (poblacionales) no se calculan: te los dan como dato
#  ("se sabe", "históricamente") o son el valor de la hipótesis.
# ---------------------------------------------------------------------


# --- Valores sueltos -------------------------------------------------

# CUÁNDO: la consigna te da una lista de valores medidos uno por uno.
# PARA QUÉ: obtener la media muestral x̄.
# Fórmula: x̄ = (suma de los valores) / n
def media(valores):
    return sum(valores) / len(valores)


# CUÁNDO: la consigna te da una lista de valores medidos uno por uno.
# PARA QUÉ: obtener el desvío muestral S.
# Fórmula: S = raíz( suma de (valor - x̄)² / (n - 1) )
def desvio(valores):
    x = media(valores)
    suma = sum((v - x) ** 2 for v in valores)
    return (suma / (len(valores) - 1)) ** 0.5


# --- Tablas agrupadas (intervalos + frecuencias) ---------------------
#
#  La tabla se carga como una lista de (desde, hasta, frecuencia):
#
#      tabla = [
#          (100, 150, 17),
#          (150, 200, 51),
#      ]
#
#  Como no sabés el valor exacto de cada dato, se supone que todos
#  los datos de un intervalo valen su punto medio (marca de clase).

# CUÁNDO: te dan una tabla con intervalos y frecuencias.
# PARA QUÉ: obtener n (la cantidad total de datos) = suma de frecuencias.
def n_agrupado(clases):
    return sum(f for desde, hasta, f in clases)


# CUÁNDO: te dan una tabla con intervalos y frecuencias.
# PARA QUÉ: obtener la media muestral x̄.
# Fórmula: x̄ = suma de (marca de clase × frecuencia) / n
def media_agrupada(clases):
    n = n_agrupado(clases)
    suma = sum((desde + hasta) / 2 * f for desde, hasta, f in clases)
    return suma / n


# CUÁNDO: te dan una tabla con intervalos y frecuencias.
# PARA QUÉ: obtener el desvío muestral S.
# Fórmula: S = raíz( suma de (marca - x̄)² × frecuencia / (n - 1) )
def desvio_agrupado(clases):
    n = n_agrupado(clases)
    x = media_agrupada(clases)
    suma = sum(((desde + hasta) / 2 - x) ** 2 * f for desde, hasta, f in clases)
    return (suma / (n - 1)) ** 0.5


# --- Pasar de desvío a varianza y al revés ---------------------------

# CUÁNDO: tenés el desvío y la fórmula pide la varianza.
# PARA QUÉ: varianza = desvío²
def varianza_desde_desvio(desvio):
    return desvio ** 2


# CUÁNDO: tenés la varianza y la consigna o la fórmula pide el desvío.
# PARA QUÉ: desvío = raíz(varianza)
def desvio_desde_varianza(varianza):
    return varianza ** 0.5


# --- Proporciones (conteos) ------------------------------------------

# CUÁNDO: la consigna cuenta casos, ej: "de 95 unidades, 8 tienen fallas".
# PARA QUÉ: obtener la proporción muestral p̂ = r / n.
# Ojo con qué cuenta r: si preguntan por las unidades BUENAS,
# r = 95 - 8 = 87, no 8.
def proporcion(r, n):
    return r / n


# ---------------------------------------------------------------------
#  KIT 2: BUSCAR VALORES EN TABLAS
# ---------------------------------------------------------------------
#
#  Reemplazan buscar a mano en las tablas del cuadernillo.
#  "probabilidad" es siempre el área que queda a la IZQUIERDA del valor.
# ---------------------------------------------------------------------

# CUÁNDO: comparar varianzas o desvíos de DOS poblaciones (Tema IV).
# PARA QUÉ: obtener el valor de la tabla F, ej: F(0,10 ; 12 ; 20) = 0,4855
#   probabilidad = área a la izquierda (ej: 0.10)
#   gl_num = n - 1 de la muestra que va ARRIBA (numerador)
#   gl_den = n - 1 de la muestra que va ABAJO (denominador)
def valor_f(probabilidad, gl_num, gl_den):
    return f.ppf(probabilidad, gl_num, gl_den)
