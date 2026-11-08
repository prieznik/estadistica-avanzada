# =====================================================================
#  ej02 lineas
# =====================================================================
#  Consigna:
#
#
#  Planteo en papel (antes de programar):
#    Herramienta:
#    Población 1 / qué cuenta p:
#    H0:
#    H1:
#    Cola:            α:
# =====================================================================

import _ruta
from formulas import *

'''
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
'''
# --- Datos de la consigna ---
tablaA= [(20,30,8),(30,40,25),(40,50,34),(50,60,10),(50,70,3)]
tablaB= [(20,30,6),(30,40,14),(40,50,20),(50,60,24),(50,70,16)]

nA= n_agrupado(tablaA)
xA= media_agrupada(tablaA)       
sA= desvio_agrupado(tablaA)

nB= n_agrupado(tablaB)
xB= media_agrupada(tablaB)
sB= desvio_agrupado(tablaB)

print("Máquina A: n =", nA, "media =", xA, "desvío =", sA)
print("Máquina B: n =", nB, "media =", xB, "desvío =", sB)

print("J2 =", cociente_varianzas(sB, sA))
print("J2c =", valor_critico(phi0=1, alfa=0.10, gl_arriba=nB-1, gl_abajo=nA-1, cola="derecha"))
rechaza_h0(cociente_varianzas(sB, sA), valor_critico(phi0=1, alfa=0.10, gl_arriba=nB-1, gl_abajo=nA-1, cola="derecha"), "derecha")
# --- a) ---


# Conclusión en palabras:
#
