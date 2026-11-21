# 12 — GHRT-VPT: modelo de transición, cálculos y distinción entre burbujas y universos

**Fecha:** 2026-11-21. **Estado:** modelo de juguete matemático; no representa una transición real observada ni una tecnología viable.

## 1. De dónde surge

Hipótesis original del autor: un fondo cósmico expansivo persistente podría originar fluctuaciones/transiciones de vacío que den lugar a historias locales tipo Big Bang, sin que todo el espacio parental deje de existir. La expansión acelerada en sí misma no es una “tensión” acumulativa que necesariamente se rompa. Debe existir un potencial con estados diferentes, una transición dinámica y una solución gravitatoria coherente. El antecedente más cercano es la inflación eterna de falso vacío, no el Steady State clásico.

El potencial symmetron cuadrático-cuártico de GHRT anterior ofrece una transición continua, no un estado falso separado por barrera. Para estudiar nucleación de primer orden se define un potencial distinto.

## 2. Potencial de sexto orden y mínimos

En unidades naturales ℏ=c=1, un escalar canónico χ, y=χ/f:

U_eff(y;ρ_*) = U_0 + E_*⁴ [a(ρ_*)y²/2 − y⁴/4 + y⁶/6],
a(ρ_*) = a_0 + ρ_* f²/(M²E_*⁴).

Aquí ρ_* representa la densidad auxiliar de **materia no relativista** usada en el potencial efectivo; es incorrecto sustituir sin más por toda la densidad de radiación.

W(y)=ay²/2−y⁴/4+y⁶/6; W'(y)=y(a−y²+y⁴).
Los extremos no triviales satisfacen y²_±=[1±√(1−4a)]/2 cuando 0≤a≤1/4.

Si 0<a<3/16, y=0 es falso mínimo metastable, y_− barrera y y_+ mínimo verdadero. A a=3/16 hay degeneración energética entre y=0 y y_+; a→0 hace que y=0 pierda estabilidad local. Si 3/16<a<1/4, los dos mínimos pueden coexistir con origen como mínimo más profundo, pero ya no se está describiendo la misma dirección favorable de decaimiento.

Benchmark no ajustado a datos: a=0.180;
y_−=0.48520600665;
y_+=0.87439986911;
W(y_−)=+0.00950675306;
W(y_+)=−0.002840086392;
ΔU=0.002840086392 E_*⁴.

Estos números prueban sólo la estructura del potencial.

## 3. Túnel cuántico y sus límites

Γ≈𝒜e^(−B), donde B=S_E[bounce]−S_E[falso] y 𝒜 es prefactor de fluctuaciones por cuatro-volumen.

En la **aproximación plana, pared delgada**:
B_flat≈27π²σ⁴/(2ΔU³);
R_flat≈3σ/ΔU.

Para a=3/16 la tensión entre estados degenerados es σ=9 f E_*²/(64√3)=0.0811898816 f E_*².
Si esta tensión degenerada se utiliza como aproximación en a=0.180,
B_flat≈252724.00372 (f/E_*)⁴.

La pared delgada y espacio plano pueden fallar cuando la barrera no es muy alta respecto de ΔU, cuando hay gravedad, cuando R se acerca al radio de Hubble y con efectos térmicos; todos los resultados precedentes están sujetos a esas advertencias.

## 4. Ejemplo numérico con la escala de energía oscura actual

Parámetros ΛCDM de referencia: H_0=67.4 km/s/Mpc, Ω_m=0.315, Ω_Λ=0.685:
H_0≈2.1843×10⁻¹⁸ s⁻¹; H_∞≈1.8078×10⁻¹⁸ s⁻¹;
u_Λ≈5.2532×10⁻¹⁰ J/m³; E_*=(u_Λ ℏ³c³)^(1/4)≈2.240365 meV.

Si se **elige** una tasa objetivo ε=Γ/H⁴=0.001 y se **supone** el prefactor 𝒜≈E_*⁴, la acción requerida resulta:
B_obj≈4 ln(E_*/(ℏH_∞))−ln(ε)≈285.749.

Resolver B_flat=B_obj produce f/E_*≈0.18337, f≈0.410822 meV y R_flat≈1.385 mm. Es un **ejemplo invertido/calibrado**: la tasa fue ingresada como condición, NO fue predicha por la teoría.

La masa local del escalar en y=0 es m_χ=√a E_*²/f≈5.183×10⁻³ eV. En contraste, ℏH_∞≈1.190×10⁻³³ eV; su cociente ≈4.36×10³⁰. La elección que facilita la nucleación del ejemplo no es un campo que evolucione lentamente a escala de Hubble. Esto no demuestra que una masa pesada en un falso vacío no pueda sostener energía de vacío, pero sí impide reclamar ambas dinámicas lentas y rápidas para **el mismo campo en el mismo ejemplo**.

Si se toma f~M_Pl,reducida≈2.435×10²⁷ eV manteniendo la escala meV, el valor FORMAL B_flat~3.5×10¹²⁵ implica una supresión extrema en la fórmula plana, pero el radio resultante sobrepasa el horizonte y esa fórmula ya no es una predicción física fiable. Se necesitan bounces gravitatorios completos.

## 5. Sensibilidad ambiental y quinta fuerza

Para los mismos f y E_*, al exigir una modificación Δa=0.01 por densidad de materia cosmológica promedio, ρ_m/E_*⁴≈Ω_m/Ω_Λ≈0.459854,
M=f√[(ρ_m/E_*⁴)/Δa]≈2.79 meV.

