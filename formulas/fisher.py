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
#    Notación:  muestra  j = S1/S2     población  ψ = σ1/σ2
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
#        -> σP / σA < 0,8   -> P arriba, ψ0 = 0,8
#    b) Si solo preguntan si las variabilidades son iguales,
#       poné arriba la de desvío más GRANDE -> trabajás con cola derecha.
#
#  VALOR CRÍTICO (la línea)
#    Te parás en el borde de H0 (ej: baja justo un 20%) y preguntás:
#    ¿qué cociente podría salirme por azar? La línea es el valor que
#    por azar solo cruzarías un α de las veces.
#      j²c = ψ0² · F
#    De qué lado va la línea, según lo que dice H1:
#      H1 "menor" -> cola izquierda -> F(α)
#      H1 "mayor" -> cola derecha   -> F(1 - α)
#    Si el cociente de la muestra cruza la línea -> se rechaza H0.
#
#  QUÉ DECIDÍS VOS / QUÉ CALCULA EL PROGRAMA
#    Vos: qué va arriba, ψ0, α y la cola (leyendo la consigna).
#    Programa: el valor F, el cociente, la línea y si la cruza o no.
# =====================================================================

from scipy.stats import f


# CUÁNDO: necesitás un valor de la tabla F.
# PARA QUÉ: reemplaza buscar en la tabla, ej: F(0,10 ; 12 ; 20) = 0,4855
#   probabilidad = área a la IZQUIERDA del valor (ej: 0.10)
#   gl_num = n - 1 de la muestra que va ARRIBA
#   gl_den = n - 1 de la muestra que va ABAJO
def valor_f(probabilidad, gl_num, gl_den):
    return f.ppf(probabilidad, gl_num, gl_den)


# CUÁNDO: ya tenés los desvíos muestrales de las dos poblaciones.
# PARA QUÉ: obtener el cociente de la muestra j² = S_arriba² / S_abajo²
def cociente_varianzas(s_arriba, s_abajo):
    return (s_arriba / s_abajo) ** 2


# CUÁNDO: tenés que decidir (hacer el ensayo de hipótesis).
# PARA QUÉ: obtener la línea j²c = ψ0² · F
#   psi0  = relación de DESVÍOS de la hipótesis (ej: 0.8; si es igualdad, 1)
#   alfa  = riesgo (ej: 0.10)
#   cola  = "izquierda" (H1 dice menor) o "derecha" (H1 dice mayor)
def valor_critico(psi0, alfa, gl_num, gl_den, cola):
    if cola == "izquierda":
        return psi0 ** 2 * valor_f(alfa, gl_num, gl_den)
    else:
        return psi0 ** 2 * valor_f(1 - alfa, gl_num, gl_den)


# CUÁNDO: ya tenés el cociente de la muestra y la línea.
# PARA QUÉ: saber si el cociente cruzó la línea.
#   True  -> se rechaza H0 (la diferencia no parece azar)
#   False -> no se rechaza H0 (puede ser azar, no se puede afirmar)
def rechaza_h0(cociente, critico, cola):
    if cola == "izquierda":
        return cociente <= critico
    else:
        return cociente >= critico
