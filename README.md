# Estadística Aplicada — segundo parcial

Funciones en Python para resolver los ejercicios del segundo parcial de Estadística Aplicada (UADE, cátedra Dopazo): comparación de dos poblaciones (Fisher, t de Student, Z), proporciones (Bernoulli/Binomial) y Chi cuadrado.

El programa **hace las cuentas e imprime un bloque "Para la hoja"** con las fórmulas, el valor crítico, la regla de decisión y la decisión. **El planteo lo hacés vos**: qué herramienta, cuál es la población 1, H0, H1, la cola y la conclusión en palabras del problema.

## Instalación (una sola vez)

1. **Python** ([python.org/downloads](https://www.python.org/downloads/)). En el instalador, tildá **"Add python.exe to PATH"**.
2. **VS Code** ([code.visualstudio.com](https://code.visualstudio.com/)) con la extensión **Python** (de Microsoft).
3. **Git** ([git-scm.com](https://git-scm.com/)).
4. **Bajar el repo:** en VS Code, Ctrl + Shift + P → **Git: Clone** → pegar la dirección del repo → elegir una carpeta.
5. **scipy** (la librería con las tablas): en la terminal de VS Code (Ctrl + ñ), parada en la carpeta del repo:

   ```
   py -m pip install -r requirements.txt
   ```

**Funciona sin internet** una vez instalado. Antes del parcial, apagá el wifi y corré `practica/ejemplo_parcial_resuelto.py` para confirmarlo.

## Cómo está organizado

```
├── formulas/                       ← todas las funciones (no hace falta abrirlas)
├── practica/
│   ├── _ruta.py                    ← no tocar
│   ├── plantilla_ejercicio.py      ← copiala para cada ejercicio nuevo
│   └── ejemplo_parcial_resuelto.py ← un segundo parcial completo, de referencia
├── requirements.txt
└── README.md
```

## Cómo resolver un ejercicio

1. **Copiá `practica/plantilla_ejercicio.py`** y renombrala (ej: `ej01_fallas.py`).
2. **Planteo en papel** (los comentarios de arriba de la plantilla): herramienta, población 1 o qué cuenta p, H0, H1, cola y α.
3. **Cargá los datos y llamá a la función** que corresponde. Arriba del archivo ya está:

   ```python
   import _ruta
   from formulas import *
   ```

   Con eso tenés **todas** las funciones. La plantilla está ordenada así: **1. Consigna**, **2. Ayuda** (la lista de funciones por tema, comentada, para no tener que buscarla), **3. Datos de contexto** (planteo en papel + tablas), **4. Resolución** (las llamadas a las funciones y la conclusión de cada punto).
4. **Corré** con el botón ▶ (arriba a la derecha).
5. **Copiá el bloque "Para la hoja"** y escribí la conclusión en palabras del problema.

Mirá `practica/ejemplo_parcial_resuelto.py`: es un parcial entero hecho así, con el planteo en papel en los comentarios y lo que dice la guía al lado de cada resultado.

### ¿Cómo sabe el programa cuáles son H0 y H1?

No lee la consigna: lo saca de **lo que vos le pasás**.

```python
ensayo_proporcion(0.05, 120, 9, 0.05, "derecha")
#                 p0    n    r  α     cola
```

- `cola = "derecha"` → H0: p ≤ p0, H1: p > p0
- `cola = "izquierda"` → H0: p ≥ p0, H1: p < p0
- (en promedios también existe `"bilateral"` → H1: ≠)

La cola sale del **signo de H1**, que decidís vos leyendo la consigna. Si le pasás la cola equivocada, te arma las hipótesis equivocadas. Si escribís una cola que no existe (por ejemplo `"maximo"`), te avisa.

## Qué función usar

| Si la consigna... | Función |
|---|---|
| da una tabla con intervalos y frecuencias | `n, x, s = resumen_tabla(tabla, "Línea A")` (imprime las fórmulas) |
| compara promedios de A y B (paso previo: ¿varianzas iguales?) | `metodo_para_medias(n1, x1, s1, n2, x2, s2)` → "pool" o "welch" |
| "¿se puede asegurar que A produce más que B?", "más de un 10%" | `ensayo_medias(metodo, delta0, alfa, n1, x1, s1, n2, x2, s2, cola, h=1)` |
| da los σ "según registros históricos" | `ensayo_medias("conocidos", ...)` (usa Z, sin Fisher) |
| "diferencia mínima / máxima esperada" | `intervalo_diferencia(metodo, confianza, ..., tipo="minimo")` |
| "más regular", "menor variabilidad", "reducir el desvío" | `ensayo_varianzas(phi0, alfa, n_arriba, s_arriba, n_abajo, s_abajo, cola)` |
| "fallas máximo del 7%... ¿cumple?" | `ensayo_proporcion(p0, n, r, alfa, cola)` |
| "estimar el porcentaje de..." | `intervalo_proporcion(r, n, confianza, tipo)` |
| "% por debajo de 14.000 hs" (con tabla) | `contar_debajo(tabla, 14)` y después `intervalo_proporcion` |
| "¿cuántas unidades más?" | `n_para_error_proporcion` o `n_para_relacion_proporcion` (+ `reducir`) |
| "probabilidad de (no) detectar si en realidad es..." | `beta_proporcion(rc, n, p1, cola)` |
| "¿sigue un modelo Normal / Gamma / Gumbel...?" | `bondad_ajuste(tabla, modelo, alfa, parametros=None)` |
| tabla de doble entrada, "¿depende de...?" | `contingencia(tabla, alfa)` |

Recordá:
- Las tablas se cargan como `[(desde, hasta, frecuencia), ...]`.
- Decimales con **punto** (`0.05`) y porcentajes entre 0 y 1 (`7%` → `0.07`).
- "Más de un 10%" → `h = 1.10`; "un 10% menos" → `h = 0.90`.

## Validación

Cada función se probó contra ejercicios resueltos de la guía y del apunte (Temas III a VI): valores críticos, intervalos, tamaños de muestra y decisiones coinciden. En Chi cuadrado el χ² puede diferir en el segundo decimal respecto del apunte, porque el apunte redondea antes de calcular; la decisión no cambia.

**A confirmar con el profesor:** cuando el valor de corte cae en el medio de una clase, `contar_debajo` reparte esa clase en forma proporcional.

Es una ayuda para hacer las cuentas: revisá siempre que el planteo sea el correcto.
