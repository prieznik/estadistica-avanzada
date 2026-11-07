# Estadística Avanzada

Funciones en Python para resolver los ejercicios del segundo parcial de Estadística Aplicada (UADE, cátedra Dopazo).

## Cómo está organizado

```
estadistica-avanzada/
├── formulas/                       ← todas las funciones (no hace falta abrirlas)
├── practica/
│   ├── _ruta.py                    ← no tocar
│   ├── plantilla_ejercicio.py      ← copiala para cada ejercicio nuevo
│   └── ejemplo_parcial_resuelto.py ← un segundo parcial completo, de referencia
├── PASOS.md
├── requirements.txt
└── README.md
```

## Cómo resolver un ejercicio

1. Copiá `practica/plantilla_ejercicio.py` y renombrala (ej: `ej01_fallas.py`).
2. Completá el planteo en papel (está en los comentarios de arriba).
3. Arriba del archivo ya está todo lo que necesitás:

   ```python
   import _ruta
   from formulas import *
   ```

   Con eso tenés **todas** las funciones. Si no te acordás cuál usar, escribí `ayuda()` y corré el archivo: te muestra la lista por tema.
4. Corré el archivo con el botón ▶ (arriba a la derecha).

Recordatorio: decimales con **punto** (`0.05`) y porcentajes entre 0 y 1 (`7%` → `0.07`).

## Requisitos (se instalan una sola vez)

1. **Python** ([python.org](https://www.python.org/downloads/)), tildando "Add python.exe to PATH".
2. **VS Code** ([code.visualstudio.com](https://code.visualstudio.com/)) con la extensión **Python**.
3. **Git** ([git-scm.com](https://git-scm.com/)).
4. **scipy**: en la terminal de VS Code (Ctrl + ñ), en la carpeta del repo:

   ```
   py -m pip install -r requirements.txt
   ```

## Antes del parcial

El parcial es **sin internet**: unos días antes, apagá el wifi y corré `ejemplo_parcial_resuelto.py` para confirmar que todo funciona.

## Validación

Cada función se probó contra ejercicios resueltos de la guía y del apunte (Temas III a VI). En chi cuadrado el χ² puede diferir en el segundo decimal respecto del apunte, porque el apunte redondea antes de calcular; la decisión no cambia.
