# =====================================================================
#  MEDIAS - Comparar los promedios de dos poblaciones (t de Student)
# =====================================================================
#
#  QUÉ RESPONDE
#    ¿El promedio de una población es mayor / menor / distinto que el
#    de otra? ¿En cuánto? ¿En qué porcentaje?
#
#  SEÑALES EN LA CONSIGNA
#    "producción promedio", "rendimiento", "existen diferencias",
#    "¿se puede asegurar que A es mayor que B?", "mayor en un 30%",
#    "diferencia mínima / máxima esperada", "incremento porcentual".
#    Casi siempre viene DESPUÉS de comparar varianzas (fisher.py).
#
#  EL CAMINO (siempre en este orden)
#    1) Sacar n, media y desvío de cada población      -> datos.py
#    2) ¿Las varianzas son iguales o distintas?        -> metodo_para_medias()
#         iguales  -> método "pool"  (se amalgaman los desvíos)
#         distintas -> método "welch" (grados de libertad aproximados)
#       (si te DAN los σ poblacionales -> método "conocidos", usa Normal)
#    3) Plantear la hipótesis sobre la diferencia      -> hipotesis.py
#    4) Valor crítico y decisión, o intervalo, o porcentaje
#
#  LA IDEA
#    Para comparar promedios se RESTA (al revés que en Fisher):
#      δ = μ1 - μ2           (parámetro)     d = x̄1 - x̄2    (muestra)
#    Con porcentaje se usa h = 1 + f  (ej: "mayor en un 30%" -> h = 1.30):
#      δ* = μ1 - h·μ2        (parámetro)     d* = x̄1 - h·x̄2 (muestra)
#    "A es mayor que B en más de un 30%"  ->  μA > 1,30·μB  ->  μA - 1,30·μB > 0
#
#  COSAS QUE TENÉS QUE SABER
#    - La diferencia SÍ puede dar negativa (es una resta).
#    - La población que nombra la frase va como 1 (adelante en la resta).
#    - Pool:  gl = n1 + n2 - 2
#    - Welch: gl se calcula con una fórmula y se redondea PARA ABAJO.
#    - Para elegir el método, el apunte usa α = 10% en el test F, poniendo
#      arriba el desvío más grande (cola derecha).
#    - Con muestras grandes (las tablas del parcial, n > 100) la t es casi
#      igual a la Normal, pero se usa t igual.
#
#  QUÉ DECIDÍS VOS / QUÉ CALCULA EL PROGRAMA
#    Vos: cuál es la población 1, δ0, h, α, la cola, y la conclusión.
#    Programa: el método, el error estándar, gl, t, valor crítico,
#              intervalo y el h límite.
#
#  ORDEN DE LOS DATOS (igual en todas las funciones)
#    n1, x1, s1, n2, x2, s2   ->  primero todo de la población 1,
#                                después todo de la población 2.
# =====================================================================

from scipy.stats import t, norm
from formulas.fisher import cociente_varianzas, valor_critico, rechaza_h0
from formulas.fisher import valor_f as valor_f_
from formulas._formato import titulo, seccion, linea, flecha, fin


def _n(x, dec=4):
    return f"{x:.{dec}f}".replace(".", ",")


def _p(prob):
    return f"{prob:g}".replace(".", ",")


def _chequear(cola=None, metodo=None, tipo=None):
    if cola is not None and cola not in ("derecha", "izquierda", "bilateral"):
        raise ValueError(f'cola = "{cola}" no existe. Usá "derecha", "izquierda" o "bilateral".')
    if metodo is not None and metodo not in ("pool", "welch", "conocidos"):
        raise ValueError(f'metodo = "{metodo}" no existe. Usá "pool", "welch" o "conocidos".')
    if tipo is not None and tipo not in ("bilateral", "minimo", "maximo"):
        raise ValueError(f'tipo = "{tipo}" no existe. Usá "bilateral", "minimo" o "maximo".')


# --- Paso 2: elegir el método ----------------------------------------

