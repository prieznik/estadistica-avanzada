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
#  2. AYUDA: qué función usar
# =====================================================================
#
#  COLA:  "derecha" (H1 >)  |  "izquierda" (H1 <)  |  "bilateral" (H1 ≠, solo promedios)
#  TIPO de intervalo:  "bilateral" (estimar)  |  "maximo"  |  "minimo"
#  Decimales con PUNTO (0.05). Porcentajes entre 0 y 1 (7% -> 0.07).
#  Tablas: [(desde, hasta, frecuencia), ...]
#
#  --- DATOS DE LA CONSIGNA ---
#  n, x, s = resumen_tabla(tabla, "Línea A")    n, media y desvío (con fórmulas)
#  media(lista), desvio(lista)                  si te dan los valores sueltos
#  contar_debajo(tabla, valor)                  cuántos quedan por debajo de un valor
#  contar_encima(tabla, valor)                  cuántos quedan por encima
#
#  --- FISHER (comparar variabilidad) ---
#  ensayo_varianzas(phi0, alfa, n_arriba, s_arriba, n_abajo, s_abajo, cola)
#        cuando Fisher ES la pregunta ("¿más regular?", "¿reduce el desvío?")
#        phi0 = 1 si solo "más/menos"; 0.8 si "reduce más de un 20%"
#
#  --- PROMEDIOS DE DOS GRUPOS (t de Student o Z) ---
#  metodo = metodo_para_medias(n1, x1, s1, n2, x2, s2)
#        paso previo (Fisher, α = 10%): devuelve "pool" o "welch"
#  ensayo_medias(metodo, delta0, alfa, n1, x1, s1, n2, x2, s2, cola, h=1)
#        delta0 casi siempre 0; con porcentaje: h = 1.10 ("10% más"), 0.90 ("10% menos")
#        si te dan los σ ("registros históricos"): metodo = "conocidos" (usa Z, sin Fisher)
#  intervalo_diferencia(metodo, confianza, n1, x1, s1, n2, x2, s2, tipo)
#        "diferencia mínima / máxima esperada"
#  h_limite(metodo, alfa, n1, x1, s1, n2, x2, s2, cola)
#        "diferencia porcentual mínima garantizada"
#
#  --- PROPORCIONES (Bernoulli / Binomial) ---
#  ensayo_proporcion(p0, n, r, alfa, cola)        ¿cumple? (rc, regla de decisión)
#  intervalo_proporcion(r, n, confianza, tipo)    estimar el %
#  beta_proporcion(rc, n, p1, cola)               prob. de NO detectar (detectar = 1 - β)
#  n_para_error_proporcion(p_hat, e, confianza)       cuántas unidades (error)
#  n_para_relacion_proporcion(p_hat, R, confianza)    cuántas unidades (relación)
#  reducir(valor, porcentaje)                     "reducir en un 30%" -> reducir(R, 0.30)
#  relacion_intervalo(A, B), error_intervalo(A, B)
#
#  --- CHI CUADRADO ---
#  bondad_ajuste(tabla, modelo, alfa, parametros=None)
#        modelo: "normal", "lognormal", "gamma", "weibull", "gumbel_min", "gumbel_max"
#        parametros = None si se estiman; {"mu": 20, "sigma": 2.5} si te los dan
#  contingencia(tabla_doble_entrada, alfa)
#
#  --- VALORES DE TABLA SUELTOS ---
#  valor_f(prob, gl_arriba, gl_abajo), valor_t(prob, gl), valor_chi2(prob, gl)

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
