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


def _n(x, dec=4):
    return f"{x:.{dec}f}".replace(".", ",")


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
def metodo_para_medias(n1, x1, s1, n2, x2, s2, alfa=0.10):
    if s1 >= s2:
        s_arr, n_arr, s_ab, n_ab, quien = s1, n1, s2, n2, "σ1/σ2"
    else:
        s_arr, n_arr, s_ab, n_ab, quien = s2, n2, s1, n1, "σ2/σ1"
    j2 = cociente_varianzas(s_arr, s_ab)
    j2c = valor_critico(1, alfa, n_arr - 1, n_ab - 1, "derecha")
    rechaza = rechaza_h0(j2, j2c, "derecha")
    print("--- Para la hoja: paso previo (Fisher) ---")
    print("Como los desvíos poblacionales no se conocen, antes de comparar las medias se")
    print("prueba si las varianzas se pueden suponer iguales. Se usa la distribución F de")
    print("Fisher-Snedecor porque se comparan las varianzas de dos poblaciones independientes.")
    print(f"φ = {quien} (arriba el desvío muestral más grande)")
    print(f"H0: φ ≤ 1 (varianzas iguales)   H1: φ > 1   (cola derecha),  α = {_n(alfa, 2)}")
    print(f"Valor crítico: j²c = φ0² · F(1-α ; n_arriba-1 ; n_abajo-1) = "
          f"1 · F({_n(1 - alfa, 2)} ; {n_arr - 1} ; {n_ab - 1}) = {_n(j2c)}")
    print(f"Muestra: j² = S_arriba² / S_abajo² = {_n(s_arr)}² / {_n(s_ab)}² = {_n(j2)}")
    if rechaza:
        print(f"{_n(j2)} ≥ {_n(j2c)} -> se rechaza H0 -> varianzas DISTINTAS -> método de Welch")
        print("------------------------------------------")
        return "welch"
    print(f"{_n(j2)} < {_n(j2c)} -> no se rechaza H0 -> varianzas supuestas IGUALES -> "
          f"método Pool (desvío amalgamado)")
    print("------------------------------------------")
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
# PARA QUÉ: imprime gl, error estándar, d, dc y la decisión. Devuelve True/False.
def ensayo_medias(metodo, delta0, alfa, n1, x1, s1, n2, x2, s2, cola, h=1):
    _chequear(cola=cola, metodo=metodo)
    gl = grados_libertad(metodo, n1, s1, n2, s2, h)
    se = error_estandar(metodo, n1, s1, n2, s2, h)
    d = diferencia_muestral(x1, x2, h)
    dc = valor_critico_diferencia(metodo, delta0, alfa, n1, x1, s1, n2, x2, s2, cola, h)
    rechaza = rechaza_h0_diferencia(d, dc, cola)
    param = "δ = μ1 - μ2" if h == 1 else f"δ* = μ1 - h·μ2 (h = {_n(h, 2)})"
    signo = {"derecha": (">", "≤"), "izquierda": ("<", "≥"), "bilateral": ("≠", "=")}[cola]
    print("--- Para la hoja: comparación de medias ---")
    print(f"Parámetro: {param}")
    print(f"H0: {param.split(' =')[0]} {signo[1]} {_n(delta0, 2)}   "
          f"H1: {param.split(' =')[0]} {signo[0]} {_n(delta0, 2)}   (cola {cola}),  α = {_n(alfa, 2)}")
    if metodo == "pool":
        sa = desvio_amalgamado(n1, s1, n2, s2)
        print("Se usa t de Student con desvío amalgamado (Pool), porque los desvíos poblacionales")
        print("no se conocen y las varianzas se suponen iguales.")
        print(f"Sa = raíz(((n1-1)·S1² + (n2-1)·S2²)/(n1+n2-2)) = {_n(sa)}")
        print(f"σ_d = Sa · raíz(1/n1 + h²/n2) = {_n(se)}      gl = n1 + n2 - 2 = {gl}")
    elif metodo == "welch":
        print("Se usa t de Student con el método de Welch, porque los desvíos poblacionales")
        print("no se conocen y las varianzas son distintas.")
        print(f"σ_d = raíz(S1²/n1 + h²·S2²/n2) = {_n(se)}      gl (Aspin-Welch, para abajo) = {gl}")
    else:
        print("Se usa la Normal (Z), porque los desvíos poblacionales son conocidos.")
        print(f"σ_d = raíz(σ1²/n1 + h²·σ2²/n2) = {_n(se)}")
    tabla = "Z" if metodo == "conocidos" else f"t(gl = {gl})"
    if cola == "bilateral":
        print(f"Valor crítico: dc = δ0 ± {tabla}(1-α/2) · σ_d = {_n(dc[0])} y {_n(dc[1])}")
        regla = f"si d queda por fuera de [{_n(dc[0])} ; {_n(dc[1])}], se rechaza H0"
    elif cola == "derecha":
        print(f"Valor crítico: dc = δ0 + {tabla}(1-α) · σ_d = {_n(dc)}")
        regla = f"si d ≥ {_n(dc)}, se rechaza H0"
    else:
        print(f"Valor crítico: dc = δ0 - {tabla}(1-α) · σ_d = {_n(dc)}")
        regla = f"si d ≤ {_n(dc)}, se rechaza H0"
    print(f"Regla de decisión: {regla}")
    if h == 1:
        print(f"Muestra: d = x̄1 - x̄2 = {_n(x1)} - {_n(x2)} = {_n(d)}")
    else:
        print(f"Muestra: d* = x̄1 - h·x̄2 = {_n(x1)} - {_n(h, 2)}·{_n(x2)} = {_n(d)}")
    print("-> SE RECHAZA H0 (se puede afirmar H1)" if rechaza
          else "-> NO se rechaza H0 (no hay pruebas suficientes para H1)")
    print("-------------------------------------------")
    return rechaza