# CUÁNDO: antes de comparar medias, si NO te dan los σ poblacionales.
# PARA QUÉ: decidir si se amalgama ("pool") o se usa "welch".
# Hace el test F como el apunte: desvío más grande arriba, cola derecha,
# φ0 = 1, α = 10%. Imprime el planteo para que lo copies en la hoja.
def metodo_para_medias(n1, x1, s1, n2, x2, s2, alfa=0.10, nombres=("1", "2")):
    a, b = nombres
    if s1 >= s2:
        s_arr, n_arr, s_ab, n_ab, arr, ab = s1, n1, s2, n2, a, b
    else:
        s_arr, n_arr, s_ab, n_ab, arr, ab = s2, n2, s1, n1, b, a
    j2 = cociente_varianzas(s_arr, s_ab, mostrar=False)
    F = valor_f_(1 - alfa, n_arr - 1, n_ab - 1)
    j2c = valor_critico(1, alfa, n_arr - 1, n_ab - 1, "derecha", mostrar=False)
    rechaza = rechaza_h0(j2, j2c, "derecha", mostrar=False)

    titulo("Paso previo: F de Fisher (¿varianzas iguales?)")
    seccion("Hipótesis   (arriba el desvío muestral más grande)")
    linea(f"H0: σ{arr} ≤ σ{ab}   (varianzas iguales)")
    linea(f"H1: σ{arr} > σ{ab}")
    linea(f"Cola derecha   ·   α = {_n(alfa, 2)}   (el paso previo siempre usa 10%)")
    seccion("Justificación")
    linea("Los desvíos poblacionales no se conocen: antes de comparar las medias")
    linea("se prueba si las varianzas se pueden suponer iguales. Se usa la F de")
    linea("Fisher porque se comparan varianzas de dos poblaciones independientes.")
    seccion("Muestra")
    linea(f"j² = S{arr}² / S{ab}²")
    linea(f"   = {_n(s_arr)}² / {_n(s_ab)}²")
    linea(f"   = {_n(j2)}")
    seccion("Valor crítico")
    linea(f"j²c = φ0² · F(1-α ; n{arr}-1 ; n{ab}-1)")
    linea(f"    = 1² · F({_n(1 - alfa, 2)} ; {n_arr - 1} ; {n_ab - 1})")
    linea(f"    = 1 · {_n(F)}")
    linea(f"    = {_n(j2c)}")
    seccion("CR (condición de rechazo)")
    linea(f"Si j² ≥ {_n(j2c)}  →  se rechaza H0")
    seccion("RD (regla de decisión)")
    linea("Si se rechaza H0  →  varianzas distintas  →  método de Welch")
    linea("Si no se rechaza  →  varianzas iguales    →  método Pool")
    seccion("Decisión")
    if rechaza:
        linea(f"{_n(j2)} ≥ {_n(j2c)}  →  se rechaza H0")
        flecha("varianzas DISTINTAS  →  método de WELCH")
        fin()
        return "welch"
    linea(f"{_n(j2)} < {_n(j2c)}  →  no se rechaza H0")
    flecha("varianzas supuestas IGUALES  →  método POOL")
    fin()
    return "pool"


# --- Piezas del cálculo ------------------------------------------------

# CUÁNDO: método "pool" (varianzas supuestas iguales).
# PARA QUÉ: un único desvío que junta las dos muestras.
# Sa = raíz( ((n1-1)·S1² + (n2-1)·S2²) / (n1 + n2 - 2) )
def desvio_amalgamado(n1, s1, n2, s2):
    return (((n1 - 1) * s1 ** 2 + (n2 - 1) * s2 ** 2) / (n1 + n2 - 2)) ** 0.5


# CUÁNDO: método "welch" (varianzas probadas distintas).
# PARA QUÉ: grados de libertad aproximados de Aspin-Welch, redondeados
# para abajo. Con porcentaje, h multiplica a la población 2.
def gl_welch(n1, s1, n2, s2, h=1):
    a = s1 ** 2 / n1
    b = h ** 2 * s2 ** 2 / n2
    nu = (a + b) ** 2 / (a ** 2 / (n1 - 1) + b ** 2 / (n2 - 1))
    return int(nu)


# CUÁNDO: siempre que compares medias (lo usan las otras funciones).
# PARA QUÉ: grados de libertad según el método ("conocidos" no tiene).
def grados_libertad(metodo, n1, s1, n2, s2, h=1):
    if metodo == "pool":
        return n1 + n2 - 2
    if metodo == "welch":
        return gl_welch(n1, s1, n2, s2, h)
    return None


# CUÁNDO: siempre que compares medias (lo usan las otras funciones).
# PARA QUÉ: el desvío de la diferencia d (o d*).
#   pool:      Sa · raíz(1/n1 + h²/n2)
#   welch:     raíz(S1²/n1 + h²·S2²/n2)
#   conocidos: raíz(σ1²/n1 + h²·σ2²/n2)   (s1 y s2 son los σ dados)
def error_estandar(metodo, n1, s1, n2, s2, h=1):
    if metodo == "pool":
        return desvio_amalgamado(n1, s1, n2, s2) * (1 / n1 + h ** 2 / n2) ** 0.5
    return (s1 ** 2 / n1 + h ** 2 * s2 ** 2 / n2) ** 0.5


