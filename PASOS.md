# Pasos por tipo de pregunta — Segundo parcial

Cómo se usa: leé el punto de la consigna, buscá abajo qué tipo de pregunta es
(por las **señales**) y seguí los pasos de ese tipo, en orden.

Siempre, antes de empezar un ejercicio: sacá **n, media y desvío** de cada grupo
(o **r** y **n** si es un conteo).

---

## 0. ¿Qué tipo de pregunta es?

| Si la consigna dice... | Es | Andá a |
|---|---|---|
| "¿se puede afirmar que A es más **variable / irregular / parejo**...?" | Comparar variabilidad | **1** |
| "¿existen **diferencias**...?", "¿A **produce más** que B?", "¿se aconseja cambiar?" | Comparar promedios | **2** |
| "más de un **X%** de A respecto de B" | Comparar promedios con porcentaje | **2** (con h) |
| "diferencia **mínima / máxima esperada**", "estimar la diferencia" | Intervalo de la diferencia | **3** |
| "¿qué **diferencia porcentual mínima** se puede garantizar?" | Porcentaje garantizado | **4** |
| "¿se **ajusta / sigue / se comporta** según el modelo Normal, Gamma...?" | Bondad de ajuste | **5** |
| "porcentaje de fallas **máximo del X%**... ¿**cumple**?" | Ensayo de una proporción | **6** |
| "**estimar el porcentaje** de unidades buenas / defectuosas" | Intervalo de una proporción | **7** |
| "estimar el porcentaje que **no cumple el mínimo** de X" (con tabla) | Contar y estimar proporción | **8** |
| "¿**cuántas unidades más** para reducir el error / la relación?" | Tamaño de muestra | **9** |
| "¿probabilidad de **(no) detectar** si en realidad el porcentaje es X?" | β o potencia | **10** |

---

## 1. Comparar variabilidad (F de Fisher)

1. **Población arriba:** la que nombra la frase. Si solo preguntan si son iguales, la de **desvío más grande**.
2. **Parámetro:** φ = σarriba / σabajo. Si hay porcentaje ("reducir en más de un 20%"), φ0 = 0,8. Si no, φ0 = 1.
3. **Hipótesis:** H1 = lo que se quiere probar ("más variable" → φ > φ0). H0 = lo contrario.
4. **Cola:** H1 con > → derecha. H1 con < → izquierda.
5. **Valor crítico:** j²c = φ0² · F (gl: n − 1 de la de arriba ; n − 1 de la de abajo).
6. **Muestra:** j² = Sarriba² / Sabajo².
7. **Comparar:** ¿j² cruza j²c? Sí → se rechaza H0. No → no se rechaza.
8. **Conclusión** en palabras del problema.

Programa: `fisher.py` → `valor_critico()`, `cociente_varianzas()`, `rechaza_h0()`

---

## 2. Comparar promedios de dos grupos (t de Student)

1. **Paso previo: ¿misma variabilidad?** Hacé el **tipo 1** con φ0 = 1, desvío más grande arriba, cola derecha, **α = 10%**.
   - No se rechaza → varianzas iguales → **Pool**
   - Se rechaza → varianzas distintas → **Welch**
2. **Población 1:** la que nombra la frase ("N produce más que A" → N es la 1).
3. **¿Hay porcentaje?**
   - No → parámetro δ = μ1 − μ2
   - Sí ("más de un 10%") → h = 1,10 → parámetro δ* = μ1 − h · μ2
4. **Hipótesis:** H1 = lo que se quiere probar (ej: δ* > 0). H0 = lo contrario (δ* ≤ 0).
5. **Cola:** > → derecha. < → izquierda. "existen diferencias" (≠) → bilateral.
6. **Valor crítico:** dc = δ0 ± t · (error estándar). Lo calcula el programa con el método del paso 1.
7. **Muestra:** d = x̄1 − h · x̄2 (si no hay porcentaje, h = 1).
8. **Comparar:** ¿d cruza dc? Sí → se rechaza H0. No → no se rechaza.
9. **Conclusión** en palabras del problema ("se aconseja comprar" / "no hay pruebas suficientes").

Programa: `medias.py` → `metodo_para_medias()` (paso 1) y `ensayo_medias()` (pasos 6 a 8)

---

## 3. Diferencia mínima / máxima esperada (intervalo)

