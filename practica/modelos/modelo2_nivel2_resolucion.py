# =====================================================================
#  RESOLUCIÓN · modelo2_nivel2
#  Corré este archivo con ▶: imprime cada punto en formato hoja.
#  Abrilo DESPUÉS de intentarlo vos.
# =====================================================================
#  RESPUESTAS (para comparar):
#  1 a) Fisher previo: j² = 1,0026 < 1,2951 → Pool. H0: μN ≤ μA.
#       d = 1,60 ≥ dc = 1,1718 → se rechaza → el nuevo dura en promedio más que el actual.
#  1 b) h = 1,10: d* = 0,632 < d*c = 1,2318 → no se rechaza → no se aconseja el reemplazo
#       (no se puede asegurar que dure más de un 10% más).
#  1 c) h = 1,0417 → incremento mínimo garantizado: 4,17%.
#  1 d) χ² = 0,2702 < 5,9915 (gl = 2) → la Gamma es buena candidata.
#  1 e) r = 27 de 100 por debajo de 8 → entre 18,61% y 36,80% (95%).
#  2 a) Pesimista (inversión): H0: p ≥ 0,08, H1: p < 0,08, cola izquierda.
#       rc = 9 (Fb(9/200;0,08) = 0,0374 ≤ 0,05) y r = 9 → ENTRA (el rc cuenta) → se rechaza →
#       se aconseja cambiar de proveedor.
#  2 b) Potencia: 1 - β = 0,7192.
#  2 c) Porcentaje máximo: 7,72% (95%).
#  3 a) Apareadas (mismo operario): H0: μAntes - μDespués ≤ 3. d̄ = 4,625 ≥ dc = 4,3838 →
#       se rechaza → la capacitación reduce el tiempo promedio en más de 3 minutos.
#  3 b) Entre 3,24 y 6,01 minutos (90%).
# =====================================================================

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
from formulas import *

tablaA = [(0, 4, 10), (4, 8, 32), (8, 12, 30), (12, 16, 16), (16, 20, 8), (20, 24, 4)]
tablaN = [(0, 4, 5), (4, 8, 22), (8, 12, 33), (12, 16, 22), (16, 20, 12), (20, 24, 6)]
antes   = [52, 48, 55, 60, 47, 58, 51, 56]
despues = [47, 45, 49, 53, 46, 52, 48, 50]

# --- 1 a) Fisher previo + promedios (H1: μN > μA) ---
nA, xA, sA = resumen_tabla(tablaA, "Actual (A)")
nN, xN, sN = resumen_tabla(tablaN, "Nuevo (N)")
metodo = metodo_para_medias(nN, xN, sN, nA, xA, sA, nombres=("N", "A"))
ensayo_medias(metodo, 0, 0.05, nN, xN, sN, nA, xA, sA, "derecha", nombres=("N", "A"))

# --- 1 b) más de un 10% más -> h = 1.10 ---
ensayo_medias(metodo, 0, 0.05, nN, xN, sN, nA, xA, sA, "derecha", h=1.10, nombres=("N", "A"))

# --- 1 c) incremento porcentual mínimo garantizado ---
h_limite(metodo, 0.05, nN, xN, sN, nA, xA, sA, "derecha", nombres=("N", "A"))

# --- 1 d) bondad de ajuste Gamma para N ---
bondad_ajuste(tablaN, "gamma", 0.05)

# --- 1 e) % por debajo de 8 (mil horas) -> r y después intervalo bilateral ---
r = contar_debajo(tablaN, 8)
print("r (componentes nuevos con menos de 8.000 h) =", r)
intervalo_proporcion(r, nN, 0.95, "bilateral")

# --- 2 a) inversión -> pesimista: H0: p ≥ 0,08, H1: p < 0,08 (cola izquierda) ---
ensayo_proporcion(0.08, 200, 9, 0.05, "izquierda")

# --- 2 b) probabilidad de cambiar si p = 4% -> potencia 1 - β ---
rc = valor_critico_proporcion(0.08, 200, 0.05, "izquierda")
beta_proporcion(rc, 200, 0.04, "izquierda")

# --- 2 c) porcentaje MÁXIMO ---
intervalo_proporcion(9, 200, 0.95, "maximo")

# --- 3 a) apareadas: δ = μAntes - μDespués, H1: δ > 3 ---
ensayo_apareadas(antes, despues, 3, 0.05, "derecha", nombres=("Antes", "Después"))

# --- 3 b) intervalo 90% ---
intervalo_apareadas(antes, despues, 0.90, "bilateral", nombres=("Antes", "Después"))
