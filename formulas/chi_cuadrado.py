# =====================================================================
#  CHI CUADRADO - ¿Los datos siguen un modelo? ¿Dos variables se relacionan?
# =====================================================================
#
#  QUÉ RESPONDE
#    1) BONDAD DE AJUSTE: ¿los datos de una tabla se comportan según un
#       modelo (Normal, Log-Normal, Gamma, Weibull, Gumbel)?
#    2) CONTINGENCIA: ¿dos clasificaciones son independientes?
#       (ej: preferencia de fragancia vs. local donde se vende)
#
#  SEÑALES EN LA CONSIGNA
#    "¿se puede verificar que la producción se ajusta a un modelo Gamma?"
#    "¿sigue el modelo Gumbel del Máximo?", "¿se comporta normalmente?"
#    -> bondad de ajuste
#    Tabla de doble entrada con conteos y "¿depende de...?",
#    "¿influye?", "¿difieren entre...?"  -> contingencia
#
#  LA IDEA
#    Comparás lo OBSERVADO (Fo, la tabla) con lo ESPERADO (Fe, lo que
#    debería haber si H0 fuera cierta):
#      χ² = suma de (Fo - Fe)² / Fe
#    Si los datos siguen el modelo, Fo y Fe se parecen y χ² da chico.
#    Si χ² da más grande que el valor de tabla, se rechaza H0.
#
#  CÓMO SE PLANTEA (siempre igual)
#    H0: "los datos siguen el modelo X"   (o "son independientes")
#    Cola SIEMPRE derecha. α típico = 5% si no lo dan.
#    Si NO se rechaza: "el modelo es un buen candidato" (no "se prueba").
#
#  COSAS QUE TENÉS QUE SABER
#    - χ² nunca da negativo (suma de cuadrados).
#    - Todas las Fe tienen que ser ≥ 5. Si no, se AMALGAMAN (juntan)
#      con la clase vecina. El programa lo hace solo, desde las puntas.
#    - El modelo cubre todo su dominio, así que se agregan clases en las
#      puntas con Fo = 0 ("x o menos", "x o más"), como en la guía.
#    - Grados de libertad:
#        bondad:       gl = k - 1 - p
#                      k = clases que quedan después de amalgamar
#                      p = parámetros ESTIMADOS de los datos (0 si te
#                          los dan como dato, 2 si los estimás)
#        contingencia: gl = (filas - 1) · (columnas - 1)
#    - Los parámetros se estiman "por momentos": con x̄ y S de la tabla.
#
#  MODELOS (y su dominio)
#    "normal"      -∞ a +∞    parámetros μ y σ
#    "lognormal"    0 a +∞    m y D (media y desvío del logaritmo)
#    "gamma"        0 a +∞    r (forma) y λ (tasa)
#    "weibull"      0 a +∞    w (forma) y b (escala)
#    "gumbel_min"  -∞ a +∞    θ (modo) y β (escala)
#    "gumbel_max"  -∞ a +∞    θ (modo) y β (escala)
#
#  QUÉ DECIDÍS VOS / QUÉ CALCULA EL PROGRAMA
#    Vos: qué modelo probar, si los parámetros son dato o se estiman, α,
#         y la conclusión en palabras.
#    Programa: parámetros, probabilidades, Fe, amalgamado, χ², gl y decisión.
# =====================================================================

import math
from scipy.stats import chi2, norm, lognorm, gamma, weibull_min, gumbel_l, gumbel_r
from scipy.optimize import brentq
from formulas.datos import n_agrupado, media_agrupada, desvio_agrupado
from formulas._formato import titulo, seccion, linea, flecha, fin

INF = float("inf")
EULER = 0.5772156649015329
DOMINIO = {
    "normal": -INF, "gumbel_min": -INF, "gumbel_max": -INF,
    "lognormal": 0, "gamma": 0, "weibull": 0,
}