# CUÁNDO: necesitás un valor de la tabla t de Student.
# PARA QUÉ: reemplaza la tabla, ej: t(0,99 ; 22) = 2,5083
def valor_t(probabilidad, gl):
    return float(t.ppf(probabilidad, gl))


def _fractil(metodo, probabilidad, gl):
    if metodo == "conocidos":
        return float(norm.ppf(probabilidad))
    return valor_t(probabilidad, gl)


# CUÁNDO: tenés las dos medias muestrales.
# PARA QUÉ: d = x̄1 - h·x̄2   (sin porcentaje, h = 1 y queda x̄1 - x̄2)
def diferencia_muestral(x1, x2, h=1):
    return x1 - h * x2


# --- Ensayo de hipótesis -----------------------------------------------

# CUÁNDO: "¿se puede asegurar que...?" sobre los promedios.
# PARA QUÉ: el valor crítico dc (la línea).
#   delta0 = valor de la hipótesis (casi siempre 0; "en 0,35 como mínimo" -> 0.35)
#   cola   = "derecha" (H1 >), "izquierda" (H1 <) o "bilateral" (H1 ≠)
#   h      = 1 + porcentaje (ej: 1.30). Sin porcentaje, dejalo en 1.
# En bilateral devuelve los dos límites (abajo, arriba).
def valor_critico_diferencia(metodo, delta0, alfa, n1, x1, s1, n2, x2, s2, cola, h=1):
    gl = grados_libertad(metodo, n1, s1, n2, s2, h)
    se = error_estandar(metodo, n1, s1, n2, s2, h)
    if cola == "derecha":
        return delta0 + _fractil(metodo, 1 - alfa, gl) * se
    if cola == "izquierda":
        return delta0 - _fractil(metodo, 1 - alfa, gl) * se
    k = _fractil(metodo, 1 - alfa / 2, gl)
    return (delta0 - k * se, delta0 + k * se)


# CUÁNDO: ya tenés d (muestra) y dc (la línea).
# PARA QUÉ: True = se rechaza H0; False = no se rechaza.
def rechaza_h0_diferencia(d, dc, cola):
    if cola == "derecha":
        return d >= dc
    if cola == "izquierda":
        return d <= dc
    return d <= dc[0] or d >= dc[1]


# CUÁNDO: querés todo el ensayo de una, impreso para la hoja.
# PARA QUÉ: imprime hipótesis, muestra, valor crítico, CR, RD y decisión.
#   nombres = cómo se llaman los grupos, ej: ("B", "A") -> H0: μB ≤ μA
def _raiz(metodo, n1, s1, n2, s2, h, a, b):
    """Devuelve la raíz del valor crítico como en la guía: (con símbolos, con números)."""
    hh = "" if h == 1 else "h²·"
    hv = "" if h == 1 else f"{_n(h, 2)}²·"
    if metodo == "pool":
        sa = desvio_amalgamado(n1, s1, n2, s2)
        return (f"Sa · √(1/n{a} + {hh}1/n{b})",
                f"{_n(sa)} · √(1/{n1} + {hv}1/{n2})")
    letra = "σ" if metodo == "conocidos" else "S"
    return (f"√({letra}{a}²/n{a} + {hh}{letra}{b}²/n{b})",
            f"√({_n(s1)}²/{n1} + {hv}{_n(s2)}²/{n2})")


