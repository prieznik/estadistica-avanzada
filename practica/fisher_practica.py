import _ruta 
from formulas.datos import media_agrupada, desvio_agrupado, n_agrupado
from formulas.fisher import valor_f, cociente_varianzas, valor_critico, rechaza_h0

# (desde, hsata, frecuencia)
tabla_A = [(480,490,5),(490,500,15),(500,510,30),(510,520,15),(520,530,5)]
tabla_B = [(480,490,10),(490,500,15),(500,510,20),(510,520,15),(520,530,10)]

# calcular n, media y desvío de cada maquina 
n_A = n_agrupado(tabla_A)
n_B = n_agrupado(tabla_B)
media_A = media_agrupada(tabla_A)
media_B = media_agrupada(tabla_B)
desvio_A = desvio_agrupado(tabla_A)
desvio_B = desvio_agrupado(tabla_B)

print("Máquina A: n =", n_A, "media =", media_A, "desvío =", desvio_A)
print("Máquina B: n =", n_B, "media =", media_B, "desvío =", desvio_B)
