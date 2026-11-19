# =====================================================================
#  REGRESIÓN LINEAL SIMPLE (Tema VII de la guía)
# =====================================================================
#
#  QUÉ RESPONDE
#    ¿Hay relación lineal entre x e y? ¿Cuánto cambia y por cada unidad
#    de x? ¿Qué y espero para un x dado?
#
#  SEÑALES EN LA CONSIGNA
#    "recta de mínimos cuadrados", "modelo de regresión", "en función de",
#    "validar el modelo", "coeficiente de correlación", "qué porcentaje se
#    explica", "por cada ... adicional", "estimar el promedio para x = ...",
#    "intervalo de predicción".
#
#  QUÉ ES x Y QUÉ ES y
#    y = la variable que se quiere explicar ("los minutos de producción
#        en función de las horas" -> y = minutos, x = horas).
#
#  NOTACIÓN (igual que la guía, Tema VII problema 12)
#    ŷ = b0 + b1·x     b1 = pendiente (contribución marginal)
#    S = desvío del modelo   Sb1 = desvío de b1   r = correlación
#    gl = n - 2
#
#  LAS FUNCIONES
#    regresion_simple(x, y, alfa)                 recta + validación + r²
#    ensayo_pendiente(x, y, beta10, alfa, cola)   "¿disminuye en más de 1?"
#    intervalo_pendiente(x, y, confianza)         contribución marginal
#    intervalo_correlacion(x, y, confianza)       fuerza de la relación (ρ y ρ²)
#    estimar_media_regresion(x, y, x0, confianza)    y PROMEDIO para x0
#    predecir_regresion(x, y, x0, confianza)         y de UN caso para x0
#    (tipo = "bilateral", "minimo" o "maximo" en las de intervalos)
# =====================================================================

import math
from scipy.stats import t, norm
from formulas._formato import titulo, seccion, linea, flecha, fin


def _n(x, dec=4):
    return f"{x:.{dec}f}".replace(".", ",")


def _g(v):
    return f"{v:g}".replace(".", ",")


def _p(prob):
    return f"{prob:g}".replace(".", ",")


def _sumas(x, y):
    if len(x) != len(y):
        raise ValueError(f"x tiene {len(x)} valores e y tiene {len(y)}: tienen que ser iguales.")
    n = len(x)
    sx, sy = sum(x), sum(y)
    sx2 = sum(v * v for v in x)
    sy2 = sum(v * v for v in y)
    sxy = sum(a * b for a, b in zip(x, y))
    xm, ym = sx / n, sy / n
    sxx = sx2 - n * xm ** 2
    syy = sy2 - n * ym ** 2
    sxy_c = sxy - n * xm * ym
    b1 = sxy_c / sxx
    b0 = ym - b1 * xm
    s = math.sqrt((sy2 - b0 * sy - b1 * sxy) / (n - 2))
    sb1 = s / math.sqrt(sxx)
    r = sxy_c / math.sqrt(sxx * syy)
    return dict(n=n, sx=sx, sy=sy, sx2=sx2, sy2=sy2, sxy=sxy, xm=xm, ym=ym,
                sxx=sxx, syy=syy, b1=b1, b0=b0, s=s, sb1=sb1, r=r, gl=n - 2)


def _recta(c):
    signo = "+" if c["b1"] >= 0 else "-"
    return f"ŷ = {_n(c['b0'])} {signo} {_n(abs(c['b1']))} · x"