def _imprimir_gl(metodo, n1, s1, n2, s2, h, a, b):
    """Imprime Sa (Pool) y los grados de libertad: fórmula, reemplazo, resultado."""
    hh = "" if h == 1 else "h²·"
    gl = grados_libertad(metodo, n1, s1, n2, s2, h)
    if metodo == "pool":
        sa = desvio_amalgamado(n1, s1, n2, s2)
        linea(f"Sa = √( ((n{a}-1)·S{a}² + (n{b}-1)·S{b}²) / (n{a} + n{b} - 2) )")
        linea(f"   = √( ({n1 - 1}·{_n(s1)}² + {n2 - 1}·{_n(s2)}²) / {n1 + n2 - 2} )")
        linea(f"   = {_n(sa)}")
        linea()
        linea(f"gl = n{a} + n{b} - 2")
        linea(f"   = {n1} + {n2} - 2")
        linea(f"   = {gl}")
        linea()
    elif metodo == "welch":
        va = s1 ** 2 / n1
        vb = h ** 2 * s2 ** 2 / n2
        nu = (va + vb) ** 2 / (va ** 2 / (n1 - 1) + vb ** 2 / (n2 - 1))
        linea(f"gl = (S{a}²/n{a} + {hh}S{b}²/n{b})² / [ 1/(n{a}-1)·(S{a}²/n{a})² + 1/(n{b}-1)·({hh}S{b}²/n{b})² ]")
        linea(f"   = ({_n(va)} + {_n(vb)})² / [ 1/{n1 - 1}·{_n(va)}² + 1/{n2 - 1}·{_n(vb)}² ]")
        linea(f"   = {_n(nu, 4)}  →  {gl}   (Welch, se redondea para abajo)")
        linea()
    return gl


def ensayo_medias(metodo, delta0, alfa, n1, x1, s1, n2, x2, s2, cola, h=1, nombres=("1", "2")):
    _chequear(cola=cola, metodo=metodo)
    a, b = nombres
    gl = grados_libertad(metodo, n1, s1, n2, s2, h)
    se = error_estandar(metodo, n1, s1, n2, s2, h)
    d = diferencia_muestral(x1, x2, h)
    dc = valor_critico_diferencia(metodo, delta0, alfa, n1, x1, s1, n2, x2, s2, cola, h)
    rechaza = rechaza_h0_diferencia(d, dc, cola)
    s_h1, s_h0 = {"derecha": (">", "≤"), "izquierda": ("<", "≥"), "bilateral": ("≠", "=")}[cola]
    lado = f"μ{b}" if h == 1 else f"{_n(h, 2)}·μ{b}"
    dn = "d" if h == 1 else "d*"
    delta = "δ" if h == 1 else "δ*"

    titulo("Comparación de medias")
    seccion("Hipótesis")
    if delta0 == 0:
        linea(f"H0: μ{a} {s_h0} {lado}")
        linea(f"H1: μ{a} {s_h1} {lado}")
    else:
        linea(f"H0: μ{a} - {lado} {s_h0} {_n(delta0, 2)}")
        linea(f"H1: μ{a} - {lado} {s_h1} {_n(delta0, 2)}")
    linea(f"Cola {cola}   ·   α = {_n(alfa, 2)}")
    linea(f"(En las fórmulas: {delta} = μ{a} - {lado}   y   δ0 = {_n(delta0, 2)})")
    seccion("Justificación")
    if metodo == "pool":
        linea("t de Student con desvío amalgamado (Pool): los desvíos poblacionales")
        linea("no se conocen y las varianzas se suponen iguales (paso previo).")
    elif metodo == "welch":
        linea("t de Student con el método de Welch: los desvíos poblacionales")
        linea("no se conocen y las varianzas son distintas (paso previo).")
    else:
        linea("Normal (Z): los desvíos poblacionales son conocidos.")

    seccion("Muestra")
    if h == 1:
        linea(f"d = x̄{a} - x̄{b}")
        linea(f"  = {_n(x1)} - {_n(x2)}")
        linea(f"  = {_n(d)}")
    else:
        linea(f"d* = x̄{a} - h·x̄{b}")
        linea(f"   = {_n(x1)} - {_n(h, 2)}·{_n(x2)}")
        linea(f"   = {_n(d)}")

    seccion("Valor crítico")
    _imprimir_gl(metodo, n1, s1, n2, s2, h, a, b)
    rs, rv = _raiz(metodo, n1, s1, n2, s2, h, a, b)
    prob = 1 - alfa / 2 if cola == "bilateral" else 1 - alfa
    k = _fractil(metodo, prob, gl)
    et = "1-α/2" if cola == "bilateral" else "1-α"
    if metodo == "conocidos":
        linea(f"Z({et}) = Z({_p(prob)}) = {_n(k)}")
        tab, tabv = f"Z({et})", f"Z({_p(prob)})"
    else:
        linea(f"t({et} ; gl) = t({_p(prob)} ; {gl}) = {_n(k)}")
        tab, tabv = f"t({et} ; gl)", f"t({_p(prob)} ; {gl})"
    linea()
    sp = " " * len(dn + "c")
    if cola == "bilateral":
        linea(f"{dn}c = δ0 ± {tab} · {rs}")
        linea(f"{sp} = {_n(delta0, 2)} ± {_n(k)} · {rv}")
        linea(f"{sp} = {_n(dc[0])}   y   {_n(dc[1])}")
        cr = f"Si {dn} ≤ {_n(dc[0])}  o  {dn} ≥ {_n(dc[1])}  →  se rechaza H0"
    elif cola == "derecha":
        linea(f"{dn}c = δ0 + {tab} · {rs}")
        linea(f"{sp} = {_n(delta0, 2)} + {_n(k)} · {rv}")
        linea(f"{sp} = {_n(dc)}")
        cr = f"Si {dn} ≥ {_n(dc)}  →  se rechaza H0"
    else:
        linea(f"{dn}c = δ0 - {tab} · {rs}")
        linea(f"{sp} = {_n(delta0, 2)} - {_n(k)} · {rv}")
        linea(f"{sp} = {_n(dc)}")
        cr = f"Si {dn} ≤ {_n(dc)}  →  se rechaza H0"
    seccion("CR (condición de rechazo)")
    linea(cr)
    seccion("RD (regla de decisión)")
    linea(f"Si se rechaza H0  →  se puede afirmar H1 (μ{a} {s_h1} {lado})")
    linea("[completá con la acción del problema: ej. se aconseja comprar]")
    seccion("Decisión")
    if cola == "bilateral":
        linea(f"{dn} = {_n(d)}  " + ("queda afuera de" if rechaza else "queda dentro de")
              + f"  [{_n(dc[0])} ; {_n(dc[1])}]")
    else:
        mayor = d >= dc
        linea(f"{dn} = {_n(d)}  {'≥' if mayor else '<'}  {_n(dc)}")
    flecha(f"SE RECHAZA H0: se puede afirmar que μ{a} {s_h1} {lado}" if rechaza
           else f"NO se rechaza H0: no hay pruebas suficientes de que μ{a} {s_h1} {lado}")
    fin()
    return rechaza


