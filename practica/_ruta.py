# Este archivo le dice a Python dónde está la carpeta "formulas".
# Cada ejercicio de esta carpeta lo importa con:  import _ruta
# No hace falta tocarlo.

import os
import sys

carpeta_del_repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, carpeta_del_repo)
