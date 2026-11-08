# =====================================================================
#  FORMATO de los bloques "Para la hoja" (no hace falta abrirlo)
# =====================================================================
#  Todos los bloques se imprimen igual:
#
#  ════════════════════════════════════════════════════════════
#    Título del bloque
#  ════════════════════════════════════════════════════════════
#
#    Sección
#        renglón
#        renglón
#
#    Decisión
#        → lo que se concluye
#  ════════════════════════════════════════════════════════════
# =====================================================================

ANCHO = 64


def titulo(texto):
    print()
    print("═" * ANCHO)
    print(f"  {texto}")
    print("═" * ANCHO)


def seccion(nombre):
    print()
    print(f"  {nombre}")


def linea(texto=""):
    print(f"      {texto}")


def flecha(texto):
    print(f"      → {texto}")


def fin():
    print("═" * ANCHO)
    print()