# --- Estimación (intervalos) -------------------------------------------

# CUÁNDO: "estimar la diferencia", "diferencia mínima / máxima esperada",
#         "con un N.C. del 90%".
# PARA QUÉ: límites para δ = μ1 - μ2.
#   tipo = "bilateral" -> (A, B)  entre cuánto y cuánto
#          "minimo"    -> A       diferencia mínima garantizada (δ ≥ A)
#          "maximo"    -> B       diferencia máxima esperada   (δ ≤ B)
def intervalo_diferencia(metodo, confianza, n1, x1, s1, n2, x2, s2, tipo="bilateral",
                         mostrar=True, nombres=("1", "2")):
    _chequear(metodo=metodo, tipo=tipo)
    a, b = nombres
    alfa = 1 - confianza
    gl = grados_libertad(metodo, n1, s1, n2, s2)
    se = error_estandar(metodo, n1, s1, n2, s2)
    d = x1 - x2
    prob = 1 - alfa / 2 if tipo == "bilateral" else 1 - alfa
    k = _fractil(metodo, prob, gl)
    et = "1-α/2" if tipo == "bilateral" else "1-α"
    if metodo == "conocidos":
        tab, tabv = f"Z({et})", f"Z({_p(prob)})"
    else:
        tab, tabv = f"t({et} ; gl)", f"t({_p(prob)} ; {gl})"
    if tipo == "bilateral":
        res = (d - k * se, d + k * se)
    elif tipo == "minimo":
        res = d - k * se
    else:
        res = d + k * se
    if not mostrar:
        return res
    titulo(f"Estimación de δ = μ{a} - μ{b}")
    seccion("Datos")
    linea(f"Método: {metodo}   ·   confianza = {_n(confianza, 2)}")
    seccion("Muestra")
    linea(f"d = x̄{a} - x̄{b}")
    linea(f"  = {_n(x1)} - {_n(x2)}")
    linea(f"  = {_n(d)}")
    seccion("Límites")
    _imprimir_gl(metodo, n1, s1, n2, s2, 1, a, b)
    rs, rv = _raiz(metodo, n1, s1, n2, s2, 1, a, b)
    linea(f"{tab} = {tabv} = {_n(k)}")
    linea()
    if tipo == "bilateral":
        linea(f"A ; B = d ∓ {tab} · {rs}")
        linea(f"      = {_n(d)} ∓ {_n(k)} · {rv}")
        linea(f"      = {_n(res[0])}  y  {_n(res[1])}")
        seccion("Resultado")
        flecha(f"P({_n(res[0])} ≤ μ{a} - μ{b} ≤ {_n(res[1])}) = {_n(confianza, 2)}")
    elif tipo == "minimo":
        linea(f"A = d - {tab} · {rs}")
        linea(f"  = {_n(d)} - {_n(k)} · {rv}")
        linea(f"  = {_n(res)}")
        seccion("Resultado (diferencia MÍNIMA esperada)")
        flecha(f"P(μ{a} - μ{b} ≥ {_n(res)}) = {_n(confianza, 2)}")
    else:
        linea(f"B = d + {tab} · {rs}")
        linea(f"  = {_n(d)} + {_n(k)} · {rv}")
        linea(f"  = {_n(res)}")
        seccion("Resultado (diferencia MÁXIMA esperada)")
        flecha(f"P(μ{a} - μ{b} ≤ {_n(res)}) = {_n(confianza, 2)}")
    fin()
    return res


