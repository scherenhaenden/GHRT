# 10 — Falsification Tests and Model Acceptance

## Logic gates

G1. **Dimensions and frames.** Every equation maintains consistent dimensions; Einstein/Jordan/$\rho_*$ densities are not confused, and the action does not double-count matter.

G2. **Solutions.** Minima, screening profiles, Friedmann solutions, and a gravitational bounce exist with explicit boundary conditions. Do not infer solutions from a plot of the potential.

G3. **Stability.** No ghosts, gradient instabilities, or couplings that invalidate the EFT; control radiative naturalness or expose the fine-tuning.

G4. **Local recovery.** The theory passes at least the relevant fifth-force and relativity tests. The coefficient $\beta = M_{\rm Pl}\,d\ln A/d\chi$ is evaluated in the right environment.

G5. **Thermal history.** Sufficient energy for reheating; compute $\eta_B$ and perturbations rather than assuming them because a bubble wall exists.

G6. **Cosmological data.** Predictions distinguishable from $\Lambda$CDM and reproducible comparison with observations. Make priors and degeneracies explicit.

G7. **Entropy and causality.** If inter-universe continuity is claimed, identify a physical information channel and compatibility with horizons and thermodynamics; otherwise classify it as speculation.

## Minimal numerical check

Run `python3 models/vpt_benchmark.py`. It must verify the extrema and energy differences of the sixth-order potential and the example scales. This is an **algebraic** check, not empirical validation.

## Rejection criteria

A candidate version is ruled out in the chosen regime if it violates dimensional consistency, lacks the claimed minimum/tunneling solution, simultaneously requires irreconcilable masses for a single field, predicts an unscreened force incompatible with bounds, or fails to produce the required thermal history while claiming to have explained it. Reformulating hypotheses is not falsifying nature: preserve the history of parameters and failed cases.

## Publication

Tag each result as `[LITERATURE]`, `[DERIVATION]`, `[BENCHMARK]`, `[HYPOTHESIS]`, or `[SPECULATION]`. Declare whenever a prediction depends on assuming the value later presented as a result.