# CUÁNDO: "hallar la recta", "construir el modelo", "validar el modelo",
#         "¿qué porcentaje se explica?".
# PARA QUÉ: imprime sumas, b1, b0, la recta, S, Sb1, r, r² y el ensayo
#   H0: β1 = 0 (validación), como la guía. Devuelve un diccionario.
def regresion_simple(x, y, alfa=0.05, nombres=("x", "y")):
    c = _sumas(x, y)
    nx, ny = nombres
    n = c["n"]
    titulo("Regresión lineal simple")
    seccion("Variables")
    linea(f"x = {nx}   (explicativa)      y = {ny}   (a explicar)")
    seccion("Sumas")
    linea(f"n = {n}   Σx = {_g(c['sx'])}   x̄ = {_n(c['xm'])}   Σx² = {_g(c['sx2'])}")
    linea(f"Σy = {_g(c['sy'])}   ȳ = {_n(c['ym'])}   Σy² = {_g(c['sy2'])}   Σyx = {_g(c['sxy'])}")

    seccion("Pendiente (contribución marginal)")
    linea("b1 = (Σyx - n·x̄·ȳ) / (Σx² - n·x̄²)")
    linea(f"   = ({_g(c['sxy'])} - {n}·{_n(c['xm'])}·{_n(c['ym'])}) / ({_g(c['sx2'])} - {n}·{_n(c['xm'])}²)")
    linea(f"   = {_n(c['b1'])}")
    seccion("Ordenada al origen")
    linea("b0 = ȳ - b1·x̄")
    linea(f"   = {_n(c['ym'])} - ({_n(c['b1'])})·{_n(c['xm'])}")
    linea(f"   = {_n(c['b0'])}")
    seccion("Recta de mínimos cuadrados   [inciso: hallar la recta / construir el modelo]")
    linea("(\"hallar la recta\" = calcular b0 y b1 y escribir la ecuación)")
    flecha(_recta(c))
    seccion("Interpretación (en palabras, para la hoja)")
    verbo = "aumenta" if c["b1"] >= 0 else "disminuye"
    linea(f"b1 = {_n(c['b1'])}: por cada unidad más de {nx}, {ny} {verbo}")
    linea(f"     en promedio {_n(abs(c['b1']))}.   (el signo dice si sube o baja)")
    linea(f"b0 = {_n(c['b0'])}: con {nx} = 0, {ny} valdría en promedio {_n(c['b0'])}.")
    xmin, xmax = min(x), max(x)
    if not (xmin <= 0 <= xmax):
        linea(f"     Es una extrapolación: x = 0 está fuera del rango observado ({_g(xmin)} a {_g(xmax)}).")

    seccion("Desvíos   [van en: validar, porque tc usa Sb1]")
    linea("S   = √( (Σy² - b0·Σy - b1·Σyx) / (n - 2) )")
    linea(f"    = √( ({_g(c['sy2'])} - {_n(c['b0'])}·{_g(c['sy'])} - ({_n(c['b1'])})·{_g(c['sxy'])}) / {n - 2} )")
    linea(f"    = {_n(c['s'])}")
    linea("Sb1 = S / √(Σx² - n·x̄²)")
    linea(f"    = {_n(c['s'])} / √({_n(c['sxx'])})")
    linea(f"    = {_n(c['sb1'])}")

    seccion("Correlación y determinación   [inciso: \"qué % se explica\" / fuerza]")
    linea("r  = (Σyx - n·x̄·ȳ) / √( (Σx² - n·x̄²)·(Σy² - n·ȳ²) )")
    linea(f"   = {_n(c['r'])}")
    sentido = "directa: cuando sube " + nx + ", sube " + ny if c["r"] >= 0 else "inversa: cuando sube " + nx + ", baja " + ny
    linea("   r mide la fuerza de la relación (de -1 a 1).")
    linea(f"   Es {sentido}.")
    r2 = c["r"] ** 2
    linea(f"r² = {_n(r2)}")
    flecha(f"El {_n(r2 * 100, 2)}% de la variación de {ny} se explica por {nx};")
    linea(f"  el {_n(100 - r2 * 100, 2)}% restante se debe a otros factores.")

    tobs = c["b1"] / c["sb1"]
    tc = t.ppf(1 - alfa, n - 2)
    rechaza = abs(tobs) > tc
    seccion("Validación del modelo   [inciso: validar el modelo]")
    linea("H0: β1 = 0      H1: β1 ≠ 0")
    linea(f"  H0 en palabras: {nx} no influye en {ny}")
    linea(f"  (por cada unidad más de {nx}, {ny} cambia 0). Si se rechaza, el modelo sirve.")
    linea(f"α = {_n(alfa, 2)}   ·   t de Student con ν = n - 2 = {n - 2}")
    linea(f"tc = b1 / Sb1 = {_n(c['b1'])} / {_n(c['sb1'])} = {_n(tobs)}   →   |tc| = {_n(abs(tobs))}")
    linea("  (tc en el cuadernillo, t_obs en la guía: a cuántos Sb1 está b1 de 0)")
    linea(f"t(1-α ; ν) = t({_p(1 - alfa)} ; {n - 2}) = {_n(tc)}")
    linea("  (el límite: hasta ahí, que b1 no sea 0 puede ser casualidad de la muestra)")
    seccion("CR (condición de rechazo)")
    linea(f"Si |tc| > {_n(tc)}  →  se rechaza H0")
    seccion("Decisión")
    linea(f"|tc| = {_n(abs(tobs))}  {'>' if rechaza else '≤'}  {_n(tc)}")
    if rechaza:
        flecha(f"SE RECHAZA H0: {nx} influye en {ny} (hay relación lineal);")
        linea(f"  el modelo sirve para estimar {ny} a partir de {nx}.")
        r2 = c["r"] ** 2
        campo = ("cualquier campo de aplicación" if r2 > 0.9 else
                 "procesos físicos e industriales" if r2 > 0.8 else
                 "econometría" if r2 > 0.6 else
                 "sociología o psicología" if r2 > 0.4 else None)
        linea(f"  2º criterio (cuadernillo pág. 115): r² = {_n(r2)}" +
              (f" > umbral → válido para {campo}." if campo else " ≤ 0,4 → relación débil."))
    else:
        flecha(f"NO se rechaza H0: no se puede afirmar que {nx} influya en {ny}")
        linea("  (el modelo no es válido).")
    fin()
    c["t_obs"] = tobs
    return c


