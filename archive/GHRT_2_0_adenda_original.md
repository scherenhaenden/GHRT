# GHRT 2.0 — Adenda exploratoria: expansión persistente y Big Bangs locales

**Estado:** hipótesis matemática propuesta para explorar; no es una teoría observacionalmente validada. **Fecha:** 21 de noviembre de 2026.

## Propuesta central

Separar dos niveles: (i) una región parental de falso vacío que puede expandirse durante períodos arbitrariamente largos hacia el futuro y producir transiciones de fase cuánticas; (ii) regiones descendientes que, **si existe además un mecanismo de inflación/recalentamiento**, pueden desarrollar una historia de Big Bang caliente. Esta construcción se parece a la inflación eterna de falso vacío; no es idéntica al Steady State clásico de Hoyle, Bondi y Gold, ni prueba eternidad hacia el pasado.

## 1. Campo de fondo y gravedad

Con densidades de masa equivalentes, la aceleración cosmológica satisface:

    a¨/a = −(4πG/3) [ ρ + 3p/c² ].

Para materia fría y un campo casi constante con pχ≈−ρχ c²:

    a¨/a ≈ (4πG/3) (2ρχ − ρm).

Aceleración si 2ρχ > ρm. No existe un mecanismo estándar de 'tensión de expansión acumulada' que rompa el espacio; hace falta una barrera en el potencial y una transición de vacío. Con referencia ΛCDM/Planck H0=67,4 km/s/Mpc, Ωm=0,315 y ΩΛ=0,685:

- H0 = 2,1843·10^−18 s^−1; q0≈−0,5275.
- Densidad equivalente del campo: 5,8450·10^−27 kg/m³; energía: 5,2532·10^−10 J/m³.
- Inicio aproximado de aceleración: z≈0,632 (dentro de ΛCDM).
- Régimen asintótico de solo energía oscura: H∞=1,8078·10^−18 s^−1, tiempo H∞^−1=17,53 mil millones de años, horizonte de Hubble ~17,53 mil millones de años luz.

Estos parámetros no son predicciones de GHRT; son una calibración de referencia.

## 2. Por qué el GHRT anterior no basta

El potencial symmetron previo:

    Ueff(χ,ρ) = U0 + 1/2 (ρ/M² − μ²) χ² + λ χ⁴/4

crea una transición continua cuando el punto χ=0 se vuelve inestable. No mantiene dos mínimos simultáneos separados por una barrera en el régimen relevante. Por sí solo no produce la nucleación de burbujas de falso vacío que requiere la hipótesis de 'rupturas cuánticas'.

## 3. Extensión covariante mínima: potencial de primer orden

Escalar canónico χ, campo de Higgs H, acoplamiento ambiental universal mediante A(χ)≈exp[χ²/(2M²)], con sector gravitatorio de Einstein a escala efectiva. Potencial de prueba:

    y := χ/f,   Ueff(y,ρm) = U0 + E*⁴ [ a(ρm)y²/2 − y⁴/4 + y⁶/6 ],
    a(ρm) := a0 + ρm f²/(M² E*⁴).

Con 0<a<1/4, las configuraciones no nulas estacionarias cumplen:

    y²± = [1 ± sqrt(1−4a)]/2.

Para 0<a<3/16: y=0 es un mínimo local falso y y+=sqrt[(1+sqrt(1−4a))/2] es el mínimo verdadero, separado de 0 por la barrera y−. Para a=3/16 hay degeneración; para a→0, χ=0 pierde estabilidad. Un cambio de ρm puede llevar el sistema desde una fase apantallada a otra con nucleación posible.

**Ejemplo reproducible de la forma del potencial:** a=0,180:

    y_barrera = 0,485206, y_verdadero = 0,874400,
    [U(barrera)−U(0)]/E*⁴ = +0,009507,
    [U(verdadero)−U(0)]/E*⁴ = −0,002840,
    ΔU = U(falso)−U(verdadero)=0,002840 E*⁴.

