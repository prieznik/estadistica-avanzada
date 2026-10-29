# Estadística Avanzada

Funciones en Python para resolver los ejercicios de Estadística Aplicada (UADE).

- `formulas.py`: el kit de funciones. Solo funciones, sin datos de ningún ejercicio.
- Los demás archivos `.py`: un ejercicio cada uno. Traen las funciones con `import`.

## Requisitos (se instalan una sola vez)

1. **Python**: bajarlo de [python.org/downloads](https://www.python.org/downloads/).
   En el instalador, tildar **"Add python.exe to PATH"** antes de darle a Install.
2. **VS Code**: bajarlo de [code.visualstudio.com](https://code.visualstudio.com/).
   Adentro de VS Code, instalar la extensión **Python** (de Microsoft).
3. **Git**: bajarlo de [git-scm.com](https://git-scm.com/) (siguiente, siguiente, siguiente).
   Sirve para bajar y subir los cambios del repo.
4. **scipy**: la librería que tiene adentro las tablas (F, t, normal, chi-cuadrado).
   En la terminal de VS Code (**Ctrl + ñ**):

   ```
   py -m pip install -r requirements.txt
   ```

   (Es lo mismo que `py -m pip install scipy`.)

## Cómo correr un ejercicio

1. Abrir la carpeta del repo en VS Code.
2. Abrir el archivo del ejercicio (por ejemplo `parcial_2017.py`).
3. Darle al botón ▶ de arriba a la derecha, o en la terminal: `py parcial_2017.py`

`formulas.py` tiene que estar en la misma carpeta que el ejercicio.

## Antes del parcial

El parcial es **sin internet**. Unos días antes:

- Verificar que scipy esté instalado.
- Apagar el wifi y correr todos los ejercicios para confirmar que funcionan.

## Ejercicios de prueba

| Archivo | Qué prueba | Resultado esperado |
|---|---|---|
| `parcial_2017.py` | media y desvío de tablas agrupadas | media A = 206,52 · media B = 229 |
| `guia_tema4_ej2.py` | valores de la tabla F | 0,4855 · 2,2776 · 0,3932 |
