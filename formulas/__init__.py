# =====================================================================
#  TODO EL KIT CON UN SOLO IMPORT
# =====================================================================
#
#  En cualquier ejercicio de practica/, arriba de todo:
#
#      import _ruta
#      from formulas import *
#
#  Y ya tenés todas las funciones. Si no te acordás qué hay, escribí:
#
#      ayuda()
#
#  y te muestra la lista, ordenada por tema, con para qué sirve cada una.
# =====================================================================

from formulas.datos import (
    media, desvio, n_agrupado, media_agrupada, desvio_agrupado,
    varianza_desde_desvio, desvio_desde_varianza, proporcion,
    contar_debajo, contar_encima,
)
from formulas.hipotesis import planteo
from formulas.fisher import valor_f, cociente_varianzas, valor_critico, rechaza_h0
from formulas.medias import (
    metodo_para_medias, ensayo_medias, intervalo_diferencia, h_limite,
    n_para_error_medias, diferencias_apareadas, valor_t,
    desvio_amalgamado, error_estandar, grados_libertad,
    valor_critico_diferencia, rechaza_h0_diferencia, diferencia_muestral,
)
from formulas.proporciones import (
    ensayo_proporcion, intervalo_proporcion, beta_proporcion,
    n_ensayo_proporcion, n_para_error_proporcion, n_para_relacion_proporcion,
    error_intervalo, relacion_intervalo, reducir,
    valor_critico_proporcion, rechaza_h0_proporcion, alfa_a_posteriori, Gb, Fb,
)
from formulas.chi_cuadrado import bondad_ajuste, contingencia, valor_chi2, estimar_parametros


_AYUDA = """
=============================== KIT ===============================

DATOS DE LA CONSIGNA
  n_agrupado(tabla)            n de una tabla con frecuencias
  media_agrupada(tabla)        media de una tabla
  desvio_agrupado(tabla)       desvío de una tabla
  media(lista), desvio(lista)  si te dan los valores sueltos
  contar_debajo(tabla, valor)  cuántos datos quedan por debajo de un valor
  contar_encima(tabla, valor)  cuántos quedan por encima

  La tabla se carga así: [(desde, hasta, frecuencia), ...]

HIPÓTESIS
  planteo("μB - μA", ">", 0)   te escribe H0, H1 y te devuelve la cola

FISHER (comparar variabilidad)
  valor_critico(phi0, alfa, gl_arriba, gl_abajo, cola)   la línea j²c
  cociente_varianzas(s_arriba, s_abajo)                  j² de la muestra
  rechaza_h0(j2, j2c, cola)                              True / False

PROMEDIOS DE DOS GRUPOS (t de Student o Z)
  metodo_para_medias(n1, x1, s1, n2, x2, s2)
        paso previo de Fisher: te devuelve "pool" o "welch"
  ensayo_medias(metodo, delta0, alfa, n1, x1, s1, n2, x2, s2, cola, h=1)
        el ensayo completo (con porcentaje: h = 1.10, etc.)
        si te dan los σ: metodo = "conocidos" (usa Z)
  intervalo_diferencia(metodo, confianza, n1, x1, s1, n2, x2, s2, tipo)
        tipo = "minimo", "maximo" o "bilateral"
  h_limite(metodo, alfa, n1, x1, s1, n2, x2, s2, cola)
        porcentaje mínimo garantizado (h)

PROPORCIONES (Bernoulli / Binomial)
  ensayo_proporcion(p0, n, r, alfa, cola)     ¿cumple? (te da rc y decide)
  intervalo_proporcion(r, n, confianza, tipo) estimar el %
        tipo = "bilateral", "maximo" o "minimo"
  beta_proporcion(rc, n, p1, cola)            prob. de NO detectar (detectar = 1 - β)
  n_para_error_proporcion(p_hat, e, confianza)       cuántas unidades (error)
  n_para_relacion_proporcion(p_hat, R, confianza)    cuántas unidades (relación)
  reducir(valor, porcentaje)                  "reducir en un 30%" -> reducir(R, 0.30)
  relacion_intervalo(A, B), error_intervalo(A, B)

CHI CUADRADO
  bondad_ajuste(tabla, modelo, alfa, parametros=None)
        modelo = "normal", "lognormal", "gamma", "weibull",
                 "gumbel_min" o "gumbel_max"
        parametros = None si se estiman; {"mu": 20, "sigma": 2.5} si te los dan
  contingencia(tabla_doble_entrada, alfa)

TABLAS (si necesitás un valor suelto)
  valor_f(prob, gl1, gl2), valor_t(prob, gl), valor_chi2(prob, gl)

Recordá: decimales con PUNTO (0.05) y porcentajes entre 0 y 1 (7% -> 0.07).
====================================================================
"""


def ayuda():
    print(_AYUDA)
