# 15 — Scientific Roadmap (GHRT / GHRT-VPT)

## Stage 0 — Consolidate provenance and baseline

Preserve the manual `docs/11-manual-correcciones-v0.1.md`, external historical versions v0.1/v0.1.1/v0.1.2, and the November notes without presenting the repository as a complete source of the master PDF. Tag literature/derivations/hypotheses. Use $(-,+,+,+)$, Einstein/Jordan frames, and consistent units.

## Stage 1 — Self-consistent effective model

Fix whether Standard Model sectors couple conformally in a universal way and in which action the Higgs is placed. Specify $U_{\rm DE}(\chi)$, $V_{\rm PT}(\varphi,\chi)$, $A(\chi)$, $\mathcal{L}_{\rm portal}$, and $\mathcal{L}_{\rm CP}$ with dimensions, symmetries, parameters, and EFT domain. Derive equations by full variation; verify the Bianchi identity. Do not invent “granularity” physics without an operator and a prediction.

**Acceptance:** unambiguous action, consistent dimensions, conservation, and recovery of GR in a controlled regime.

## Stage 2 — Benchmark testing

Use `models/vpt_benchmark.py` to verify extrema and scales. Run independent sweeps in $a$, $f/E_*$, $M$, and coupling terms; separate target-input rate from predicted rate. Build a thin-wall sensitivity test against a flat $O(4)$ bounce calculation.

**Acceptance:** tested code and error plots/models, not only hand calculations.

## Stage 3 — Gravity and geometry

Jointly solve $b(\xi)$, $\chi(\xi)$, $\varphi(\xi)$ and regularity conditions; compute $B$ with gravity and the prefactor. Classify false-vacuum decay branches and the laboratory inflationary false-vacuum scenario. Continue to Lorentzian geometry and obtain interior FRW if it exists.

**Acceptance:** discretization-independent numerical solution, finite and controlled $B$, causal classification.

## Stage 4 — Particle physics and hot universe

Thermal potential terms, reheating channel, $T_{\rm RH}$, neutrino/BBN history, baryogenesis (Sakharov), EDM bounds, Higgs mixing, and naturalness. Compute the primordial spectrum; do not substitute an arbitrarily fixed $\delta\rho/\rho$.

**Acceptance:** thermal history compatible with data and allowed parameters.

## Stage 5 — Observational tests

Cosmological perturbations, CMB, BAO, growth, gravitational lensing, local fifth force, equivalence principle, pulsars/GWs as applicable to the model. Publish predictive posteriors and compare against $\Lambda$CDM under identical statistical criteria.

**Acceptance:** falsifiable predictions and reproducible documentation.

## Stage 6 — Informational question (separate)

Only once an established daughter geometry exists: define a physical information channel with degrees of freedom, capacity, parent $\to$ daughter state map, observable recovery, entropy, and causality. Do not confuse transmission of global parameters with transfer of memory or personal continuity.

The goal is **to discover failures early**, not to retroactively fit every phenomenon into GHRT.