# CUÁNDO: necesitás un valor de la tabla Chi cuadrado.
# PARA QUÉ: reemplaza la tabla, ej: χ²(0,95 ; 3) = 7,8147
def valor_chi2(probabilidad, gl):
    return float(chi2.ppf(probabilidad, gl))


# PARA QUÉ: χ² = suma de (Fo - Fe)² / Fe
def estadistico_chi2(fo, fe):
    return sum((o - e) ** 2 / e for o, e in zip(fo, fe))


# --- Estimar parámetros por momentos -----------------------------------

# CUÁNDO: el modelo no viene con parámetros dados -> se estiman.
# PARA QUÉ: los parámetros del modelo a partir de x̄ y S de la tabla.
# Devuelve un diccionario con los parámetros (y los imprime).
def estimar_parametros(modelo, clases):
    x = media_agrupada(clases)
    s = desvio_agrupado(clases)
    seccion("Paso 1 · Parámetros del modelo: no los dan, se estiman con x̄ y S (p = 2)")
    linea(f"x̄ = {x:.4f}   ·   S = {s:.4f}".replace(".", ","))
    if modelo == "normal":
        p = {"mu": x, "sigma": s}
    elif modelo == "lognormal":
        D = math.sqrt(math.log(1 + (s / x) ** 2))
        p = {"m": math.log(x / math.sqrt(1 + (s / x) ** 2)), "D": D}
    elif modelo == "gamma":
        lam = x / s ** 2
        p = {"r": x * lam, "lambda": lam}
    elif modelo == "weibull":
        cv = s / x
        w = brentq(lambda w: math.gamma(1 + 2 / w) / math.gamma(1 + 1 / w) ** 2 - 1 - cv ** 2, 0.05, 100)
        p = {"w": w, "b": x / math.gamma(1 + 1 / w)}
    elif modelo == "gumbel_min":
        beta = s * math.sqrt(6) / math.pi
        p = {"theta": x + EULER * beta, "beta": beta}
    elif modelo == "gumbel_max":
        beta = s * math.sqrt(6) / math.pi
        p = {"theta": x - EULER * beta, "beta": beta}
    else:
        raise ValueError(f"Modelo desconocido: {modelo}")
    linea("   ·   ".join(f"{k} = {v:.4f}" for k, v in p.items()).replace(".", ","))
    return p


# PARA QUÉ: la función de distribución acumulada F(x) del modelo.
def _acumulada(modelo, p, x):
    if x == INF:
        return 1.0
    if x == -INF:
        return 0.0
    if modelo == "normal":
        return norm.cdf(x, p["mu"], p["sigma"])
    if x <= 0 and DOMINIO[modelo] == 0:
        return 0.0
    if modelo == "lognormal":
        return lognorm.cdf(x, p["D"], scale=math.exp(p["m"]))
    if modelo == "gamma":
        return gamma.cdf(x, p["r"], scale=1 / p["lambda"])
    if modelo == "weibull":
        return weibull_min.cdf(x, p["w"], scale=p["b"])
    if modelo == "gumbel_min":
        return gumbel_l.cdf(x, p["theta"], p["beta"])
    return gumbel_r.cdf(x, p["theta"], p["beta"])


# PARA QUÉ: juntar clases vecinas hasta que todas tengan Fe ≥ 5.
# Empieza por las puntas (como el apunte) y después revisa el medio.
def amalgamar(etiquetas, fo, fe, detalle=False):
    et, fo, fe = list(etiquetas), list(fo), list(fe)
    grupos = [[(e, f)] for e, f in zip(etiquetas, fe)]

    def juntar(i, j):  # junta la clase j dentro de la i (vecinas)
        a, b = sorted((i, j))
        et[a] = f"{et[a].split(' a ')[0]} a {et[b].split(' a ')[-1]}"
        fo[a] += fo[b]
        fe[a] += fe[b]
        grupos[a] = grupos[a] + grupos[b]
        del et[b], fo[b], fe[b], grupos[b]

    while len(fe) > 1 and fe[0] < 5:
        juntar(0, 1)
    while len(fe) > 1 and fe[-1] < 5:
        juntar(len(fe) - 2, len(fe) - 1)
    while len(fe) > 1 and min(fe) < 5:
        i = fe.index(min(fe))
        vecino = i - 1 if i == len(fe) - 1 or (i > 0 and fe[i - 1] < fe[i + 1]) else i + 1
        juntar(i, vecino)
    if detalle:
        return et, fo, fe, grupos
    return et, fo, fe