1. **Paso previo:** igual que el paso 1 del **tipo 2** (Pool o Welch).
2. **Población 1:** la que nombra la frase ("de B respecto de A" → B es la 1).
3. **¿Qué límite piden?**
   - "mínima" → solo el límite de abajo (A)
   - "máxima" → solo el límite de arriba (B)
   - "estimar la diferencia" → los dos
4. **Calcular:** d ± t · (error estándar). No hay hipótesis.
5. **Conclusión:** "con un 95% de confianza, la diferencia es de al menos ___".

Programa: `medias.py` → `intervalo_diferencia(..., tipo="minimo")`

---

## 4. Diferencia porcentual mínima garantizada

1. **Paso previo:** igual que el paso 1 del **tipo 2**.
2. **Población 1:** la que es mayor.
3. **Buscar el h** que justo toca la línea: μ1 > h · μ2.
4. **Conclusión:** "se puede garantizar un aumento mínimo de (h − 1) · 100 %".

Programa: `medias.py` → `h_limite()`

---

## 5. ¿Sigue un modelo? (bondad de ajuste, Chi cuadrado)

1. **Hipótesis:** H0 = "los datos siguen el modelo ___". Cola siempre derecha. α = 5% si no lo dan.
2. **Parámetros:** ¿te los dan? → p = 0. ¿No? → se estiman de x̄ y S → p = 2.
3. **Esperados:** Fe = n · P(clase), según el modelo.
4. **Juntar** las clases con Fe menor a 5 con su vecina.
5. **Grados de libertad:** gl = k − 1 − p (k = clases que quedaron).
6. **Muestra:** χ² = suma de (Fo − Fe)² / Fe.
7. **Comparar** con χ²(1 − α ; gl). Lo supera → se rechaza H0.
8. **Conclusión:** se rechaza → "no sigue el modelo". No se rechaza → "el modelo es un buen candidato".

Programa: `chi_cuadrado.py` → `bondad_ajuste()`

---

## 6. ¿Cumple un porcentaje? (ensayo de una proporción)

1. **Éxito:** qué estás contando (ej: unidades con falla).
2. **Criterio:** control de rutina → optimista (H0 = cumple). Inversión o mejora → pesimista (H0 = no sirve).
3. **Hipótesis:** "fallas máximo 7%" → H0: p ≤ 0,07 (cumple), H1: p > 0,07.
4. **Cola:** > → derecha. < → izquierda.
5. **Valor crítico:** rc = la cantidad de éxitos que marca la línea (Binomial).
6. **Comparar:** r (lo observado) contra rc. Cola derecha: r ≥ rc → se rechaza H0.
7. **Conclusión** en palabras del problema.

Programa: `proporciones.py` → `ensayo_proporcion()`

---

## 7. Estimar un porcentaje (intervalo de una proporción)

1. **Éxito:** ojo con qué piden. "Buenas condiciones" → r = n − fallas.
2. **¿Qué límites?** Bilateral, solo máximo o solo mínimo.
3. **Calcular** con la Binomial. No hay hipótesis.
4. **Conclusión:** "entre ___ % y ___ %, con un 95% de confianza".

Programa: `proporciones.py` → `intervalo_proporcion()`

---

## 8. Porcentaje de una tabla que no cumple un valor

1. **Contar r:** cuántos datos de la tabla quedan por debajo (o por encima) del valor.
2. **n:** el total de ese grupo.
3. Seguir con el **tipo 7**.

Programa: `datos.py` → `contar_debajo()` y después `intervalo_proporcion()`

---

## 9. ¿Cuántas unidades más?

1. **¿Qué hay que reducir?** El error (e) o la relación de los límites (R = B / A).
2. **Valor nuevo:** "reducir en un 30%" → valor actual · 0,70.
3. **Calcular n** con la fórmula (aproximación Normal).
4. **Respuesta:** "unidades más" = n nuevo − n actual.

Programa: `proporciones.py` → `n_para_error_proporcion()` o `n_para_relacion_proporcion()`

---

## 10. Probabilidad de (no) detectar (β)

1. **Primero** hacé el **tipo 6** hasta tener rc.
2. **p1:** el valor "en realidad" que da la consigna.
3. **β** = probabilidad de **no** rechazar H0 si el valor real es p1.
4. "Probabilidad de **detectar** / de cambiar / de rechazar" → la respuesta es 1 − β.

Programa: `proporciones.py` → `beta_proporcion()`
