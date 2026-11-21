# Granular Higgs Recoil Theory (GHRT)

GHRT is an **exploratory, unvalidated physics research program** investigating whether the physical vacuum can be described by a dynamical collective degree of freedom that responds to matter, connects to the Higgs sector, and admits environmental screening, vacuum-energy mechanisms, and an explicitly speculative extension called **GHRT-VPT** (Vacuum Phase Transitions). The project is not an established theory, and the repository does not claim that GHRT explains dark energy, the cosmological constant, the Hubble tension, or the origin of time.

**Scientific status:** none of the proposed GHRT-specific dynamics has yet been shown to reproduce all precision tests or to outperform established cosmological models. Mathematical examples and benchmark values are *not* observational confirmations.

## The central idea

The working formulation introduces a hypothetical scalar field $\chi$, distinct from the observed 125 GeV Higgs excitation $h$. In a candidate scalar-tensor model, matter couples to the Jordan-frame metric

$$
\widetilde g_{\mu\nu}=A^2(\chi)g_{\mu\nu},
$$

while gravity is written in the Einstein frame. The logarithmic derivative $\alpha(\chi)=d\ln A/d\chi$ makes the scalar respond to the trace of the matter stress tensor, $T=T^\mu{}_{\mu}$. With metric signature $(-+++)$, a perfect fluid has $T=-\rho+3p$: nonrelativistic matter has a sizable trace, an ideal radiation fluid has zero classical trace, and an isotropic gas of relativistic massive particles has a suppressed trace.

This gives a covariant way to restate part of GHRT's original “Slip-Stream” intuition without introducing a preferred rest frame or a literal vacuum lattice. It does **not** by itself imply drag, friction, energy loss, or a new interaction cross-section.

## Candidate scalar-tensor core

The minimal working action is

$$
S_{\rm core}=\int d^4x\sqrt{-g}\left[\frac{M_{\rm Pl}^2}{2}R-\frac12(\partial\chi)^2-U(\chi)\right]
+S_m[A^2(\chi)g_{\mu\nu},\psi].
$$

This is a standard scalar-tensor structure, not a novel result of GHRT. It supplies a calculable starting point for deriving the scalar equation, energy exchange between matter and $\chi$, cosmological evolution, and possible fifth forces. A symmetron-like potential is one benchmark for environmental screening; it is inherited from existing literature and is not, by itself, GHRT's original contribution.

## What GHRT is trying to test

The research program asks whether one can build a consistent model that:

1. responds to the matter trace in a controlled, frame-consistent way;
2. suppresses additional scalar forces in tested environments while allowing possible cosmological effects;
3. keeps a cosmologically light mode stable against quantum corrections;
4. connects nontrivially to the Higgs sector without contradicting particle-physics constraints;
5. makes quantitative predictions for expansion, structure growth, lensing, and laboratory or astrophysical tests; and
6. treats vacuum-energy degravitation or sequestering—and any speculative GHRT-VPT vacuum-transition extension—as separate mechanisms with their own actions and consistency checks.

These are open requirements, not achieved results. In particular, the conformal scalar-tensor core does not solve the cosmological-constant problem automatically. Screening does not establish viability, and a Higgs portal does not automatically protect an ultralight scalar mass.

## Scientific status and known limitations

The material here is a set of research notes, audits, and candidate constructions. The symmetron, conformal scalar-tensor coupling, pseudo-Nambu-Goldstone potentials, degravitation, and vacuum sequestering all have prior literature. Any claim of GHRT novelty requires a comparison of explicit actions and observables with that literature.

The main unresolved issues are radiative stability of $\chi$ (including a ~30-order mass mismatch in the VPT toy benchmark), compatibility of screening with cosmology and fifth-force bounds, a well-defined Higgs connection (and CP/baryogenesis), a viable background and perturbation history, and a concrete treatment of vacuum energy. No complete parameter fit or validated GHRT-specific prediction is supplied here.

## Repository map

- `docs/00-concept.md` — conceptual motivation, including the distinction between the author's intuition and scientific evidence.
- `docs/01-postulates.md` — candidate hypotheses and their status.
- `docs/02-mathematical-framework.md` — scalar-tensor action, conventions, and field/background equations.
- `docs/03-higgs-vacuum-sector.md` — Higgs portals, dimensions, CP, and radiative stability.
- `docs/04-trace-coupling.md` — conformal coupling and matter trace.
- `docs/05-screening.md` — symmetron screening and fifth forces.
- `docs/06-vacuum-degravitation.md` — the unsolved constant-vacuum gravitation problem.
- `docs/07-cosmology.md` — accelerating expansion, false-vacuum volume, and daughter regions.
- `docs/08-time-compton-phase.md` — proper time, phases, and limitations.
- `docs/09-observational-constraints.md` — experimental and astronomical tests.
- `docs/10-falsification-tests.md` — computational and empirical failure criteria.
- `docs/11-manual-correcciones-v0.1.md` — preserved correction guidance (in Spanish) for the prior master document.
- `docs/12-vpt-model-and-calculations.md` — VPT derivations, scales, toy benchmark, and gravitational follow-up.
- `docs/13-intelligence-and-cosmic-continuity.md` — AI thought experiment, energy horizons, and information transfer.
- `docs/14-audit-and-corrections-2026-11-21.md` — critical audit of claims and prior dialogue.
- `docs/15-research-roadmap.md` — sequenced model-building work.
- `papers/literature-review.md` — research references with primary links.
- `models/vpt_benchmark.py` — reproducible standard-library benchmark and algebraic assertions.
- `archive/` — preserved unedited historical source texts (in Spanish) and provenance index.
- `notebooks/` — older empty Jupyter scaffolds; not evidence of executed calculations.
- `manuscript/GHRT.tex` — minimal LaTeX scaffold, **not** the source for any prior master PDF.
- `REPOSITORY_AUDIT.md` — tracked-content and publication audit.

## Provenance and preservation

The prior v0.1 correction manual (`docs/11-manual-correcciones-v0.1.md`) and `archive/` texts are preserved as *source history*. The author's earlier master documents (v0.1/v0.1.1/v0.1.2) and the November 2026 chat addenda are not transcribed in full here; do not present this repository as a complete transcription of those PDFs. The documentation distinguishes user-origin intuition, working mathematical models, published findings, and unverified extrapolations.

The two explanatory YouTube videos that motivated discussion are narrative prompts, **not primary physics references**:
- https://www.youtube.com/watch?v=bpGum1z8MfA
- https://www.youtube.com/watch?v=oRBu7wYuOSo

## Reproduction and working with the repository

Run the exploratory toy benchmark:

```bash
python3 models/vpt_benchmark.py
```

This checks the algebra of one intentionally tuned toy potential; it does not calculate a Coleman–De Luccia bounce, verify a theory of everything, or demonstrate an engineering route to a baby universe.

Numerical claims should include assumptions, units, provenance, and a reproducible derivation. Distinguish established results from candidate hypotheses and calculations that have not yet been performed. The current notebooks are empty and the LaTeX file is only a scaffold, so they cannot reproduce the master document or its equations.

## License

No license has been selected. The repository's public visibility does not itself grant permission to reuse its contents; licensing and attribution terms remain to be decided by the project owner.
