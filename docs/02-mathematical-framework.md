# 02 — Marco matemático mínimo

Convenciones: c=ℏ=1 salvo indicación explícita, firma (-,+,+,+), M_Pl masa de Planck **reducida**. g_μν es la métrica de Einstein; g̃_μν=A²(χ)g_μν es la de Jordan.

## Acción candidata monoescalar

S = ∫d⁴x √(-g) [ M_Pl² R/2 − (∂χ)²/2 − U(χ) + L_SM(g,H,...) ] + S_m[A²(χ)g,ψ].

Aquí escribir L_SM y S_m por separado exige evitar contar dos veces los mismos grados de libertad. Una formulación consistente debe decidir si **todo** el sector de materia estándar, incluido Higgs, está en S_m o si el portal se separa en la acción Einstein. La expresión es un esquema hasta concretar esa asignación.

Definir α(χ)=d ln A/dχ y β(χ)=M_Pl α(χ). La ecuación escalar en el marco Einstein se escribe, para el sector material acoplado:

□χ = U_,χ − α T_E.

En polvo T_E≈−ρ_E, por lo que □χ = U_,χ + α ρ_E. La conservación material transformada tiene para polvo:

ρ̇_E + 3Hρ_E = α χ̇ ρ_E;
ρ̇_* + 3Hρ_* = 0; ρ_* = ρ_E/A = A³ ρ̃.

El potencial efectivo para polvo **a ρ_* fijo**:

U_eff(χ;ρ_*) = U(χ)+ρ_*[A(χ)−1];
∂χ U_eff = U_,χ+ρ_*A_,χ.

La resta del término constante no elimina energía del tensor gravitante. Las ecuaciones de Friedmann en Einstein contienen ρ_E, no ρ_* sin transformación.

## Fondo homogéneo

3M_Pl² H² = ρ_E + ρ_r + χ̇²/2 + U(χ) [si no hay otros sectores].
−2M_Pl² Ḣ = ρ_E+(4/3)ρ_r+χ̇².

La aceleración cosmológica general es ä/a = −(ρ_tot+3p_tot)/(6M_Pl²). Requiere ρ_tot+3p_tot<0; expansión y aceleración no son sinónimos.

## Versión biescalar para investigación

S = ∫√(-g) [M_Pl²R/2 − (∂χ)²/2 − (∂φ)²/2 − U_DE(χ) − V_PT(φ,χ) + L_portal + L_CP] + S_m[A²(χ)g,ψ].

Aún no se ha elegido el L_portal ni L_CP completos: sus signos, dimensiones, contenido de campos y simetrías deben especificarse antes de deducir masas, estabilidad o bariogénesis. Para potencial V=U_DE+V_PT, el sistema euclidiano O(4), sin fuentes adicionales, contiene:

φ''+3b'/b φ' = ∂V/∂φ;
χ''+3b'/b χ' = ∂V/∂χ;
b'²=1 + b²[(φ'²+χ'²)/2 − V]/(3M_Pl²).

Son ecuaciones candidatas para un problema de contorno de Coleman–De Luccia, **no una solución ya calculada**. Deberán acompañarse de regularidad, condiciones en los extremos, acción euclidiana y continuación lorentziana.

Los campos escalares múltiples evitan imponer una sola escala dinámica, pero NO resuelven automáticamente la jerarquía radiativa, las fuerzas adicionales ni la creación de universos.