# CUÁNDO: "¿se puede afirmar que por cada ... adicional, y aumenta /
#         disminuye en más de VALOR?"
# PARA QUÉ: ensayo sobre la pendiente, como la guía (VII.12 d).
#   beta10 = el valor de la frase, con su signo ("disminuye en más de 1" -> -1)
#   cola   = "izquierda" si H1 es β1 < beta10, "derecha" si β1 > beta10
def ensayo_pendiente(x, y, beta10, alfa, cola, nombres=("x", "y")):
    if cola not in ("derecha", "izquierda"):
        raise ValueError('cola = "derecha" o "izquierda".')
    c = _sumas(x, y)
    k = t.ppf(1 - alfa, c["gl"])
    s0, s1 = ("≤", ">") if cola == "derecha" else ("≥", "<")
    op = "+" if cola == "derecha" else "-"
    b1c = beta10 + k * c["sb1"] if cola == "derecha" else beta10 - k * c["sb1"]
    rechaza = c["b1"] >= b1c if cola == "derecha" else c["b1"] <= b1c
    nx, ny = nombres
    titulo("Ensayo sobre la pendiente β1")
    seccion("Hipótesis")
    linea(f"H0: β1 {s0} {_n(beta10, 2)}")
    linea(f"H1: β1 {s1} {_n(beta10, 2)}   (lo que se quiere asegurar va en H1)")
    linea(f"Cola {cola}   ·   α = {_n(alfa, 2)}   ·   gl = n - 2 = {c['gl']}")
    seccion("Muestra")
    linea(f"b1 = {_n(c['b1'])}   ·   Sb1 = {_n(c['sb1'])}")
    seccion("Valor crítico")
    linea(f"b1c = β10 {op} t(1-α ; n-2) · Sb1")
    linea(f"    = {_n(beta10, 2)} {op} {_n(k)} · {_n(c['sb1'])}")
    linea(f"    = {_n(b1c)}")
    seccion("CR (condición de rechazo)")
    linea(f"Si b1 {'≥' if cola == 'derecha' else '≤'} {_n(b1c)}  →  se rechaza H0")
    seccion("Decisión")
    mayor = c["b1"] >= b1c
    linea(f"b1 = {_n(c['b1'])}  {'≥' if mayor else '<'}  {_n(b1c)}")
    if beta10 < 0 or (beta10 == 0 and cola == "izquierda"):
        frase = f"{ny} disminuye en más de {_n(abs(beta10), 2)}" if cola == "izquierda" else f"{ny} disminuye en menos de {_n(abs(beta10), 2)}"
    else:
        frase = f"{ny} aumenta en más de {_n(beta10, 2)}" if cola == "derecha" else f"{ny} aumenta en menos de {_n(beta10, 2)}"
    if rechaza:
        flecha(f"SE RECHAZA H0: se puede afirmar que por cada unidad más de {nx},")
        linea(f"  {frase}.")
    else:
        flecha(f"NO se rechaza H0: no se puede afirmar que por cada unidad más de {nx},")
        linea(f"  {frase}.")
    fin()
    return rechaza