def _num(x):
    if x == INF:
        return "+∞"
    if x == -INF:
        return "-∞"
    return f"{x:g}"


def _imprimir_tabla(nombre, etiquetas, fo, fe, probs=None):
    seccion(nombre)
    linea(f"{'Clase':<18}{'Fo':>8}" + (f"{'P(k)':>10}" if probs else "") + f"{'Fe':>10}")
    linea("-" * (36 + (10 if probs else 0)))
    for i, (e, o, f) in enumerate(zip(etiquetas, fo, fe)):
        txt = f"{e:<18}{o:>8g}"
        if probs:
            txt += f"{probs[i]:>10.4f}"
        linea((txt + f"{f:>10.2f}").replace(".", ","))
    linea("-" * (36 + (10 if probs else 0)))
    linea((f"{'Total':<18}{sum(fo):>8g}" + (" " * 10 if probs else "") + f"{sum(fe):>10.2f}").replace(".", ","))


# --- Bondad de ajuste --------------------------------------------------

# CUÁNDO: "¿se ajusta / sigue / se comporta según el modelo X?"
# PARA QUÉ: hace todo el contraste e imprime cada paso para la hoja.
#   clases     = la tabla, como en datos.py: [(desde, hasta, frecuencia), ...]
#   modelo     = "normal", "lognormal", "gamma", "weibull",
#                "gumbel_min" o "gumbel_max"
#   alfa       = riesgo (si no lo dan, 0.05)
#   parametros = None si se estiman (p = 2), o un diccionario si son dato
#                (p = 0). Ej: {"mu": 20, "sigma": 2.5}
# Devuelve True si se rechaza H0 (los datos NO siguen el modelo).
def bondad_ajuste(clases, modelo, alfa=0.05, parametros=None):
    if modelo not in DOMINIO:
        raise ValueError(f'modelo = "{modelo}" no existe. Usá: ' + ", ".join(DOMINIO))
    titulo(f"Bondad de ajuste (Chi cuadrado): modelo {modelo}")
    seccion("Hipótesis")
    linea(f"H0: los datos siguen el modelo {modelo}")
    linea("H1: no lo siguen")
    linea(f"Cola derecha   ·   α = {str(alfa).replace('.', ',')}")
    seccion("Justificación")
    linea("Prueba Chi cuadrado de bondad de ajuste: se comparan las frecuencias")
    linea("observadas (Fo) con las esperadas según el modelo (Fe = n · P(clase)).")
    if parametros is None:
        parametros = estimar_parametros(modelo, clases)
        p_estimados = len(parametros)
    else:
        seccion("Paso 1 · Parámetros del modelo: los da la consigna (p = 0)")
        linea(", ".join(f"{k} = {v}" for k, v in parametros.items()))
        p_estimados = 0

    # Clases completas: se agregan las puntas hasta el dominio del modelo
    tramos = [(a, b, f) for a, b, f in clases]
    minimo = DOMINIO[modelo]
    if tramos[0][0] > minimo:
        tramos.insert(0, (minimo, tramos[0][0], 0))
    tramos.append((tramos[-1][1], INF, 0))

    n = n_agrupado(clases)
    etiquetas = [f"{_num(a)} a {_num(b)}" for a, b, _ in tramos]
    fo = [f for _, _, f in tramos]
    acum = [(_acumulada(modelo, parametros, a), _acumulada(modelo, parametros, b)) for a, b, _ in tramos]
    probs = [fb - fa for fa, fb in acum]
    fe = [n * pr for pr in probs]

    seccion("Paso 2 · Agregar las puntas")
    linea(f"La tabla va de {_num(clases[0][0])} a {_num(clases[-1][1])}, pero el modelo {modelo} va de "
          f"{_num(minimo)} a +∞.")
    agregadas = [etiquetas[0]] if tramos[0][2] == 0 and tramos[0][0] == minimo and clases[0][0] > minimo else []
    agregadas.append(etiquetas[-1])
    linea("Se agregan las clases " + " y ".join(f'"{e}"' for e in agregadas)
          + " con Fo = 0 (en la muestra no hubo datos ahí).")

    seccion("Paso 3 · Probabilidad y Fe de cada clase")
    linea("P(clase) = F(hasta) - F(desde)     (F = acumulada del modelo)")
    linea(f"Fe = n · P(clase)                  (n = {n})")
    m = max(range(1, len(tramos) - 1), key=lambda t: fo[t]) if len(tramos) > 2 else 0
    a_, b_, _ = tramos[m]
    linea(f"Ejemplo, clase {etiquetas[m]}:")
    if modelo == "normal":
        mu, sg = parametros["mu"], parametros["sigma"]
        za, zb = (a_ - mu) / sg, (b_ - mu) / sg
        linea(f"   F({_num(b_)}) = Φ(({_num(b_)} - {mu:.2f}) / {sg:.2f}) = Φ({zb:.4f}) = {acum[m][1]:.4f}".replace(".", ","))
        linea(f"   F({_num(a_)}) = Φ(({_num(a_)} - {mu:.2f}) / {sg:.2f}) = Φ({za:.4f}) = {acum[m][0]:.4f}".replace(".", ","))
    else:
        linea(f"   F({_num(b_)}) = {acum[m][1]:.4f}    F({_num(a_)}) = {acum[m][0]:.4f}".replace(".", ","))
    linea(f"   P = {acum[m][1]:.4f} - {acum[m][0]:.4f} = {probs[m]:.4f}".replace(".", ","))
    linea(f"   Fe = {n} · {probs[m]:.4f} = {fe[m]:.2f}".replace(".", ","))
    _imprimir_tabla("Tabla con todas las clases", etiquetas, fo, fe, probs)

    et2, fo2, fe2, grupos = amalgamar(etiquetas, fo, fe, detalle=True)
    seccion("Paso 4 · Amalgamar: toda clase con Fe < 5 se junta con la vecina")
    juntadas = [g for g in grupos if len(g) > 1]
    if not juntadas:
        linea("Todas las Fe son ≥ 5: no hace falta juntar.")
    for g, e_new, f_new in zip(grupos, et2, fe2):
        if len(g) > 1:
            chicas = [f"{f:.2f}" for _, f in g if f < 5]
            linea(" + ".join(f"[{e}  Fe {f:.2f}]" for e, f in g).replace(".", ","))
            linea(f"   → {e_new}  Fe {f_new:.2f}   (porque {' y '.join(chicas)} < 5)".replace(".", ","))
    if juntadas:
        _imprimir_tabla("Tabla después de amalgamar", et2, fo2, fe2)
    seccion(f"k = clases que quedan = {len(fe2)}")

    chi = estadistico_chi2(fo2, fe2)
    k = len(fe2)
    gl = k - 1 - p_estimados
    critico = valor_chi2(1 - alfa, gl)
    rechaza = chi > critico
    seccion("Muestra")
    linea("χ² = Σ (Fo - Fe)² / Fe")
    linea("   = " + " + ".join(f"({o:g} - {e:.2f})²/{e:.2f}" for o, e in zip(fo2, fe2)).replace(".", ","))
    linea(f"   = {chi:.4f}".replace(".", ","))
    seccion("Valor crítico")
    linea("gl = k - 1 - p   (k = clases después de juntar, p = parámetros estimados)")
    linea(f"   = {k} - 1 - {p_estimados}")
    linea(f"   = {gl}")
    linea()
    linea("χ²c = χ²(1-α ; gl)")
    linea(f"    = χ²({1 - alfa:g} ; {gl})".replace(".", ","))
    linea(f"    = {critico:.4f}".replace(".", ","))
    seccion("CR (condición de rechazo)")
    linea(f"Si χ² ≥ {critico:.4f}  →  se rechaza H0".replace(".", ","))
    seccion("RD (regla de decisión)")
    linea(f"Si se rechaza H0  →  los datos no siguen el modelo {modelo}")
    linea(f"Si no se rechaza  →  el modelo {modelo} es un buen candidato")
    seccion("Decisión")
    linea(f"χ² = {chi:.4f}  {'≥' if rechaza else '<'}  {critico:.4f}".replace(".", ","))
    if rechaza:
        flecha(f"SE RECHAZA H0: los datos NO siguen el modelo {modelo}")
    else:
        flecha(f"NO se rechaza H0: el modelo {modelo} es un buen candidato")
    fin()
    return rechaza