Es una demostración de coexistencia de mínimos y barrera, no un ajuste del universo real.

## 4. Física cuántica de la burbuja

Tasa de nucleación por cuatro-volumen (unidades naturales ℏ=c=1):

    Γ ≈ A exp(−B),
    B := SE[solución bounce] − SE[falso vacío].

En aproximación de pared delgada y espacio plano:

    B ≈ 27π² σ⁴/(2ΔU³),     R_nuc ≈ 3σ/ΔU.

En a=3/16 la tensión de pared entre los dos vacíos degenerados se integra analíticamente:

    σ = ∫(0→sqrt(3)/2·f) dχ sqrt[2(U(χ)−U(0))]
      = 9 f E*²/(64sqrt(3)) ≈ 0,08119 f E*².

Usando esa tensión de degeneración como estimación para a=0,180:

    B_plano ≈ 2,5272·10^5 (f/E*)⁴.

Este cálculo NO incluye el efecto gravitatorio Coleman–De Luccia, determinantes de fluctuación, efectos térmicos ni colisiones. Cuando el radio de la burbuja se acerca al radio de Hubble, la fórmula plana deja de ser fiable.

### Ilustración con energía oscura actual

Tomar E*=(uΛ ℏ³c³)^(1/4)≈2,240 meV, U(0)≈uΛ y H≈H∞; por tanto ΔU≈0,002840 uΛ. Si se supone **solo como ejemplo** el prefactor A≈E*⁴ y se fija una tasa adimensional ε≈Γ/H⁴=10^−3, resulta B≈285,75 y f≈0,183 E*≈0,411 meV; R_nuc≈1,39 mm (en la aproximación plana). Los resultados dependen exponencialmente de la forma del potencial y no son predicciones ni elecciones compatibles ya verificadas con límites de quinta fuerza.

Si en cambio f~M_Pl reducido≈2,435·10^27 eV manteniendo E* a escala meV, B_plano sería ~3,5·10^125, con un radio mucho mayor que el horizonte; la aproximación plana deja de funcionar y se impone tratamiento gravitatorio completo. Esta enorme discrepancia ilustra el conflicto entre un modo ultraligero cosmológico, la escala de barrera y el ritmo de nucleación.

## 5. ¿Cómo puede persistir la expansión mientras nacen burbujas?

Para un espacio parental de Sitter aproximadamente constante, paredes a velocidad cercana a c y eventos de nucleación Poisson:

    ε := Γ c³/H⁴ [adimensional],
    V_falso(t) ∝ exp[(3 − 4πε/3) Ht]  para Ht suficientemente grande.

El volumen físico esperado de falso vacío sigue creciendo si:

    ε < 9/(4π) ≈ 0,716.

En esta idealización, el tiempo medio hasta el encuentro de una burbuja en una línea de mundo es:

    τ ≈ [3/(4πε)] H^−1.

Para ε=10^−3 y H=H∞≈1,8078·10^−18 s^−1 se obtiene τ≈4,18·10^3 mil millones de años. Es posible la coexistencia de crecimiento global y transiciones locales, **no** un estado estacionario clásico exacto.

## 6. Por qué una burbuja no es automáticamente un Big Bang caliente

La transición requiere producir un plasma: energía de vacío liberada Δu→radiación/partículas, normalmente seguida o acompañada por dinámica inflacionaria y recalentamiento. La energía oscura de hoy tiene escala:

    EΛ=uΛ^(1/4) en unidades naturales ≈2,24 meV.

Incluso convertir toda uΛ en fotones en equilibrio produciría solo:

    Tmax = [30/(2π²)]^(1/4) EΛ/kB ≈28,9 K.

En el ejemplo de barrera a=0,180, Δu=0,00284uΛ ⇒ Tmax≈6,66 K. Eso es demasiado frío para reproducir la nucleosíntesis primordial y un Big Bang caliente.