# CUÁNDO: "estimar la contribución marginal", "intervalo para el
#         coeficiente de regresión / la pendiente".
def intervalo_pendiente(x, y, confianza, tipo="bilateral", nombres=("x", "y")):
    c = _sumas(x, y)
    alfa = 1 - confianza
    prob = 1 - alfa / 2 if tipo == "bilateral" else 1 - alfa
    k = t.ppf(prob, c["gl"])
    e = k * c["sb1"]
    et = "1-α/2" if tipo == "bilateral" else "1-α"
    titulo("Estimación de la pendiente β1")
    seccion("Límites")
    linea(f"b1 = {_n(c['b1'])}   ·   Sb1 = {_n(c['sb1'])}   ·   t({_p(prob)} ; {c['gl']}) = {_n(k)}")
    if tipo == "bilateral":
        linea(f"A ; B = b1 ∓ t({et} ; n-2) · Sb1 = {_n(c['b1'])} ∓ {_n(k)} · {_n(c['sb1'])}")
        res = (c["b1"] - e, c["b1"] + e)
        flecha(f"P({_n(res[0])} ≤ β1 ≤ {_n(res[1])}) = {_n(confianza, 2)}")
        linea(f"  Por cada unidad más de {nombres[0]}, {nombres[1]} cambia en promedio entre")
        linea(f"  {_n(res[0])} y {_n(res[1])} (negativo = baja), con {_n(confianza * 100, 0)}% de confianza.")
    elif tipo == "minimo":
        res = c["b1"] - e
        linea(f"A = b1 - t(1-α ; n-2) · Sb1 = {_n(res)}")
        flecha(f"P(β1 ≥ {_n(res)}) = {_n(confianza, 2)}")
    else:
        res = c["b1"] + e
        linea(f"B = b1 + t(1-α ; n-2) · Sb1 = {_n(res)}")
        flecha(f"P(β1 ≤ {_n(res)}) = {_n(confianza, 2)}")
    fin()
    return res


# CUÁNDO: "estimar la fuerza de la relación" (ρ) o "la influencia
#         porcentual" (ρ²) con un intervalo. Usa la transformación Z de
#         Fisher, como la guía (VII.12 b y c).
def intervalo_correlacion(x, y, confianza, nombres=("x", "y")):
    c = _sumas(x, y)
    r, n = c["r"], c["n"]
    alfa = 1 - confianza
    z = norm.ppf(1 - alfa / 2)
    zr = 0.5 * math.log((1 + r) / (1 - r))
    zmin, zmax = zr - z / math.sqrt(n - 3), zr + z / math.sqrt(n - 3)
    a = (math.exp(2 * zmin) - 1) / (math.exp(2 * zmin) + 1)
    b = (math.exp(2 * zmax) - 1) / (math.exp(2 * zmax) + 1)
    titulo("Estimación de la correlación ρ y de ρ²")
    seccion("Transformación Z de Fisher")
    linea("Z = ½ · ln((1 + r) / (1 - r)) ∓ Z(1-α/2) / √(n - 3)")
    linea(f"  con r = {_n(r)}:   ½ · ln((1 + r) / (1 - r)) = {_n(zr)}   y   {_n(z)} / √{n - 3} = {_n(z / math.sqrt(n - 3))}")
    linea(f"Zmín = {_n(zmin)}   ·   Zmáx = {_n(zmax)}")
    seccion("Límites  (A ; B = (e^(2Z) - 1) / (e^(2Z) + 1))")
    flecha(f"P({_n(min(a, b))} ≤ ρ ≤ {_n(max(a, b))}) = {_n(confianza, 2)}")
    lo, hi = sorted([a ** 2, b ** 2]) if a * b > 0 else (0.0, max(a ** 2, b ** 2))
    flecha(f"P({_n(lo)} ≤ ρ² ≤ {_n(hi)}) = {_n(confianza, 2)}   (influencia porcentual)")
    linea(f"  ρ = fuerza de la relación en TODA la población (r era de la muestra).")
    linea(f"  ρ²: {nombres[0]} explica entre el {_n(lo * 100, 2)}% y el {_n(hi * 100, 2)}% de la variación")
    linea(f"  de {nombres[1]}, con {_n(confianza * 100, 0)}% de confianza.")
    fin()
    return (min(a, b), max(a, b))


