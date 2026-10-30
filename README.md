# Estadística Avanzada

Funciones en Python para resolver los ejercicios de Estadística Aplicada (UADE).

## Cómo está organizado

```
estadistica-avanzada/
├── formulas/          ← las funciones, un archivo por tema
│   ├── hipotesis.py   ← guía para plantear H0/H1, cola, optimista/pesimista, α
│   ├── datos.py       ← n, media, desvío y proporción de la consigna
│   └── fisher.py      ← comparar variabilidades de dos poblaciones (F)
├── practica/          ← un archivo por ejercicio
│   ├── _ruta.py       ← le dice a Python dónde está "formulas" (no tocar)
│   ├── parcial_2017.py
│   └── guia_tema4_ej2.py
├── requirements.txt
└── README.md
```

Cada archivo de `formulas` empieza con una **ficha teórica**: qué pregunta responde,
señales en la consigna, cosas que tenés que saber y qué decidís vos vs. qué calcula el programa.

## Qué archivo abrir según la consigna

| Si la consigna... | Abrí |
|---|---|
| pregunta "¿se puede afirmar...?", "¿existen evidencias?", "¿cumple?", "¿cuál es la decisión?" | `formulas/hipotesis.py` (primero) |
| te da valores, una tabla con frecuencias o un conteo ("8 de 95 con fallas") | `formulas/datos.py` |
| habla de variabilidad, desvío, dispersión, "más parejo", "reducir el desvío" | `formulas/fisher.py` |
| compara dos grupos A y B en una tabla (primer paso: ¿varianzas iguales?) | `formulas/fisher.py` |

## Requisitos (se instalan una sola vez)

1. **Python**: bajarlo de [python.org/downloads](https://www.python.org/downloads/).
   En el instalador, tildar **"Add python.exe to PATH"** antes de darle a Install.
2. **VS Code**: bajarlo de [code.visualstudio.com](https://code.visualstudio.com/).
   Adentro de VS Code, instalar la extensión **Python** (de Microsoft).
3. **Git**: bajarlo de [git-scm.com](https://git-scm.com/) (siguiente, siguiente, siguiente).
   Sirve para bajar y subir los cambios del repo.
4. **scipy**: la librería que tiene adentro las tablas (F, t, normal, chi-cuadrado).
   En la terminal de VS Code (**Ctrl + ñ**), parada en la carpeta del repo:

   ```
   py -m pip install -r requirements.txt
   ```

## Cómo resolver un ejercicio

1. Crear un archivo nuevo en `practica/` (ej: `parcial_2023.py`).
2. Arriba de todo, poner:

   ```python
   import _ruta
   from formulas.hipotesis import planteo
   from formulas.datos import media_agrupada, desvio_agrupado
   from formulas.fisher import cociente_varianzas, valor_critico, rechaza_h0
   ```

   (solo las funciones que vayas a usar).
3. Cargar los datos de la consigna y llamar a las funciones.
4. Correrlo con el botón ▶ de arriba a la derecha, o en la terminal: `py practica/parcial_2023.py`

Recordatorio: en Python los decimales van con **punto** (`0.084`, no `0,084`).

## Antes del parcial

El parcial es **sin internet**. Unos días antes:

- Verificar que scipy esté instalado.
- Apagar el wifi y correr todos los ejercicios de `practica/` para confirmar que funcionan.

## Ejercicios de prueba

| Archivo | Qué prueba | Resultado esperado |
|---|---|---|
| `practica/parcial_2017.py` | media y desvío de tablas agrupadas | media A = 206,52 · media B = 229 |
| `practica/guia_tema4_ej2.py` | tabla F y ensayo de varianzas | F: 0,4855 · 2,2776 · 0,3932 — j = 0,7143, jc = 0,5574, no se rechaza |
