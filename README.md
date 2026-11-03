# Estadística Avanzada

Funciones en Python para resolver los ejercicios del segundo parcial de Estadística Aplicada (UADE, cátedra Dopazo).

## Cómo está organizado

```
estadistica-avanzada/
├── formulas/              ← las funciones, un archivo por tema
│   ├── hipotesis.py       ← guía para plantear H0/H1, cola, optimista/pesimista, α
│   ├── datos.py           ← n, media, desvío, proporción; contar datos bajo un valor
│   ├── fisher.py          ← comparar variabilidades de dos poblaciones (F)
│   ├── medias.py          ← comparar promedios (Pool, Welch, porcentajes, intervalos)
│   ├── proporciones.py    ← porcentajes: ensayo, β, intervalo, tamaño de muestra
│   └── chi_cuadrado.py    ← bondad de ajuste a un modelo y contingencia
├── practica/              ← un archivo por ejercicio
│   ├── _ruta.py           ← le dice a Python dónde está "formulas" (no tocar)
│   ├── guia_tema6_ej20.py ← EJEMPLO COMPLETO de un segundo parcial, resuelto
│   └── ...
├── requirements.txt
└── README.md
```

Cada archivo de `formulas` empieza con una **ficha teórica**: qué pregunta responde,
señales en la consigna, la idea, cosas que tenés que saber y qué decidís vos vs. qué calcula el programa.

## Cómo es el segundo parcial

Casi todos los segundos parciales desde 2014 tienen los mismos dos ejercicios:

**Ejercicio 1: una tabla con dos grupos (A y B)**

1. n, media y desvío de cada grupo → `datos.py`
2. ¿Varianzas iguales o distintas? → `metodo_para_medias()` en `medias.py` (usa `fisher.py`)
3. ¿Hay diferencia? ¿Más del X%? → `ensayo_medias()` en `medias.py`
4. Diferencia mínima / máxima esperada → `intervalo_diferencia()` en `medias.py`
5. ¿Sigue el modelo Gamma / Gumbel / Log-Normal? → `bondad_ajuste()` en `chi_cuadrado.py`
6. Porcentaje por debajo de un valor → `contar_debajo()` + `intervalo_proporcion()`

**Ejercicio 2: una proporción ("fallas máximo del 7%, de 95 unidades 8 fallan")**

1. ¿Cumple la especificación? → `ensayo_proporcion()` en `proporciones.py`
2. Estimar el porcentaje → `intervalo_proporcion()`
3. ¿Cuántas unidades más? → `n_para_error_proporcion()` o `n_para_relacion_proporcion()`
4. Probabilidad de detectar → `beta_proporcion()`

## Qué archivo abrir según la consigna

| Si la consigna... | Abrí |
|---|---|
| pregunta "¿se puede afirmar...?", "¿existen evidencias?", "¿cumple?", "¿cuál es la decisión?" | `hipotesis.py` (primero) |
| te da valores, una tabla con frecuencias o un conteo | `datos.py` |
| habla de variabilidad, desvío, dispersión, "más parejo" | `fisher.py` |
| compara promedios de A y B, "mayor en un X%", "diferencia mínima" | `medias.py` |
| habla de porcentaje de fallas, defectuosos, "en buenas condiciones" | `proporciones.py` |
| "¿se ajusta / sigue el modelo...?", "¿depende de...?" | `chi_cuadrado.py` |

## Requisitos (se instalan una sola vez)

1. **Python**: bajarlo de [python.org/downloads](https://www.python.org/downloads/).
   En el instalador, tildar **"Add python.exe to PATH"** antes de darle a Install.
2. **VS Code**: bajarlo de [code.visualstudio.com](https://code.visualstudio.com/).
   Adentro de VS Code, instalar la extensión **Python** (de Microsoft).
3. **Git**: bajarlo de [git-scm.com](https://git-scm.com/) (siguiente, siguiente, siguiente).
4. **scipy**: la librería que tiene adentro las tablas (F, t, normal, chi-cuadrado, binomial).
   En la terminal de VS Code (**Ctrl + ñ**), parada en la carpeta del repo:

   ```
   py -m pip install -r requirements.txt
   ```

## Cómo resolver un ejercicio

1. Crear un archivo nuevo en `practica/` (ej: `parcial_2023.py`).
2. Arriba de todo, poner `import _ruta` y traer solo las funciones que vayas a usar:

   ```python
   import _ruta
   from formulas.hipotesis import planteo
   from formulas.datos import n_agrupado, media_agrupada, desvio_agrupado
   from formulas.medias import metodo_para_medias, ensayo_medias
   ```

3. Cargar los datos de la consigna y llamar a las funciones.
   Mirá `practica/guia_tema6_ej20.py`: es un parcial entero hecho con el programa.
4. Correrlo con el botón ▶ de arriba a la derecha, o en la terminal: `py practica/parcial_2023.py`

Recordatorio: en Python los decimales van con **punto** (`0.084`, no `0,084`), y los porcentajes
entre 0 y 1 (`7%` → `0.07`).

## Antes del parcial

El parcial es **sin internet**. Unos días antes:

- Verificar que scipy esté instalado.
- Apagar el wifi y correr todos los ejercicios de `practica/` para confirmar que funcionan.

## Validación

Cada función se probó contra ejercicios resueltos de la guía y del apunte:

| Tema | Probado con | Resultado |
|---|---|---|
| Datos | Parcial 2017, guía VI.20 | medias y desvíos iguales a la resolución |
| Fisher | Guía IV.2 | F = 0,4855 · j = 0,7143 · jc = 0,5574 |
| Medias | Guía V.1 (Pool), V.3 (Welch), VI.20 a | dc, intervalos, n y h = 1,0506 iguales |
| Proporciones | Guía III.1, 2, 3, 9, 11, 12, 14, 15, VI.20 d | rc, β, intervalos y n iguales |
| Chi cuadrado | Apunte (Normal, Log-Normal, Gamma, contingencia), guía VI.15, 19, 20 | mismas decisiones y gl |

En chi cuadrado el χ² puede diferir en el segundo decimal respecto del apunte, porque el apunte
redondea las probabilidades a 4 decimales antes de calcular. La decisión no cambia.

**A confirmar con el profe:** cuando el valor de corte cae en el medio de una clase
(ej: mínimo de 22 con clases 21–23), `contar_debajo()` reparte esa clase en forma proporcional.
