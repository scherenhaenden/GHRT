# 12 — GHRT-VPT: Transition Model, Calculations, and Bubbles vs. Universes

**Date:** 2026-11-21. **Status:** mathematical toy model; does not represent an observed physical transition or a viable technology.

## 1. Origin of the idea

Author's original hypothesis: a persistent expanding cosmic background might give rise to vacuum fluctuations/transitions producing local Big Bang-like histories without the entire parent space ceasing to exist. Accelerated expansion by itself is not a cumulative “tension” that necessarily ruptures spacetime. There must exist a potential with distinct states, a dynamical transition, and a consistent gravitational solution. The closest precedent is false-vacuum eternal inflation, not the classical Steady State model.

The earlier quadratic-quartic symmetron potential of GHRT yields a continuous transition, not a false state separated by a barrier. To study first-order nucleation, a different potential is defined.

## 2. Sixth-order potential and minima

In natural units $\hbar = c = 1$, for a canonical scalar $\chi$ with $y = \chi/f$:

$$
U_{\rm eff}(y;\rho_{\ast}) = U_0 + E_{\ast}^4 \left[a(\rho_{\ast})\frac{y^2}{2} - \frac{y^4}{4} + \frac{y^6}{6}\right], \qquad a(\rho_{\ast}) = a_0 + \frac{\rho_{\ast} f^2}{M^2 E_{\ast}^4}.
$$

Here $\rho_{\ast}$ represents the auxiliary density of **nonrelativistic matter** used in the effective potential; it is incorrect to substitute total radiation density without qualification.

Define $W(y) = a y^2/2 - y^4/4 + y^6/6$, so $W'(y) = y(a - y^2 + y^4)$.
The nontrivial extrema satisfy $y_\pm^2 = [1 \pm \sqrt{1 - 4a}]/2$ when $0 \le a \le 1/4$.

If $0 < a < 3/16$, $y = 0$ is a metastable false minimum, $y_-$ is the barrier peak, and $y_+$ is the true minimum. At $a = 3/16$, $y = 0$ and $y_+$ are degenerate in energy; $a \to 0$ causes $y = 0$ to lose local stability. If $3/16 < a < 1/4$, both minima can coexist with the origin as the deeper minimum, which no longer describes the same favorable decay direction.

Benchmark (not fitted to data): $a = 0.180$;
$y_- = 0.48520600665$;
$y_+ = 0.87439986911$;
$W(y_-) = +0.00950675306$;
$W(y_+) = -0.002840086392$;
$\Delta U = 0.002840086392\,E_{\ast}^4$.

These numbers verify only the algebraic structure of the potential.

## 3. Quantum tunneling and its limits

$\Gamma \approx \mathcal{A}\,e^{-B}$, where $B = S_E[\text{bounce}] - S_E[\text{false}]$ and $\mathcal{A}$ is the fluctuation prefactor per four-volume.

In the **flat-space, thin-wall approximation**:

$$
B_{\rm flat} \approx \frac{27\pi^2\sigma^4}{2\Delta U^3}; \qquad R_{\rm flat} \approx \frac{3\sigma}{\Delta U}.
$$

For $a = 3/16$, the wall tension between degenerate states is $\sigma = \frac{9}{64\sqrt{3}}\,f E_{\ast}^2 = 0.0811898816\,f E_{\ast}^2$.
Using this degenerate tension as an approximation at $a = 0.180$ gives:

$$
B_{\rm flat} \approx 252724.00372\left(\frac{f}{E_{\ast}}\right)^4.
$$

The thin-wall and flat-space approximations can break down when the barrier is not high compared to $\Delta U$, when gravity is included, when $R$ approaches the Hubble radius, and when thermal effects are present; all preceding results are subject to these caveats.

## 4. Numerical example at the present dark-energy scale

Reference $\Lambda$CDM parameters: $H_0 = 67.4\text{ km/s/Mpc}$, $\Omega_m = 0.315$, $\Omega_\Lambda = 0.685$:
$H_0 \approx 2.1843 \times 10^{-18}\text{ s}^{-1}$; $H_\infty \approx 1.8078 \times 10^{-18}\text{ s}^{-1}$;
$u_\Lambda \approx 5.2532 \times 10^{-10}\text{ J/m}^3$; $E_{\ast} = (u_\Lambda \hbar^3 c^3)^{1/4} \approx 2.240365\text{ meV}$.

