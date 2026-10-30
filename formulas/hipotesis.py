# =====================================================================
#  HIPÓTESIS - Cómo plantear un ensayo de hipótesis
# =====================================================================
#
#  Este archivo es sobre todo una GUÍA para leer la consigna.
#  Tiene una sola función, planteo(), que te escribe H0, H1 y la cola.
#  Basado en el apunte de Dopazo (Ensayos de Hipótesis, págs. 21-24).
#
# ---------------------------------------------------------------------
#  1. ¿ES UN ENSAYO DE HIPÓTESIS?
# ---------------------------------------------------------------------
#    SÍ, si la consigna te pide DECIDIR algo:
#      "¿se puede afirmar / asegurar / probar que...?"
#      "¿existen evidencias...?"   "¿los datos son concluyentes?"
#      "¿considera que el proceso cumple...?"
#      "¿cuál es la decisión recomendada?"   "¿existen diferencias...?"
#    NO, si te pide:
#      "estimar..." / "con un N.C. del 95%"   -> intervalo de confianza
#      "¿cuántas piezas más...?"              -> tamaño de muestra
#      "¿cuál es la probabilidad de no detectar / no cambiar...?"  -> β
#
# ---------------------------------------------------------------------
#  2. REGLAS QUE NUNCA CAMBIAN
# ---------------------------------------------------------------------
#    - H0 siempre lleva el igual:   =   ≤   ≥
#    - H1 es lo contrario de H0:    ≠   >   <
#    - Las hipótesis hablan de la POBLACIÓN (μ, σ, p, ψ), nunca de la
#      muestra (x̄, S, p̂).
#    - Solo se dice "se rechaza H0" o "no se rechaza H0".
#      Nunca "se acepta H0".
#    - La conclusión fuerte es el RECHAZO. Si no se rechaza, solo
#      decís "no hay pruebas suficientes".
#    - Error tipo I (α): rechazar H0 siendo verdadera. Es el más grave.
#      (en control de procesos: "riesgo del proveedor")
#    - Error tipo II (β): no rechazar H0 siendo falsa.
#      (en control de procesos: "riesgo del consumidor")
#
# ---------------------------------------------------------------------
#  3. ¿OPTIMISTA O PESIMISTA?  (qué pongo en H0)
# ---------------------------------------------------------------------
#    OPTIMISTA -> H0 = "todo está bien / cumple"
#      Cuándo: control de producción, control de recepción de lotes,
#      muestreos periódicos o rutinarios.
#      Por qué: solo querés rechazar el lote o parar el proceso si hay
#      pruebas MUY fuertes de que está mal.
#      Ej: "porcentaje de fallas máximo del 7%. ¿Cumple?"
#          H0: p ≤ 0,07 (cumple)   H1: p > 0,07 (no cumple)
#
#    PESIMISTA -> H0 = "no sirve / no mejora"
#      Cuándo: inversión con riesgo económico (comprar un equipo,
#      cambiar el proceso para MEJORAR), algo que se hace una sola vez.
#      Por qué: solo invertís si hay pruebas MUY fuertes de que es bueno.
#      Ej: "cambiar la aleación para bajar el desvío más de un 20%"
#          H0: σP/σA ≥ 0,8 (no mejora)   H1: σP/σA < 0,8 (mejora)
#
#    EXCEPCIÓN: si el cambio es para ABARATAR costos (y no para mejorar),
#    puede ser optimista.
#
#    COMPARAR DOS POBLACIONES (A vs B, lo del segundo parcial):
#      el apunte dice que acá NO hay criterio optimista/pesimista.
#      H1 = lo que se quiere probar.
#
#    Si no sabés, el apunte dice probar en este orden:
#      1º) ¿es optimista o pesimista?
#      2º) ¿qué error es más grave? Ese tiene que ser el error tipo I.
#      3º) ¿qué se quiere probar? -> eso va en H1  (último recurso)
#
# ---------------------------------------------------------------------
#  4. ¿COLA DERECHA, IZQUIERDA O BILATERAL?
# ---------------------------------------------------------------------
#    Mirá SOLO el signo de H1:
#      H1 con  >   -> cola DERECHA
#      H1 con  <   -> cola IZQUIERDA
#      H1 con  ≠   -> BILATERAL (las dos colas)
#
#    Palabras de la consigna -> signo de lo que se quiere probar:
#      "más", "mayor", "supera", "aumenta", "excede", "más irregular"  ->  >
#      "menos", "menor", "reduce", "disminuye", "más parejo"            ->  <
#      "existen diferencias", "es distinto"                            ->  ≠
#
#    OJO con "máximo" y "mínimo": suelen describir lo que CUMPLE,
#    o sea H0 en un planteo optimista.
#      "fallas máximo del 7%"  -> H0: p ≤ 0,07  -> H1: p > 0,07 -> derecha
#
# ---------------------------------------------------------------------
#  5. ¿CUÁL ES α?
# ---------------------------------------------------------------------
#    1) Fijate qué ACCIÓN pasa si rechazás H0 (comprar, cambiar,
#       rechazar el lote, efectuar la faena...).
#    2) α = el riesgo de hacer esa acción EQUIVOCADAMENTE.
#       "riesgo del 1% de efectuar equivocadamente la faena" -> α = 0,01
#    3) Si te dan una "probabilidad" o "certeza" de NO hacerla cuando no
#       corresponde, α es el complemento:
#       "certeza del 99% de no modificar si no se consigue" -> α = 0,01
#    4) El riesgo de NO hacer la acción cuando convenía es β.
#
# ---------------------------------------------------------------------
#  6. CHECKLIST PARA LA HOJA DEL PARCIAL
# ---------------------------------------------------------------------
#    [ ] Parámetro que comparo (μ, σ, p, ψ = σ1/σ2, δ = μ1 - μ2)
#    [ ] Criterio y justificación (optimista / pesimista / lo que se
#        quiere probar)
#    [ ] H0 y H1
#    [ ] α
#    [ ] Distribución que uso y por qué (F, t, Normal, Binomial...)
#    [ ] Valor crítico y condición de rechazo
#    [ ] Regla de decisión: qué se hace si se rechaza
#    [ ] Comparar la muestra con el valor crítico
#    [ ] Conclusión EN PALABRAS DEL PROBLEMA
#        (no alcanza con "se rechaza H0": decí qué significa)
# =====================================================================


# CUÁNDO: ya decidiste qué querés probar (H1) leyendo la consigna.
# PARA QUÉ: te escribe H0 y H1 para la hoja y te devuelve la cola,
#           que después le pasás a valor_critico() y rechaza_h0().
#   parametro = texto de lo que comparás, ej: "σB/σA" o "μ" o "p"
#   signo_h1  = ">" , "<" o "≠"  (el signo de lo que se quiere probar)
#   valor     = el número de la hipótesis, ej: 1 o 0.8 o 0.07
#
# Ejemplo:
#   cola = planteo("σB/σA", ">", 1)
#   -> imprime  H0: σB/σA ≤ 1   H1: σB/σA > 1   cola derecha
#   -> cola vale "derecha"
def planteo(parametro, signo_h1, valor):
    if signo_h1 == ">":
        signo_h0, cola = "≤", "derecha"
    elif signo_h1 == "<":
        signo_h0, cola = "≥", "izquierda"
    else:
        signo_h0, cola = "=", "bilateral"

    print(f"H0: {parametro} {signo_h0} {valor}")
    print(f"H1: {parametro} {signo_h1} {valor}")
    print(f"Cola: {cola}")
    return cola