Con A=exp[χ²/(2M²)] y χ=f y_+,
β=M_Pl d lnA/dχ=M_Plχ/M²≈1.13×10²⁹.

Este gran acoplamiento requiere un estudio extraordinariamente exigente del screening y las restricciones. Si M=M_Pl, la misma corrección es Δa≈1.31×10⁻⁶² y la manipulación ambiental por densidades promedio es insignificante.

El signo importa: a crece al **incrementar** ρ_* si M²>0; vaciar una zona disminuye a y puede acercarla a la inestabilidad; concentrar materia no produce automáticamente el mismo resultado. Para a→0 desaparece la estabilidad local, por lo que la evolución puede ser **clásica**, no una fluctuación de túnel. Cavidades finitas necesitan resolver ∇²χ=∂U_eff/∂χ, energía de gradiente, tamaño crítico y contornos.

## 6. Persistencia del fondo

En de Sitter ideal con tasa Γ constante y burbujas ultrarrelativistas, ε=Γ/H⁴ en unidades naturales, y en aproximación asintótica:

V_falso(t)∝exp[(3−4πε/3)Ht].
Se obtiene volumen físico esperado creciente si ε<9/(4π)≈0.716. **Esto no es un umbral universal de percolación** ni demuestra que un observador individual sobreviva.

P_una_línea(t)≈exp[−(4πε/3)Ht] y τ≈3/(4πεH).
Con ε=0.001 y H=H_∞, τ≈4.18×10¹² años; P(100×10¹² años)≈4.18×10⁻¹¹. El volumen global puede aumentar mientras la probabilidad de supervivencia de una línea de mundo fija tiende a cero.

La futura eternidad inflacionaria no implica completitud pasada (Borde–Guth–Vilenkin bajo sus hipótesis).

## 7. Frialdad de una burbuja de energía oscura

Densidad térmica u_rad=(π²/30)g_* T⁴ en unidades naturales; eficiencia térmica 0≤ξ≤1:

T_RH=[30 ξ ΔU/(π²g_*)]^(1/4).

Con g_*=2 para fotones y ξ=1:
toda u_Λ→T≈28.866 K;
ΔU=0.002840086u_Λ→T≈6.664 K.

Una historia de BBN requiere temperaturas de recalentamiento de orden MeV. Barbieri et al. (2025) da T_RH>5.96 MeV (95%) para los escenarios estudiados. Para g_*=10.75, u_rad/u_Λ≈1.771×10³⁸. La energía oscura de hoy no alimenta por sí sola el Big Bang caliente necesario.

Ejemplo ALTERNATIVO, no solución: falso vacío de alta energía V_F~(10¹⁵ GeV)⁴; H_F≈2.37×10¹¹ GeV≈3.60×10³⁵ s⁻¹ y T_max≈4.18×10¹⁴ GeV con g_*=100 y termalización completa. Deben especificarse la fuente de ese estado, geometría, inflación interior, recalentamiento y conservación de energía.

## 8. Dos problemas distintos: decaimiento vs fabricación de un universo

(A) Fondo de falso vacío de mayor energía nuclea región de **menor energía**. Puede ser compatible con cosmología tipo burbuja en modelos inflacionarios, dependiendo de la evolución interior.

(B) Civilización en una región de baja energía pretende crear un bolsillo de **mayor energía inflacionaria** que crezca como universo descendiente. Tiene obstáculos gravitatorios diferentes y fue investigado como hipótesis por Farhi, Guth y Guven; no es consecuencia automática de (A).

No es correcto identificar automáticamente formación de burbuja, Big Bang caliente y creación de espacio-tiempo independiente. Tampoco la existencia de un agujero negro externo implica por sí sola supervivencia o transferencia causal de memoria a una región hija. El significado y observabilidad de “universo descendiente” necesitan definirse geometrícamente.

## 9. Arquitectura alternativa con dos campos

Para no imponer al mismo χ una masa de meV y 10⁻³³ eV, investigar χ (sector cosmológico ambiental) y φ (transición de vacío alta energía), conectados a Higgs y quizá CP con operadores bien especificados:

S=∫√−g [M_Pl²R/2−(∂χ)²/2−(∂φ)²/2−U_DE(χ)−V_PT(φ,χ)+L_portal+L_CP]+S_m[A²(χ)g,ψ].

Ejemplo V_PT=V_F+E_F⁴[a(χ)(φ/F)²/2−(φ/F)⁴/4+(φ/F)⁶/6].

No se han calculado bounces Coleman–De Luccia, espectro de fluctuaciones, ni efectos radiativos de esta acción. Desgravitar exactamente todo vacío constante también apagaría la expansión de de Sitter: conflicto sin resolver.

## 10. Trabajo por realizar

Definir sectores y evitar doble conteo Higgs; derivar el potencial efectivo finito-T; hallar soluciones euclidianas O(4) con gravedad y acción completa; continuar a tiempo lorentziano; resolver FRW interior, recalentamiento, bariogénesis y perturbaciones; confrontar CMB/BAO/BBN, quinta fuerza y pruebas de Higgs; evaluar entropía/horizontes. Sólo entonces estimar qué clase de región física puede formarse.

**Referencias:** Coleman–De Luccia 1980; Farhi–Guth 1987; Farhi–Guth–Guven 1990; Borde–Guth–Vilenkin 2003; Planck 2018/2020; Barbieri et al. 2025. Enlaces en papers/literature-review.md.