If one **chooses** a target rate $\varepsilon = \Gamma/H^4 = 0.001$ and **assumes** prefactor $\mathcal{A} \approx E_{\ast}^4$, the required bounce action is:

$$
B_{\rm obj} \approx 4\ln\!\left(\frac{E_{\ast}}{\hbar H_\infty}\right) - \ln(\varepsilon) \approx 285.749.
$$

Solving $B_{\rm flat} = B_{\rm obj}$ yields $f/E_{\ast} \approx 0.18337$, $f \approx 0.410822\text{ meV}$, and $R_{\rm flat} \approx 1.385\text{ mm}$. This is an **inverted/calibrated example**: the rate was entered as a target condition, **not** predicted by the theory.

The local scalar mass at $y = 0$ is $m_\chi = \sqrt{a}\,E_{\ast}^2/f \approx 5.183 \times 10^{-3}\text{ eV}$. By contrast, $\hbar H_\infty \approx 1.190 \times 10^{-33}\text{ eV}$; their ratio is $\approx 4.36 \times 10^{30}$. The parameter choice that facilitates nucleation in this example is not a field that slow-rolls on Hubble scales. This does not prove that a heavy field trapped in a false vacuum cannot sustain vacuum energy, but it prevents claiming both slow-roll and rapid-nucleation dynamics for **the same field in the same example**.

If one takes $f \sim M_{\rm Pl,reduced} \approx 2.435 \times 10^{27}\text{ eV}$ while keeping the $\text{meV}$ scale, the formal value $B_{\rm flat} \sim 3.5 \times 10^{125}$ implies extreme suppression in the flat formula, while the resulting radius exceeds the horizon and the flat formula is no longer a reliable physical prediction. Full gravitational bounces are required.

## 5. Environmental sensitivity and fifth force

For the same $f$ and $E_{\ast}$, requiring a shift $\Delta a = 0.01$ at mean cosmological matter density $\rho_m / E_{\ast}^4 \approx \Omega_m / \Omega_\Lambda \approx 0.459854$ gives:

$$
M = f\sqrt{\frac{\rho_m / E_{\ast}^4}{\Delta a}} \approx 2.79\text{ meV}.
$$

With $A = \exp[\chi^2/(2M^2)]$ and $\chi = f y_+$,

$$
\beta = M_{\rm Pl}\frac{d\ln A}{d\chi} = \frac{M_{\rm Pl}\chi}{M^2} \approx 1.13 \times 10^{29}.
$$

Such a large coupling requires an extraordinarily stringent study of screening and experimental bounds. If $M = M_{\rm Pl}$, the same shift is $\Delta a \approx 1.31 \times 10^{-62}$, and environmental control via mean densities is negligible.

Sign matters: $a$ grows when $\rho_{\ast}$ **increases** if $M^2 > 0$; emptying a region lowers $a$ and can push it toward instability, whereas concentrating matter does not automatically produce the same result. As $a \to 0$, local stability disappears, so evolution can be **classical**, not a tunneling fluctuation. Finite cavities require solving $\nabla^2\chi = \partial U_{\rm eff}/\partial\chi$ with gradient energy, critical size, and boundary conditions.

## 6. Persistence of the background

In ideal de Sitter space with constant rate $\Gamma$ and ultrarelativistic bubble walls, $\varepsilon = \Gamma/H^4$ in natural units, and in the asymptotic approximation:

$$
V_{\rm false}(t) \propto \exp\left[\left(3 - \frac{4\pi\varepsilon}{3}\right)Ht\right].
$$

Expected physical false-vacuum volume grows if $\varepsilon < 9/(4\pi) \approx 0.716$. **This is not a universal percolation threshold**, nor does it prove that an individual observer survives.

$$
P_{\rm worldline}(t) \approx \exp\!\left(-\frac{4\pi\varepsilon}{3}Ht\right), \qquad \tau \approx \frac{3}{4\pi\varepsilon H}.
$$

With $\varepsilon = 0.001$ and $H = H_\infty$, $\tau \approx 4.18 \times 10^{12}\text{ yr}$; $P(100 \times 10^{12}\text{ yr}) \approx 4.18 \times 10^{-11}$. Global volume can grow while the survival probability of any fixed worldline tends to zero.

