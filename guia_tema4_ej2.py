# =====================================================================
#  Guía de Problemas - Tema IV, problema 2 (aleación "Dural")
#  Comparación de desvíos de dos poblaciones (distribución F)
# =====================================================================
#
#  Datos de la consigna:
#    P (aleación propuesta): 13 piezas, desvío 0,06  -> va ARRIBA -> gl = 12
#    A (material actual):    21 piezas, desvío 0,084 -> va ABAJO  -> gl = 20
#
#  Por ahora solo probamos que valor_f dé los mismos números que la guía.
# =====================================================================

from formulas import valor_f

n_p = 13
n_a = 21

gl_num = n_p - 1   # 12
gl_den = n_a - 1   # 20

# Punto a): la guía usa F(0,10 ; 12 ; 20) = 0,4855
print("Punto a)  F(0.10; 12; 20) =", round(valor_f(0.10, gl_num, gl_den), 4), "  (guía: 0,4855)")

# Punto d): la guía usa F(0,95 ; 12 ; 20) = 2,2776 y F(0,05 ; 12 ; 20) = 0,3932
print("Punto d)  F(0.95; 12; 20) =", round(valor_f(0.95, gl_num, gl_den), 4), "  (guía: 2,2776)")
print("Punto d)  F(0.05; 12; 20) =", round(valor_f(0.05, gl_num, gl_den), 4), "  (guía: 0,3932)")