# CUÁNDO: "¿qué diferencia porcentual mínima se puede garantizar?",
#         "¿hay un incremento o decremento porcentual? ¿de cuánto?"
# PARA QUÉ: el h del borde, donde d* justo toca la línea.
#   cola = "derecha"   -> μ1 > h·μ2 : h MÍNIMO garantizado (incremento)
#          "izquierda" -> μ1 < h·μ2 : h MÁXIMO (decremento)
# El porcentaje es (h - 1) · 100. Ej: h = 1,0506 -> 5,06 % más.
def h_limite(metodo, alfa, n1, x1, s1, n2, x2, s2, cola="derecha", mostrar=True):
    def borde(h):
        d = diferencia_muestral(x1, x2, h)
        dc = valor_critico_diferencia(metodo, 0, alfa, n1, x1, s1, n2, x2, s2, cola, h)
        return d - dc

    lo, hi = 1e-6, 2 * max(x1 / x2, x2 / x1, 1) + 1
    for _ in range(200):
        medio = (lo + hi) / 2
        if (borde(medio) > 0) == (borde(lo) > 0):
            lo = medio
        else:
            hi = medio
    h = (lo + hi) / 2
    if mostrar:
        titulo("Porcentaje límite (h)")
        seccion("Planteo")
        linea("Se busca el h para el cual d* = x̄1 - h·x̄2 queda justo")
        linea("sobre el valor crítico:  x̄1 - h·x̄2 = dc*(h)")
        seccion("Resultado")
        linea(f"h = {_n(h)}")
        if cola == "derecha":
            flecha(f"μ1 supera a μ2 en al menos un {_n((h - 1) * 100, 2)}% "
                   f"(riesgo {_n(alfa, 2)})")
        else:
            flecha(f"μ1 es como máximo el {_n(h * 100, 2)}% de μ2 (riesgo {_n(alfa, 2)})")
        fin()
    return h


# CUÁNDO: "¿cuántas muestras más para reducir el error a ...?"
#         (mismo tamaño n en las dos poblaciones)
# PARA QUÉ: n de cada población. Se itera porque t depende de n.
#   e = error que querés lograr (ej: la mitad del anterior)
def n_para_error_medias(metodo, confianza, s1, s2, e, mostrar=True):
    alfa = 1 - confianza
    n = 2
    while True:
        gl = grados_libertad(metodo, n, s1, n, s2)
        k = _fractil(metodo, 1 - alfa / 2, gl)
        se = error_estandar(metodo, n, s1, n, s2)
        if k * se <= e:
            break
        n += 1
    if mostrar:
        tabla = "Z" if metodo == "conocidos" else "t"
        titulo("Tamaño de muestra")
        seccion("Planteo")
        linea(f"Menor n (igual en las dos) tal que {tabla}(1-α/2) · √(S1²/n + S2²/n) ≤ e = {_n(e)}")
        seccion("Resultado")
        linea(f"n = {n}:  {_n(k)} · {_n(se)} = {_n(k * se)} ≤ {_n(e)}")
        flecha(f"n = {n}   (unidades MÁS = n nuevo - n que ya tenías, en cada población)")
        fin()
    return n


# --- Muestras apareadas ------------------------------------------------

# CUÁNDO: los MISMOS individuos medidos dos veces (antes / después,
#         dos métodos sobre la misma pieza). No es independiente.
# PARA QUÉ: pasa las dos listas a una lista de diferencias d_i = x1_i - x2_i.
#   Después usás media() y desvio() de datos.py sobre esa lista,
#   y n = cantidad de pares, gl = n - 1, error estándar = S_d / raíz(n).
def diferencias_apareadas(lista1, lista2):
    return [a - b for a, b in zip(lista1, lista2)]
