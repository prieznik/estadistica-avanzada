# =====================================================================
#  RESOLUCIÓN · modelo1_nivel1
#  Corré este archivo con ▶: imprime cada punto en formato hoja.
#  Abrilo DESPUÉS de intentarlo vos.
# =====================================================================
#  RESPUESTAS (para comparar):
#  1 a) Fisher previo: j² = 1,0043 < 1,2951 → Pool. H0: μB ≤ μA, cola derecha.
#       d = 4,6 ≥ dc = 2,7937 → se rechaza → la marca B dura en promedio más que la A.
#  1 b) A = 2,4263 → con 90% de confianza B dura en promedio como mínimo 242,63 h más que A.
#  1 c) χ² = 0,3807 < χ²(0,95;2) = 5,9915 → la Normal es buena candidata para A.
#  2 a) Optimista (control de rutina): H0: p ≤ 0,04. rc = 11, r = 9 → no se rechaza →
#       no se detiene el proceso (no hay pruebas de que supere el 4%).
#  2 b) Entre 2,78% y 11,08% (95%).
#  2 c) n = 543 → 543 - 150 = 393 piezas más.
#  3 a) ŷ = 18,9214 - 0,5091·x → por cada hora más de capacitación, 0,51 errores menos.
#  3 b) |t_obs| = 9,2449 > t(0,95;6) = 1,9432 → hay relación lineal; r = -0,9666 (fuerte).
#  3 c) r² = 0,9344 → el 93,44%.
#  3 d) Entre 9,90 y 11,65 errores en promedio (95%).
# =====================================================================

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from formulas import *

tablaA = [(40, 50, 6), (50, 60, 18), (60, 70, 34), (70, 80, 26), (80, 90, 12), (90, 100, 4)]
tablaB = [(40, 50, 3), (50, 60, 10), (60, 70, 28), (70, 80, 32), (80, 90, 19), (90, 100, 8)]
horas   = [10, 12, 15, 18, 20, 22, 25, 28]
errores = [14, 12, 12, 9, 10, 7, 7, 4]

# --- 1 a) Fisher previo + promedios (H1: μB > μA) ---
nA, xA, sA = resumen_tabla(tablaA, "Marca A")
nB, xB, sB = resumen_tabla(tablaB, "Marca B")
metodo = metodo_para_medias(nB, xB, sB, nA, xA, sA, nombres=("B", "A"))
ensayo_medias(metodo, 0, 0.05, nB, xB, sB, nA, xA, sA, "derecha", nombres=("B", "A"))

# --- 1 b) diferencia mínima, 90% ---
intervalo_diferencia(metodo, 0.90, nB, xB, sB, nA, xA, sA, "minimo", nombres=("B", "A"))

# --- 1 c) bondad de ajuste Normal para A ---
bondad_ajuste(tablaA, "normal", 0.05)

# --- 2 a) control de rutina -> optimista: H0: p ≤ 0,04 ---
ensayo_proporcion(0.04, 150, 9, 0.05, "derecha")

# --- 2 b) estimar el % -> bilateral ---
A, B = intervalo_proporcion(9, 150, 0.95, "bilateral")

# --- 2 c) n para error 2% ---
n_para_error_proporcion(9 / 150, 0.02, 0.95)

# --- 3 a) b) c) recta, validación y r² ---
regresion_simple(horas, errores, 0.05, nombres=("Horas", "Errores"))

# --- 3 d) promedio para x0 = 16 ---
estimar_media_regresion(horas, errores, 16, 0.95)
