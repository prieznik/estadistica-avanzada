# =====================================================================
#  FISHER - Comparar la variabilidad de dos poblaciones (distribución F)
# =====================================================================
#
#  QUÉ RESPONDE
#    ¿Una población es más variable (más dispersa, menos pareja) que otra?
#    No compara promedios: compara desvíos o varianzas.
#
#  SEÑALES EN LA CONSIGNA
#    "variabilidad", "desvío", "dispersión", "más parejo", "regularidad",
#    "reducir el desvío en un X%".
#    También es el PRIMER PASO del ejercicio de las tablas (A vs B):
#    antes de comparar medias hay que ver si las varianzas son iguales.
#
#  LA IDEA
#    Se DIVIDE (no se resta):   j² = S_arriba² / S_abajo²
#      cerca de 1 -> variabilidades parecidas
#      mayor a 1  -> la de arriba es más variable
#      menor a 1  -> la de arriba es más pareja
#    Notación:  muestra  j = S1/S2     población  φ = σ1/σ2
#
#    Aunque las dos poblaciones sean iguales, por azar el cociente casi
#    nunca da 1. La distribución F dice cuánto puede moverse por azar.
#
#  COSAS QUE TENÉS QUE SABER
#    - F nunca da negativo (es un cociente de cuadrados).
#    - No es simétrica: los valores de cola izquierda y derecha no son
#      "espejo" uno del otro.
#    - Depende de DOS grados de libertad: n - 1 de cada muestra.
#    - El ORDEN importa: F(12 ; 20) no es lo mismo que F(20 ; 12).
#      Los primeros gl son siempre los de la muestra que va ARRIBA.
#
#  QUÉ VA ARRIBA
#    a) Si la consigna afirma algo de una población, esa va arriba.
#       "el desvío de la PROPUESTA es menor en más de un 20% que el actual"
#        -> σP / σA < 0,8   -> P arriba, φ0 = 0,8
#    b) Si solo preguntan si las variabilidades son iguales,
#       poné arriba la de desvío más GRANDE -> trabajás con cola derecha.
#
#  VALOR CRÍTICO (la línea)
#    Te parás en el borde de H0 (ej: baja justo un 20%) y preguntás:
#    ¿qué cociente podría salirme por azar? La línea es el valor que
#    por azar solo cruzarías un α de las veces.
#      j²c = φ0² · F
#    De qué lado va la línea, según lo que dice H1:
#      H1 "menor" -> cola izquierda -> F(α)
#      H1 "mayor" -> cola derecha   -> F(1 - α)
#    Si el cociente de la muestra cruza la línea -> se rechaza H0.
#
#  QUÉ DECIDÍS VOS / QUÉ CALCULA EL PROGRAMA
#    Vos: qué va arriba, φ0, α y la cola (leyendo la consigna).
#    Programa: el valor F, el cociente, la línea y si la cruza o no.
# =====================================================================

from scipy.stats import f
from formulas._formato import titulo, seccion, linea, flecha, fin


def _n(x, dec=4):
    return f"{x:.{dec}f}".replace(".", ",")


# CUÁNDO: necesitás un valor de la tabla F.
# PARA QUÉ: reemplaza buscar en la tabla, ej: F(0,10 ; 12 ; 20) = 0,4855
#   probabilidad = área a la IZQUIERDA del valor (ej: 0.10)
#   gl_arriba = n - 1 de la muestra que va ARRIBA
#   gl_abajo = n - 1 de la muestra que va ABAJO
def valor_f(probabilidad, gl_arriba, gl_abajo):
    return float(f.ppf(probabilidad, gl_arriba, gl_abajo))


# CUÁNDO: ya tenés los desvíos muestrales de las dos poblaciones.
# PARA QUÉ: obtener el cociente de la muestra j² = S_arriba² / S_abajo²
def cociente_varianzas(s_arriba, s_abajo, mostrar=True):
    j2 = (s_arriba / s_abajo) ** 2
    if mostrar:
        print(f"Muestra: j² = S_arriba² / S_abajo² = {_n(s_arriba)}² / {_n(s_abajo)}² = {_n(j2)}"
              f"   (j = {_n(j2 ** 0.5)})")
    return j2


