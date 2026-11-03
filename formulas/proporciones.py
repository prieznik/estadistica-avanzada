# =====================================================================
#  PROPORCIONES - Porcentajes (proceso de Bernoulli, modelo Binomial)
# =====================================================================
#
#  QUÉ RESPONDE
#    ¿Cumple un porcentaje máximo o mínimo? ¿Qué porcentaje hay en toda
#    la población? ¿Cuántas unidades hay que revisar?
#    Es el EJERCICIO 2 de casi todos los segundos parciales.
#
#  SEÑALES EN LA CONSIGNA
#    "porcentaje de fallas máximo del 7%", "de 95 unidades, 8 tienen
#    fallas", "fracción defectuosa", "estimar el porcentaje de unidades
#    en buenas condiciones", "¿cuántas unidades más...?"
#    También: "estimar el porcentaje de equipos por debajo de 14.000 hs"
#    sobre una tabla -> contás r con contar_debajo() de datos.py.
#
#  LA IDEA
#    Cada unidad es "éxito" o "no". En una muestra de n hay r éxitos.
#    r sigue una Binomial. El apunte calcula TODO EXACTO con la Binomial
#    (por eso en una resolución dice "por exacto"):
#      Gb(r / n ; p) = P(R ≥ r)   probabilidad acumulada DERECHA
#      Fb(r / n ; p) = P(R ≤ r)   probabilidad acumulada IZQUIERDA
#    Solo los tamaños de muestra para estimar se hacen con la
#    aproximación Normal (no hay fórmula exacta).
#
#  COSAS QUE TENÉS QUE SABER
#    - r y rc son CANTIDADES enteras (unidades), no porcentajes.
#    - Definí bien qué es "éxito": si preguntan por las BUENAS,
#      r = n - fallas.
#    - p va entre 0 y 1 (7% -> 0.07).
#    - Control de producción / recepción -> planteo OPTIMISTA
#      ("fallas máximo del 7%" -> H0: p ≤ 0,07, cola derecha).
#    - Inversión / mejora -> planteo PESIMISTA.
#    - "Reducir en un 30% la relación de los límites" -> R nuevo = R · 0,70
#      (así lo hace la guía, problema 15 del Tema III).
#
#  QUÉ DECIDÍS VOS / QUÉ CALCULA EL PROGRAMA
#    Vos: qué es éxito, p0, α, la cola (con hipotesis.py), la conclusión.
#    Programa: rc, α real, β, límites del intervalo y tamaños de muestra.
# =====================================================================

from scipy.stats import binom, norm
from scipy.optimize import brentq


# --- Las dos acumuladas del apunte ------------------------------------

# Gb(r/n ; p) = P(R ≥ r)   (acumulada derecha)
def Gb(r, n, p):
    return float(binom.sf(r - 1, n, p))


# Fb(r/n ; p) = P(R ≤ r)   (acumulada izquierda)
def Fb(r, n, p):
    return float(binom.cdf(r, n, p))


# --- Ensayo de hipótesis -----------------------------------------------

# CUÁNDO: "¿cumple la especificación?", "¿se puede asegurar que el
#         porcentaje supera / es menor que...?"
# PARA QUÉ: el valor crítico rc (cantidad de éxitos que marca la línea).
#   cola "derecha"   (H1: p > p0) -> el MENOR rc con Gb(rc/n ; p0) ≤ α
#                                    se rechaza si r ≥ rc
#   cola "izquierda" (H1: p < p0) -> el MAYOR rc con Fb(rc/n ; p0) ≤ α
#                                    se rechaza si r ≤ rc
# Devuelve None si con ese n no se puede rechazar nunca.
def valor_critico_proporcion(p0, n, alfa, cola):
    if cola == "derecha":
        for rc in range(0, n + 2):
            if Gb(rc, n, p0) <= alfa:
                return rc
        return None
    rc_valido = None
    for rc in range(0, n + 1):
        if Fb(rc, n, p0) <= alfa:
            rc_valido = rc
        else:
            break
    return rc_valido


# CUÁNDO: ya tenés r (de la muestra) y rc.
# PARA QUÉ: True = se rechaza H0; False = no se rechaza.
def rechaza_h0_proporcion(r, rc, cola):
    if rc is None:
        return False
    return r >= rc if cola == "derecha" else r <= rc


# CUÁNDO: para chequear la decisión por otro camino ("a posteriori").
# PARA QUÉ: α* = probabilidad de obtener lo observado (o algo más extremo)
#   si H0 fuera cierta. Se rechaza si α* ≤ α.
def alfa_a_posteriori(r, n, p0, cola):
    return Gb(r, n, p0) if cola == "derecha" else Fb(r, n, p0)