# --- Contingencia ------------------------------------------------------

# CUÁNDO: tabla de doble entrada con conteos y "¿depende de...?",
#         "¿son independientes?", "¿difieren entre...?"
# PARA QUÉ: hace el contraste de independencia e imprime cada paso.
#   tabla = lista de filas, ej: [[32, 45, 23, 28], [14, 51, 15, 14]]
#   Fe de cada celda = total fila · total columna / total general
# Devuelve True si se rechaza H0 (las variables NO son independientes).
def contingencia(tabla, alfa=0.05):
    tot_fila = [sum(f) for f in tabla]
    tot_col = [sum(c) for c in zip(*tabla)]
    total = sum(tot_fila)
    esperados = [[tf * tc / total for tc in tot_col] for tf in tot_fila]
    titulo("Tabla de contingencia (Chi cuadrado)")
    seccion("Hipótesis")
    linea("H0: las dos clasificaciones son independientes")
    linea("H1: hay relación entre ellas")
    linea(f"Cola derecha   ·   α = {str(alfa).replace('.', ',')}")
    seccion("Esperados (Fe = total fila · total columna / total)")
    for fila in esperados:
        linea("  ".join(f"{e:9.4f}" for e in fila))
    if min(min(f) for f in esperados) < 5:
        linea("Ojo: hay celdas con Fe < 5. Habría que juntar filas o columnas.")
    fo = [o for fila in tabla for o in fila]
    fe = [e for fila in esperados for e in fila]
    chi = estadistico_chi2(fo, fe)
    gl = (len(tabla) - 1) * (len(tabla[0]) - 1)
    critico = valor_chi2(1 - alfa, gl)
    rechaza = chi > critico
    seccion("Muestra")
    linea("χ² = Σ (Fo - Fe)² / Fe")
    linea(f"   = {chi:.4f}".replace(".", ","))
    seccion("Valor crítico")
    linea("gl = (filas - 1) · (columnas - 1)")
    linea(f"   = ({len(tabla)} - 1) · ({len(tabla[0])} - 1)")
    linea(f"   = {gl}")
    linea()
    linea("χ²c = χ²(1-α ; gl)")
    linea(f"    = χ²({1 - alfa:g} ; {gl})".replace(".", ","))
    linea(f"    = {critico:.4f}".replace(".", ","))
    seccion("CR (condición de rechazo)")
    linea(f"Si χ² ≥ {critico:.4f}  →  se rechaza H0".replace(".", ","))
    seccion("RD (regla de decisión)")
    linea("Si se rechaza H0  →  hay relación entre las dos clasificaciones")
    seccion("Decisión")
    linea(f"χ² = {chi:.4f}  {'≥' if rechaza else '<'}  {critico:.4f}".replace(".", ","))
    flecha("SE RECHAZA H0: hay relación (no son independientes)" if rechaza
           else "NO se rechaza H0: no se puede asegurar que haya relación")
    fin()
    return rechaza