# --- Estimación (intervalos) -------------------------------------------

# CUÁNDO: "estimar la diferencia", "diferencia mínima / máxima esperada",
#         "con un N.C. del 90%".
# PARA QUÉ: límites para δ = μ1 - μ2.
#   tipo = "bilateral" -> (A, B)  entre cuánto y cuánto
#          "minimo"    -> A       diferencia mínima garantizada (δ ≥ A)
#          "maximo"    -> B       diferencia máxima esperada   (δ ≤ B)
def intervalo_diferencia(metodo, confianza, n1, x1, s1, n2, x2, s2, tipo="bilateral", mostrar=True):
    _chequear(metodo=metodo, tipo=tipo)
    alfa = 1 - confianza
    gl = grados_libertad(metodo, n1, s1, n2, s2)
    se = error_estandar(metodo, n1, s1, n2, s2)
    d = x1 - x2
    tabla = "Z" if metodo == "conocidos" else f"t(gl = {gl})"
    if mostrar:
        print("--- Para la hoja: estimación de δ = μ1 - μ2 ---")
        print(f"Método {metodo}. d = x̄1 - x̄2 = {_n(d)},  σ_d = {_n(se)},  confianza = {confianza:.0%}")
    if tipo == "bilateral":
        k = _fractil(metodo, 1 - alfa / 2, gl)
        A, B = d - k * se, d + k * se
        if mostrar:
            print(f"A ; B = d ∓ {tabla}(1-α/2) · σ_d = {_n(d)} ∓ {_n(k)} · {_n(se)}")
            print(f"P({_n(A)} ≤ δ ≤ {_n(B)}) = {confianza:.0%}")
            print("-----------------------------------------------")
        return (A, B)
    k = _fractil(metodo, 1 - alfa, gl)
    if tipo == "minimo":
        A = d - k * se
        if mostrar:
            print(f"A = d - {tabla}(1-α) · σ_d = {_n(d)} - {_n(k)} · {_n(se)} = {_n(A)}")
            print(f"P(δ ≥ {_n(A)}) = {confianza:.0%}   (diferencia MÍNIMA esperada)")
            print("-----------------------------------------------")
        return A
    B = d + k * se
    if mostrar:
        print(f"B = d + {tabla}(1-α) · σ_d = {_n(d)} + {_n(k)} · {_n(se)} = {_n(B)}")
        print(f"P(δ ≤ {_n(B)}) = {confianza:.0%}   (diferencia MÁXIMA esperada)")
        print("-----------------------------------------------")
    return B


# CUÁNDO: "¿qué diferencia porcentual mínima se puede garantizar?",
#         "¿hay un incremento o decremento porcentual? ¿de cuánto?"
# PARA QUÉ: el h del borde, donde d* justo toca la línea.
#   cola = "derecha"   -> μ1 > h·μ2 : h MÍNIMO garantizado (incremento)
#          "izquierda" -> μ1 < h·μ2 : h MÁXIMO (decremento)
# El porcentaje es (h - 1) · 100. Ej: h = 1,0506 -> 5,06 % más.
def h_limite(metodo, alfa, n1, x1, s1, n2, x2, s2, cola="derecha"):
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
    return (lo + hi) / 2


# CUÁNDO: "¿cuántas muestras más para reducir el error a ...?"
#         (mismo tamaño n en las dos poblaciones)
# PARA QUÉ: n de cada población. Se itera porque t depende de n.
#   e = error que querés lograr (ej: la mitad del anterior)
def n_para_error_medias(metodo, confianza, s1, s2, e):
    alfa = 1 - confianza
    n = 2
    while True:
        gl = grados_libertad(metodo, n, s1, n, s2)
        k = _fractil(metodo, 1 - alfa / 2, gl)
        if k * error_estandar(metodo, n, s1, n, s2) <= e:
            return n
        n += 1


# --- Muestras apareadas ------------------------------------------------

# CUÁNDO: los MISMOS individuos medidos dos veces (antes / después,
#         dos métodos sobre la misma pieza). No es independiente.
# PARA QUÉ: pasa las dos listas a una lista de diferencias d_i = x1_i - x2_i.
#   Después usás media() y desvio() de datos.py sobre esa lista,
#   y n = cantidad de pares, gl = n - 1, error estándar = S_d / raíz(n).
def diferencias_apareadas(lista1, lista2):
    return [a - b for a, b in zip(lista1, lista2)]