# CUÁNDO: querés todo el ensayo de una, impreso para la hoja.
# PARA QUÉ: imprime rc, α real, la condición de rechazo, α* y la decisión.
def ensayo_proporcion(p0, n, r, alfa, cola):
    rc = valor_critico_proporcion(p0, n, alfa, cola)
    print(f"p̂ = r/n = {r}/{n} = {r / n:.4f}")
    if rc is None:
        print("  Con este n no se puede rechazar H0 con ese α.")
        return False
    if cola == "derecha":
        print(f"  rc = {rc}   (α real = Gb({rc}/{n} ; {p0}) = {Gb(rc, n, p0):.4f})")
        print(f"  Condición de rechazo: si r ≥ {rc} -> se rechaza H0")
    else:
        print(f"  rc = {rc}   (α real = Fb({rc}/{n} ; {p0}) = {Fb(rc, n, p0):.4f})")
        print(f"  Condición de rechazo: si r ≤ {rc} -> se rechaza H0")
    a_post = alfa_a_posteriori(r, n, p0, cola)
    rechaza = rechaza_h0_proporcion(r, rc, cola)
    print(f"  r = {r}   α* (a posteriori) = {a_post:.4f}")
    print("  -> SE RECHAZA H0" if rechaza else "  -> NO se rechaza H0")
    return rechaza


# CUÁNDO: "¿cuál es la probabilidad de NO detectar / no cambiar / no
#         rechazar si el porcentaje en realidad es p1?"
# PARA QUÉ: β (error tipo II). La potencia ("probabilidad de detectar",
#   "de cambiar", "de rechazar") es 1 - β.
#   cola "derecha":   β = Fb(rc - 1 / n ; p1)
#   cola "izquierda": β = Gb(rc + 1 / n ; p1)
def beta_proporcion(rc, n, p1, cola):
    if cola == "derecha":
        return Fb(rc - 1, n, p1)
    return Gb(rc + 1, n, p1)


# CUÁNDO: "determinar el tamaño de muestra y la condición de rechazo"
#         cuando te dan α Y β (o una probabilidad de detectar).
# PARA QUÉ: el menor n (y su rc) que cumple las dos condiciones. Exacto.
#   p1 = el valor "malo" (o "bueno") que querés detectar con prob. 1 - β
def n_ensayo_proporcion(p0, p1, alfa, beta, cola, n_max=20000):
    for n in range(1, n_max + 1):
        rc = valor_critico_proporcion(p0, n, alfa, cola)
        if rc is not None and beta_proporcion(rc, n, p1, cola) <= beta:
            return n, rc
    return None


# --- Estimación (intervalos) -------------------------------------------

# CUÁNDO: "estimar el porcentaje de...", "con un N.C. del 95%",
#         "porcentaje máximo / mínimo".
# PARA QUÉ: límites exactos con la Binomial, como el apunte:
#   Gb(r/n ; A) = α/2   y   Fb(r/n ; B) = α/2
#   tipo = "bilateral" -> (A, B)
#          "maximo"    -> B  con Fb(r/n ; B) = α   (porcentaje máximo)
#          "minimo"    -> A  con Gb(r/n ; A) = α   (porcentaje mínimo)
def intervalo_proporcion(r, n, confianza, tipo="bilateral"):
    alfa = 1 - confianza
    cola = alfa / 2 if tipo == "bilateral" else alfa

    def limite_A(prob):
        return 0.0 if r == 0 else brentq(lambda p: Gb(r, n, p) - prob, 1e-12, 1 - 1e-12)

    def limite_B(prob):
        return 1.0 if r == n else brentq(lambda p: Fb(r, n, p) - prob, 1e-12, 1 - 1e-12)

    if tipo == "bilateral":
        return (limite_A(cola), limite_B(cola))
    if tipo == "maximo":
        return limite_B(cola)
    return limite_A(cola)


# CUÁNDO: necesitás el error o la relación de un intervalo (A, B).
# error = (B - A) / 2        relación R = B / A
def error_intervalo(A, B):
    return (B - A) / 2


def relacion_intervalo(A, B):
    return B / A


# CUÁNDO: "reducir en un X% el error / la relación anterior".
# PARA QUÉ: el nuevo valor objetivo. Ej: reducir(1.44546, 0.30) -> 1.0118
def reducir(valor, porcentaje):
    return valor * (1 - porcentaje)


# CUÁNDO: "¿cuántas unidades para un error de ...?" (aprox. Normal)
# PARA QUÉ: n = (Z / e)² · p̂ · (1 - p̂) + 1   (redondeado para arriba)
def n_para_error_proporcion(p_hat, e, confianza):
    z = norm.ppf(1 - (1 - confianza) / 2)
    return int(-(-((z / e) ** 2 * p_hat * (1 - p_hat) + 1) // 1))


# CUÁNDO: "¿cuántas unidades para reducir la relación de los límites?"
#         (aprox. Normal, fórmula del apunte de Estimación)
# PARA QUÉ: n = ((R + 1) / (R - 1) · Z)² · (1/p̂ - 1) + 1
def n_para_relacion_proporcion(p_hat, R, confianza):
    if R <= 1:
        raise ValueError("La relación objetivo tiene que ser mayor que 1.")
    z = norm.ppf(1 - (1 - confianza) / 2)
    n = ((R + 1) / (R - 1) * z) ** 2 * (1 / p_hat - 1) + 1
    return int(-(-n // 1))
