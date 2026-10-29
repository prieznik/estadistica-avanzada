# =====================================================================
#  DATOS - Sacar n, media, desvío y proporción de la consigna
# =====================================================================
#
#  QUÉ RESPONDE
#    Este archivo no responde ninguna pregunta del ejercicio: prepara
#    los números que después usan todos los demás temas.
#    Todo ejercicio necesita, para cada población: n, media y desvío.
#
#  CÓMO VIENEN LOS DATOS EN LA CONSIGNA
#    - Valores sueltos (ej: 5,01 - 5,11 - 5,08 ...)   -> media, desvio
#    - Tabla con intervalos y frecuencias             -> *_agrupado
#    - "con un desvío de 0,084" / "media de 4,2"      -> no calcular nada,
#                                                       escribirlos tal cual
#    - "de 95 unidades, 8 tienen fallas"              -> proporcion
#
#  COSAS QUE TENÉS QUE SABER
#    - Estas funciones dan valores MUESTRALES: x̄ y S.
#    - μ y σ (poblacionales) NO se calculan. Pistas para reconocerlos:
#        "se sabe", "históricamente", "el proceso tiene", "el fabricante
#        asegura"  -> poblacional (μ, σ)
#        "en una muestra de n piezas se obtuvo"  -> muestral (x̄, S)
#    - El desvío se calcula dividiendo por (n - 1), no por n.
#    - En Python los decimales van con PUNTO: 0.084, no 0,084.
#
#  QUÉ DECIDÍS VOS / QUÉ CALCULA EL PROGRAMA
#    Vos: qué dato es de qué población, y si es muestral o poblacional.
#    Programa: las cuentas.
# =====================================================================


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
