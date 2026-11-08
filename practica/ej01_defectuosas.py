# =====================================================================
#  ej01_defectuosas
# =====================================================================
#  Consigna:
''' Un proceso especifica un porcentaje de piezas defectuosas máximo del 5%. Se revisan 120 piezas y 9 son defectuosas.
a) Con un riesgo del 5%, ¿cumple la especificación?
b) Con un 95% de confianza, estimá el porcentaje de piezas en buen estado de toda la producción.'''
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

# ayuda()   # descomentá esta línea si no te acordás qué funciones hay

'''
PROPORCIONES (Bernoulli / Binomial)
  ensayo_proporcion(p0, n, r, alfa, cola)     ¿cumple? (te da rc y decide)
  intervalo_proporcion(r, n, confianza, tipo) estimar el %
        tipo = "bilateral", "maximo" o "minimo"
  beta_proporcion(rc, n, p1, cola)            prob. de NO detectar (detectar = 1 - β)
  n_para_error_proporcion(p_hat, e, confianza)       cuántas unidades (error)
  n_para_relacion_proporcion(p_hat, R, confianza)    cuántas unidades (relación)
  reducir(valor, porcentaje)                  "reducir en un 30%" -> reducir(R, 0.30)
  relacion_intervalo(A, B), error_intervalo(A, B)
'''

# --- a) ---
# calcular r critico
ensayo_proporcion(p0=0.05, n=120, r=9, alfa=0.05, cola="derecha")
intervalo_proporcion(r=111, n=120, confianza=0.95, tipo="bilateral")

# Conclusión en palabras:
#