Un estudio de constraints cosmológicas de baja temperatura de recalentamiento da TRH>5,96 MeV (95 %); el cociente mínimo de energía radiante respecto de uΛ, con g*=10,75, es aproximadamente 1,77·10^38. No puede originarse de una transición cuyo único presupuesto energético es la energía oscura actual.

**Reparación candidata:** introducir un sector de falso vacío primordial de alta energía, por ejemplo V_F~(10^15 GeV)^4, y un sector de inflación/recalentamiento dentro de cada burbuja. Para V_F así, H_F≈2,37·10^11 GeV≈3,60·10^35 s^−1 y H_F^−1≈2,78·10^−36 s; si toda V_F se convierte en un plasma con g*=100, su límite termodinámico ideal es T≈4,18·10^14 GeV. Son cifras ilustrativas, no un modelo que automáticamente produzca las perturbaciones observadas.

## 7. Cuatro problemas nuevos que GHRT debe reconocer explícitamente

**Vacío absoluto vs. expansión:** si la desgravitación GHRT desconecta *toda* energía de vacío exactamente constante, también podría eliminar la fuente de la expansión inflacionaria. Se necesita un mecanismo consistente que distinga energía absoluta secluida de diferencias energéticas que sí gravitan.

**Radiación y acoplamiento a traza:** T^μ_μ≈0 para radiación ideal; entonces 'alta densidad' en una época dominada por radiación no basta para apantallar χ mediante el mecanismo de traza anterior. Se requieren correcciones térmicas del potencial (si el portal lo permite) u otro régimen temprano, calculados sin violar las restricciones sobre el Higgs.

**Conexión con Higgs y estabilidad cuántica:** el portal H†Hχ² debe especificarse y renormalizarse; un χ ultraligero o barreras de escala cosmológica pueden ser inestables por correcciones de bucles. Un nuevo campo para inflación/recalentamiento también debe controlar las masas del sector visible.

**Eternidad hacia el pasado:** expansión de tipo de Sitter que continúa eternamente hacia el futuro no demuestra que el espacio-tiempo no tenga borde pasado. Bajo condiciones de expansión media positiva se aplica el teorema de incompletitud Borde–Guth–Vilenkin. Haría falta una fase pasada diferente y una solución global regular para aspirar a un auténtico universo pasado-eterno.

## 8. Estado de la hipótesis

**Sí es posible:** escribir un campo GHRT con apantallamiento ambiental, transición cuántica de primer orden y un fondo que sigue expandiéndose mientras aparecen regiones descendientes. Un universo puede, en un modelo, tener historias de Big Bang caliente locales.

**No está probado:** que la ruptura se deba a una fuerza de expansión acumulada, que una burbuja produzca necesariamente un Big Bang, que la conexión con Higgs sea radiativamente estable, que un único campo y una sola escala de energía puedan dar simultáneamente energía oscura y un Big Bang caliente, que el modelo reproduzca CMB/BAO/BBN/crecimiento de estructuras y que el universo sea eterno hacia el pasado.

**Nombre provisional de esta extensión:** GHRT-VPT (*Vacuum Phase Transitions*), como subsector de GHRT, no como teoría independiente validada.

## Fuentes externas de contraste

- Planck 2018 resultados cosmológicos: https://doi.org/10.1051/0004-6361/201833910
- Coleman y De Luccia (1980), transición cuántica gravitatoria: https://doi.org/10.1103/PhysRevD.21.3305
- Bubble nucleation and completion of a first-order transition: https://doi.org/10.1103/PhysRevD.46.2384
- Borde, Guth y Vilenkin (2003), incompletitud hacia el pasado: https://doi.org/10.1103/PhysRevLett.90.151301
- Recalentamiento mínimo, estudio 2025: https://arxiv.org/abs/2501.01369
- Correcciones de temperatura y acoplamiento conforme: https://doi.org/10.1088/1475-7516/2009/07/025