# CUÁNDO: tenés que decidir (hacer el ensayo de hipótesis).
# PARA QUÉ: obtener la línea j²c = φ0² · F
#   phi0  = relación de DESVÍOS de la hipótesis (ej: 0.8; si es igualdad, 1)
#   alfa  = riesgo (ej: 0.10)
#   cola  = "izquierda" (H1 dice menor) o "derecha" (H1 dice mayor)
def valor_critico(phi0, alfa, gl_arriba, gl_abajo, cola, mostrar=True):
    if cola not in ("derecha", "izquierda"):
        raise ValueError(f'cola = "{cola}" no existe. Usá "derecha" o "izquierda".')
    prob = alfa if cola == "izquierda" else 1 - alfa
    F = valor_f(prob, gl_arriba, gl_abajo)
    j2c = phi0 ** 2 * F
    if mostrar:
        etiqueta = "α" if cola == "izquierda" else "1-α"
        print(f"Valor crítico: j²c = φ0² · F({etiqueta} ; n_arriba-1 ; n_abajo-1)")
        print(f"   j²c = {_n(phi0, 2)}² · F({_n(prob, 2)} ; {gl_arriba} ; {gl_abajo}) "
              f"= {_n(phi0 ** 2)} · {_n(F)} = {_n(j2c)}   (jc = {_n(j2c ** 0.5)})")
    return j2c


# CUÁNDO: ya tenés el cociente de la muestra y la línea.
# PARA QUÉ: saber si el cociente cruzó la línea.
#   True  -> se rechaza H0 (la diferencia no parece azar)
#   False -> no se rechaza H0 (puede ser azar, no se puede afirmar)
def rechaza_h0(cociente, critico, cola, mostrar=True):
    rechaza = cociente <= critico if cola == "izquierda" else cociente >= critico
    if mostrar:
        signo = ("≤" if rechaza else ">") if cola == "izquierda" else ("≥" if rechaza else "<")
        print(f"{_n(cociente)} {signo} {_n(critico)} -> "
              + ("SE RECHAZA H0 (se puede afirmar H1)" if rechaza
                 else "NO se rechaza H0 (no hay pruebas suficientes para H1)"))
    return rechaza


# CUÁNDO: Fisher ES la pregunta ("¿la máquina nueva es más regular?",
#         "¿reduce el desvío en más de un 20%?").
# PARA QUÉ: hace todo el ensayo e imprime el bloque para la hoja.
#   phi0 = 1 si se pregunta solo "más/menos variable"; 0.8 si "reduce más de 20%"
#   la muestra "arriba" es la que nombra la frase.
def ensayo_varianzas(phi0, alfa, n_arriba, s_arriba, n_abajo, s_abajo, cola):
    if cola not in ("derecha", "izquierda"):
        raise ValueError(f'cola = "{cola}" no existe. Usá "derecha" o "izquierda".')
    s0, s1 = ("≤", ">") if cola == "derecha" else ("≥", "<")
    gl1, gl2 = n_arriba - 1, n_abajo - 1
    prob = alfa if cola == "izquierda" else 1 - alfa
    etiqueta = "α" if cola == "izquierda" else "1-α"
    F = valor_f(prob, gl1, gl2)
    j2c = valor_critico(phi0, alfa, gl1, gl2, cola, mostrar=False)
    j2 = cociente_varianzas(s_arriba, s_abajo, mostrar=False)
    rechaza = rechaza_h0(j2, j2c, cola, mostrar=False)

    titulo("Comparación de varianzas (F de Fisher)")
    seccion("Justificación")
    linea("Se usa la distribución F de Fisher-Snedecor porque se comparan")
    linea("las varianzas (desvíos) de dos poblaciones independientes.")
    seccion("Hipótesis")
    linea("φ = σ_arriba / σ_abajo")
    linea(f"H0: φ {s0} {_n(phi0, 2)}")
    linea(f"H1: φ {s1} {_n(phi0, 2)}")
    linea(f"Cola {cola}   ·   α = {_n(alfa, 2)}")
    seccion("Valor crítico")
    linea(f"j²c = φ0² · F({etiqueta} ; n_arriba-1 ; n_abajo-1)")
    linea(f"    = {_n(phi0, 2)}² · F({_n(prob, 2)} ; {gl1} ; {gl2})")
    linea(f"    = {_n(j2c)}")
    regla = "j² ≥ j²c" if cola == "derecha" else "j² ≤ j²c"
    seccion("Regla de decisión")
    linea(f"Si {regla} = {_n(j2c)}, se rechaza H0")
    seccion("Muestra")
    linea(f"j² = S_arriba² / S_abajo² = {_n(s_arriba)}² / {_n(s_abajo)}²")
    linea(f"   = {_n(j2)}")
    seccion("Decisión")
    if cola == "izquierda":
        signo = "≤" if rechaza else ">"
    else:
        signo = "≥" if rechaza else "<"
    linea(f"{_n(j2)} {signo} {_n(j2c)}")
    flecha("SE RECHAZA H0 (se puede afirmar H1)" if rechaza
           else "NO se rechaza H0 (no hay pruebas suficientes para H1)")
    fin()
    return rechaza