Future eternal inflation does not imply past geodesic completeness (Borde–Guth–Vilenkin under its hypotheses).

## 7. Coldness of a dark-energy bubble

Thermal energy density $u_{\rm rad} = (\pi^2/30) g_{\ast} T^4$ in natural units; thermalization efficiency $0 \le \xi \le 1$:

$$
T_{\rm RH} = \left(\frac{30\,\xi\,\Delta U}{\pi^2 g_{\ast}}\right)^{1/4}.
$$

With $g_{\ast} = 2$ for photons and $\xi = 1$:
- all of $u_\Lambda \to T \approx 28.866\text{ K}$;
- $\Delta U = 0.002840086\,u_\Lambda \to T \approx 6.664\text{ K}$.

A BBN history requires MeV-scale reheating temperatures. Barbieri et al. (2025) find $T_{\rm RH} > 5.96\text{ MeV}$ (95% CL) for the studied scenarios. For $g_{\ast} = 10.75$, $u_{\rm rad}/u_\Lambda \approx 1.771 \times 10^{38}$. Present dark energy alone cannot power the required hot Big Bang.

ALTERNATIVE example, not a solution: a high-energy false vacuum $V_F \sim (10^{15}\text{ GeV})^4$; $H_F \approx 2.37 \times 10^{11}\text{ GeV} \approx 3.60 \times 10^{35}\text{ s}^{-1}$ and $T_{\rm max} \approx 4.18 \times 10^{14}\text{ GeV}$ with $g_{\ast} = 100$ and complete thermalization. The source of such a state, geometry, interior inflation, reheating, and energy conservation must all be specified.

## 8. Two distinct problems: decay vs. manufacturing a universe

(A) A higher-energy false-vacuum background nucleates a **lower-energy** region. This can be compatible with bubble-type cosmology in inflationary models, depending on interior evolution.

(B) A civilization in a low-energy region attempts to create a pocket of **higher inflationary energy** that grows into a daughter universe. This faces different gravitational obstacles and was investigated hypothetically by Farhi, Guth, and Guven; it is not an automatic consequence of (A).

It is incorrect to automatically equate bubble formation, a hot Big Bang, and creation of an independent spacetime. Nor does the external existence of a black hole by itself imply survival or causal memory transfer into a daughter region. The meaning and observability of a “daughter universe” must be defined geometrically.

## 9. Alternative two-field architecture

To avoid forcing the same $\chi$ to have both $\text{meV}$ and $10^{-33}\text{ eV}$ mass scales, investigate $\chi$ (environmental cosmological sector) and $\varphi$ (high-energy vacuum transition), connected to the Higgs and possibly CP with well-specified operators:

$$
S = \int d^4x\,\sqrt{-g}\left[\frac{M_{\rm Pl}^2}{2}R - \frac{1}{2}(\partial\chi)^2 - \frac{1}{2}(\partial\varphi)^2 - U_{\rm DE}(\chi) - V_{\rm PT}(\varphi,\chi) + \mathcal{L}_{\rm portal} + \mathcal{L}_{\rm CP}\right] + S_m[A^2(\chi)g,\psi].
$$

Example: $V_{\rm PT} = V_F + E_F^4\left[a(\chi)(\varphi/F)^2/2 - (\varphi/F)^4/4 + (\varphi/F)^6/6\right]$.

No Coleman–De Luccia bounces, fluctuation spectra, or radiative effects have been computed for this action. Exactly degravitating all constant vacuum energy would also shut off de Sitter expansion: an unresolved conflict.

## 10. Work to be done

Define sectors and avoid Higgs double-counting; derive the finite-$T$ effective potential; find $O(4)$ Euclidean solutions with gravity and full action; continue to Lorentzian signature; solve interior FRW, reheating, baryogenesis, and perturbations; confront CMB/BAO/BBN, fifth-force, and Higgs tests; evaluate entropy/horizons. Only then estimate what kind of physical region can form.

**References:** Coleman–De Luccia 1980; Farhi–Guth 1987; Farhi–Guth–Guven 1990; Borde–Guth–Vilenkin 2003; Planck 2018/2020; Barbieri et al. 2025. Links in `papers/literature-review.md`.
