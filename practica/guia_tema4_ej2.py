# =====================================================================
#  Guía de Problemas - Tema IV, problema 2 (aleación "Dural")
#  Comparación de desvíos de dos poblaciones (distribución F)
# =====================================================================
#
#  Datos de la consigna:
#    P (aleación propuesta): 13 piezas, desvío 0,06  -> va ARRIBA
#    A (material actual):    21 piezas, desvío 0,084 -> va ABAJO
#
#  Lo que decidí leyendo la consigna (punto a):
#    Quieren probar que P baja el desvío MÁS de un 20%:  σP / σA < 0,8
#    -> ψ0 = 0,8   cola izquierda   α = 0,10
# =====================================================================

import _ruta  # para que Python encuentre la carpeta formulas
from formulas.fisher import valor_f, cociente_varianzas, valor_critico, rechaza_h0

n_p, s_p = 13, 0.06
n_a, s_a = 21, 0.084

gl_num = n_p - 1   # 12 (P va arriba)
gl_den = n_a - 1   # 20 (A va abajo)

# --- Prueba de la tabla F (valores de la guía) ---
print("F(0.10; 12; 20) =", round(valor_f(0.10, gl_num, gl_den), 4), "  (guía: 0,4855)")
print("F(0.95; 12; 20) =", round(valor_f(0.95, gl_num, gl_den), 4), "  (guía: 2,2776)")
print("F(0.05; 12; 20) =", round(valor_f(0.05, gl_num, gl_den), 4), "  (guía: 0,3932)")

# --- Punto a) ---
j2 = cociente_varianzas(s_p, s_a)
j2c = valor_critico(0.8, 0.10, gl_num, gl_den, "izquierda")

print()
print("Punto a)")
print("  Cociente de la muestra j² =", round(j2, 4), "  -> j =", round(j2 ** 0.5, 4), "  (guía: j = 0,7143)")
print("  Línea j²c =", round(j2c, 4), "  -> jc =", round(j2c ** 0.5, 4), "  (guía: 0,3107 y 0,5574)")
print("  ¿Se rechaza H0?", rechaza_h0(j2, j2c, "izquierda"), "  (guía: no se rechaza)")