def _intervalo_y(x, y, x0, confianza, tipo, prediccion, nombres=("x", "y")):
    c = _sumas(x, y)
    y0 = c["b0"] + c["b1"] * x0
    alfa = 1 - confianza
    prob = 1 - alfa / 2 if tipo == "bilateral" else 1 - alfa
    k = t.ppf(prob, c["gl"])
    uno = 1 if prediccion else 0
    raiz = math.sqrt(uno + 1 / c["n"] + (x0 - c["xm"]) ** 2 / c["sxx"])
    e = k * c["s"] * raiz
    et = "1-α/2" if tipo == "bilateral" else "1-α"
    pre = "1 + " if prediccion else ""
    if prediccion:
        titulo(f"Intervalo de PREDICCIÓN para un caso con x0 = {_g(x0)}")
    else:
        titulo(f"Estimación del valor PROMEDIO de y para x0 = {_g(x0)}")
    seccion("Estimador puntual")
    linea(f"ŷ0 = b0 + b1·x0 = {_n(c['b0'])} + ({_n(c['b1'])})·{_g(x0)} = {_n(y0)}")
    seccion("Límites")
    op = "∓" if tipo == "bilateral" else ("-" if tipo == "minimo" else "+")
    linea(f"ŷ0 {op} t({et} ; n-2) · S · √( {pre}1/n + (x0 - x̄)² / (Σx² - n·x̄²) )")
    linea(f"= {_n(y0)} {op} {_n(k)} · {_n(c['s'])} · √( {pre}1/{c['n']} + "
          f"({_g(x0)} - {_n(c['xm'])})² / {_n(c['sxx'])} )")
    linea(f"= {_n(y0)} {op} {_n(e)}")
    que = "y" if prediccion else "E(y)"
    if tipo == "bilateral":
        res = (y0 - e, y0 + e)
        flecha(f"P({_n(res[0])} ≤ {que} ≤ {_n(res[1])}) = {_n(confianza, 2)}")
        nx, ny = nombres
        if prediccion:
            linea(f"  UN caso con {nx} = {_g(x0)} tendrá {ny} entre {_n(res[0])} y {_n(res[1])},")
            linea(f"  con {_n(confianza * 100, 0)}% de confianza. Es más ancho que el del promedio")
            linea("  porque un caso solo varía más que el promedio de muchos (el \"1 +\" de la raíz).")
        else:
            linea(f"  El PROMEDIO de {ny} de todos los casos con {nx} = {_g(x0)} está entre")
            linea(f"  {_n(res[0])} y {_n(res[1])}, con {_n(confianza * 100, 0)}% de confianza.")
    elif tipo == "minimo":
        res = y0 - e
        flecha(f"P({que} ≥ {_n(res)}) = {_n(confianza, 2)}   (MÍNIMO)")
    else:
        res = y0 + e
        flecha(f"P({que} ≤ {_n(res)}) = {_n(confianza, 2)}   (MÁXIMO)")
    fin()
    return res


# CUÁNDO: "estimar el PROMEDIO de y para x = ..." ("en promedio", "la
#         dureza promedio", "el costo medio").
def estimar_media_regresion(x, y, x0, confianza, tipo="bilateral", nombres=("x", "y")):
    return _intervalo_y(x, y, x0, confianza, tipo, prediccion=False, nombres=nombres)


# CUÁNDO: "si UN determinado caso tiene x = ..., ¿qué y puede tener?"
#         ("intervalo de predicción", "para un empleado", "la semana que viene").
def predecir_regresion(x, y, x0, confianza, tipo="bilateral", nombres=("x", "y")):
    return _intervalo_y(x, y, x0, confianza, tipo, prediccion=True, nombres=nombres)
