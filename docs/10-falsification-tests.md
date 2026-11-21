# 10 — Pruebas de falsación y aceptación de un modelo

## Puertas lógicas

G1. **Dimensiones y marcos.** Toda ecuación mantiene dimensiones correctas; densidades Einstein/Jordan/ρ_* no se confunden y la acción no cuenta materia dos veces.

G2. **Soluciones.** Existen mínimos, perfiles de screening, soluciones de Friedmann y bounce gravitatorio con condiciones de contorno explícitas. No inferir soluciones de una gráfica del potencial.

G3. **Estabilidad.** Sin fantasmas, gradientes inestables ni acoplamientos que invaliden la EFT; controlar naturalidad radiativa o exponer el ajuste fino.

G4. **Recuperación local.** La teoría pasa al menos las pruebas de quinta fuerza y relatividad relevantes. El coeficiente β=M_Pl dlnA/dχ se calcula en el entorno correcto.

G5. **Historia térmica.** Energía para recalentamiento suficiente; calcular η_B y fluctuaciones, no asumirlos porque existe una pared de burbuja.

G6. **Datos cosmológicos.** Predicciones diferenciables de ΛCDM y comparación reproducible con observaciones. Explicitar los priors y las degeneraciones.

G7. **Entropía y causalidad.** Si se reclama continuidad entre universos, identificar canal informacional físico y compatibilidad con horizontes y termodinámica; de lo contrario clasificarlo como especulación.

## Caso numérico mínimo

Ejecutar python3 models/vpt_benchmark.py. Debe verificar los extremos y diferencias de energía del potencial de sexto orden y las escalas del ejemplo. Es una prueba **algebraica**, no validación empírica.

## Criterios de descarte

Una versión candidata queda descartada en el régimen elegido si viola dimensiones, carece de mínimo/túnel descrito, requiere simultáneamente masas irreconciliables para un único campo, predice una fuerza sin apantallamiento incompatible con límites o no produce la historia térmica exigida mientras reclama haberla explicado. Reformular hipótesis no es falsar la naturaleza: conservar histórico de parámetros y casos fallidos.

## Publicación

Separar en cada resultado [LITERATURA], [DERIVACIÓN], [BENCHMARK], [HIPÓTESIS] y [ESPECULACIÓN]. Declarar cuando una predicción dependa de suponer el valor que después se presenta como resultado.
