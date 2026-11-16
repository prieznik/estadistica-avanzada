# =====================================================================
#  RESOLUCIÓN · modelo3_nivel3
#  Corré este archivo con ▶: imprime cada punto en formato hoja.
#  Abrilo DESPUÉS de intentarlo vos.
# =====================================================================
#  RESPUESTAS (para comparar):
#  1 a) Fisher como pregunta: H0: σN ≥ 0,80·σA, H1: σN < 0,80·σA, cola izquierda, α = 10%.
#       j² = 0,1332 ≤ j²c = 0,2671 → se rechaza → se aconseja adoptar el método nuevo.
#  1 b) Paso previo: j² = 7,5086 ≥ 2,3961 → Welch (gl = 14). Bilateral: d = -0,3167 queda
#       dentro de [-1,7253 ; 1,7253] → no se rechaza → no se puede asegurar que difieran.
#  1 c) Entre -2,04 y 1,41 minutos (incluye el 0: coherente con b).
#  2 a) Consistencia: χ² = 5,2979 ≥ 3,8415 (gl = 1) → se rechaza → el % de defectuosos
#       difiere entre turnos (tarde 11,9% vs mañana 5%).
#  2 b) Independencia: χ² = 7,5031 < 9,4877 (gl = 4) → no se rechaza → no se puede asegurar
#       que la calidad dependa del turno.
#  3 a) ŷ = 141,1032 - 0,7565·x → por cada hora más, 0,76 minutos menos por unidad.
#  3 b) |t_obs| = 15,1582 > t(0,95;8) = 1,8595 → modelo válido; r = -0,9830.
#  3 c) H0: β1 ≥ -0,6; b1 = -0,7565 ≤ b1c = -0,6928 → se rechaza → sí, bajan más de 0,6.
#  3 d) ρ entre -0,9961 y -0,9274; ρ² entre 86,01% y 99,23% (95%).
#  3 e) Entre 110,19 y 111,49 minutos en promedio.
#  3 f) Entre 108,72 y 112,96 minutos. Es más ancho porque predice UN empleado (suma la
#       variabilidad individual, el "1 +" dentro de la raíz), no el promedio.
#  4 a) H0: p ≤ 0,03 (optimista, control). α = Gb(6/80 ; 0,03) = 0,0333.
#  4 b) 1 - β = 1 - Fb(5/80 ; 0,08) = 0,6250.
# =====================================================================

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from formulas import *

actual = [24.1, 26.8, 22.5, 28.9, 25.3, 21.7, 27.6, 23.8, 29.4, 24.9, 26.2, 22.0]
nuevo  = [24.6, 25.3, 23.9, 26.1, 24.8, 25.7, 23.5, 26.4, 25.0, 24.2]
turnos_2 = [[9, 19], [171, 141]]
turnos_3 = [[150, 24, 6], [128, 22, 10], [95, 12, 13]]
horas   = [30, 32, 35, 36, 38, 40, 42, 44, 45, 48]
minutos = [118, 117, 114, 115, 112, 110, 111, 108, 107, 104]

nA, xA, sA = resumen_lista(actual, "Actual (A)")
nN, xN, sN = resumen_lista(nuevo, "Nuevo (N)")

# --- 1 a) Fisher ES la pregunta: σN < 0,80·σA -> φ0 = 0,8, cola izquierda, α = 10% ---
ensayo_varianzas(0.8, 0.10, nN, sN, nA, sA, "izquierda", nombres=("N", "A"))

# --- 1 b) paso previo (α = 10%) + medias bilateral ---
metodo = metodo_para_medias(nN, xN, sN, nA, xA, sA, nombres=("N", "A"))
ensayo_medias(metodo, 0, 0.05, nN, xN, sN, nA, xA, sA, "bilateral", nombres=("N", "A"))

# --- 1 c) intervalo bilateral 95% ---
intervalo_diferencia(metodo, 0.95, nN, xN, sN, nA, xA, sA, "bilateral", nombres=("N", "A"))

# --- 2 a) dos proporciones -> prueba de consistencia (Chi cuadrado) ---
contingencia(turnos_2, 0.05)

# --- 2 b) independencia ---
contingencia(turnos_3, 0.05)

# --- 3 a) b) recta + validación ---
regresion_simple(horas, minutos, 0.05, nombres=("Horas", "Minutos"))

# --- 3 c) β1 < -0,6 -> cola izquierda ---
ensayo_pendiente(horas, minutos, -0.6, 0.05, "izquierda")

# --- 3 d) fuerza de la relación (ρ) y % explicado (ρ²) ---
intervalo_correlacion(horas, minutos, 0.95)

# --- 3 e) PROMEDIO para x0 = 40 ---
estimar_media_regresion(horas, minutos, 40, 0.95)

# --- 3 f) UN empleado con x0 = 40 -> predicción ---
predecir_regresion(horas, minutos, 40, 0.95)

# --- 4 a) H0: p ≤ 0,03 (optimista, control). α = Gb(rc/n ; p0) ---
print("4 a) α = Gb(6/80 ; 0,03) =", round(Gb(6, 80, 0.03), 4))

# --- 4 b) potencia: 1 - β con p1 = 0,08 ---
beta_proporcion(6, 80, 0.08, "derecha")
