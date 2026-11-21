# 02 — Minimal Mathematical Framework

Conventions: $c = \hbar = 1$ unless explicitly stated, signature $(-,+,+,+)$, $M_{\rm Pl}$ is the **reduced** Planck mass. $g_{\mu\nu}$ is the Einstein-frame metric; $\widetilde g_{\mu\nu} = A^2(\chi)g_{\mu\nu}$ is the Jordan-frame metric.

## Single-scalar candidate action

$$
S = \int d^4x\,\sqrt{-g}\left[\frac{M_{\rm Pl}^2}{2}R - \frac{1}{2}(\partial\chi)^2 - U(\chi) + \mathcal{L}_{\rm SM}(g,H,\dots)\right] + S_m[A^2(\chi)g,\psi].
$$

Writing $\mathcal{L}_{\rm SM}$ and $S_m$ separately here requires avoiding double-counting the same degrees of freedom. A consistent formulation must decide whether **all** of the Standard Model matter sector, including the Higgs, resides in $S_m$, or whether the portal is separated in the Einstein-frame action. The expression is a schema until that assignment is specified.

Define $\alpha(\chi) = d\ln A / d\chi$ and $\beta(\chi) = M_{\rm Pl}\,\alpha(\chi)$. The scalar equation in the Einstein frame reads, for the coupled matter sector:

$$
\Box\chi = U_{,\chi} - \alpha T_E.
$$

For dust $T_E \approx -\rho_E$, so $\Box\chi = U_{,\chi} + \alpha \rho_E$. Transformed matter conservation for dust gives:

$$
\dot\rho_E + 3H\rho_E = \alpha\dot\chi\rho_E; \qquad \dot\rho_* + 3H\rho_* = 0; \qquad \rho_* = \frac{\rho_E}{A} = A^3\widetilde\rho.
$$

The effective potential for dust **at fixed $\rho_*$** is:

$$
U_{\rm eff}(\chi;\rho_*) = U(\chi) + \rho_*[A(\chi) - 1]; \qquad \partial_\chi U_{\rm eff} = U_{,\chi} + \rho_* A_{,\chi}.
$$

Subtracting the constant term does not remove energy from the gravitating stress tensor. The Friedmann equations in the Einstein frame contain $\rho_E$, not $\rho_*$ without transformation.

## Homogeneous background

$$
3M_{\rm Pl}^2 H^2 = \rho_E + \rho_r + \frac{1}{2}\dot\chi^2 + U(\chi) \quad \text{[if no other sectors]},
$$
$$
-2M_{\rm Pl}^2 \dot H = \rho_E + \frac{4}{3}\rho_r + \dot\chi^2.
$$

General cosmological acceleration is $\ddot a / a = -(\rho_{\rm tot} + 3p_{\rm tot}) / (6M_{\rm Pl}^2)$. It requires $\rho_{\rm tot} + 3p_{\rm tot} < 0$; expansion and acceleration are not synonymous.

## Two-scalar version for research

$$
S = \int d^4x\,\sqrt{-g}\left[\frac{M_{\rm Pl}^2}{2}R - \frac{1}{2}(\partial\chi)^2 - \frac{1}{2}(\partial\varphi)^2 - U_{\rm DE}(\chi) - V_{\rm PT}(\varphi,\chi) + \mathcal{L}_{\rm portal} + \mathcal{L}_{\rm CP}\right] + S_m[A^2(\chi)g,\psi].
$$

The full $\mathcal{L}_{\rm portal}$ and $\mathcal{L}_{\rm CP}$ have not yet been chosen: their signs, dimensions, field content, and symmetries must be specified before deducing masses, stability, or baryogenesis. For a potential $V = U_{\rm DE} + V_{\rm PT}$, the $O(4)$ Euclidean system, without additional sources, contains:

$$
\varphi'' + 3\frac{b'}{b}\varphi' = \frac{\partial V}{\partial\varphi}; \qquad \chi'' + 3\frac{b'}{b}\chi' = \frac{\partial V}{\partial\chi}; \qquad b'^2 = 1 + \frac{b^2}{3M_{\rm Pl}^2}\left[\frac{1}{2}(\varphi'^2 + \chi'^2) - V\right].
$$

These are candidate equations for a Coleman–De Luccia boundary-value problem, **not an already-computed solution**. They must be accompanied by regularity, endpoint boundary conditions, the Euclidean action, and Lorentzian continuation.

Multiple scalar fields avoid imposing a single dynamical scale, but they do **not** automatically solve the radiative hierarchy, fifth forces, or universe creation.
