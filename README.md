# Granular Higgs Recoil Theory (GHRT)

GHRT is a speculative research program about whether the physical vacuum can be described by a dynamical collective degree of freedom that responds to matter and may connect to the Higgs sector. The project is not an established theory, and the repository does not claim that GHRT explains dark energy, the cosmological constant, the Hubble tension, or the origin of time.

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
6. treats vacuum-energy degravitation or sequestering as a separate mechanism with its own action and consistency checks.

These are open requirements, not achieved results. In particular, the conformal scalar-tensor core does not solve the cosmological-constant problem automatically. Screening does not establish viability, and a Higgs portal does not automatically protect an ultralight scalar mass.

## Scientific status and known limitations

The material here is a set of research notes and candidate constructions. The symmetron, conformal scalar-tensor coupling, pseudo-Nambu-Goldstone potentials, degravitation, and vacuum sequestering all have prior literature. Any claim of GHRT novelty requires a comparison of explicit actions and observables with that literature.

The main unresolved issues are radiative stability of $\chi$, compatibility of screening with cosmology and fifth-force bounds, a well-defined Higgs connection, a viable background and perturbation history, and a concrete treatment of vacuum energy. No complete parameter fit or validated GHRT-specific prediction is supplied here.

## Repository map

- `docs/00-concept.md` — planned topic scaffold (heading only): purpose, scope, and epistemic status.
- `docs/01-postulates.md` — planned topic scaffold (heading only): assumptions separated from derived consequences.
- `docs/02-mathematical-framework.md` — planned topic scaffold (heading only): frames, action, equations, and conventions.
- `docs/03-higgs-vacuum-sector.md` — planned topic scaffold (heading only): proposed relationship between $h$ and $\chi$.
- `docs/04-trace-coupling.md` — planned topic scaffold (heading only): trace source and limits of the Slip-Stream analogy.
- `docs/05-screening.md` — planned topic scaffold (heading only): symmetron benchmark and fifth-force questions.
- `docs/06-vacuum-degravitation.md` — planned topic scaffold (heading only): distinct vacuum-energy proposals and open choices.
- `docs/07-cosmology.md` — planned topic scaffold (heading only): background and perturbation observables still to calculate.
- `docs/08-time-compton-phase.md` — planned topic scaffold (heading only): interpretation of matter phase along proper time.
- `docs/09-observational-constraints.md` — planned topic scaffold (heading only): data and experimental tests to confront.
- `docs/10-falsification-tests.md` — planned topic scaffold (heading only): conditions under which candidate models fail.
- `docs/11-manual-correcciones-v0.1.md` — editorial and equation corrections for the master document.
- `papers/literature-review.md` — literature review workspace (currently a heading-only scaffold).
- `models/` — planned numerical implementations; currently no model code is present.
- `notebooks/` — empty notebook scaffolds; no calculations are implemented yet.
- `manuscript/GHRT.tex` — minimal LaTeX scaffold, not the source of the 36-page master PDF.
- `REPOSITORY_AUDIT.md` — tracked-content and publication audit.

## Working with the repository

The repository is documentation-first at this stage. Numerical claims should include assumptions, units, provenance, and a reproducible derivation. Distinguish established results from candidate hypotheses and calculations that have not yet been performed. The current notebooks are empty and the LaTeX file is only a scaffold, so they cannot reproduce the master document or its equations.

## License

No license has been selected. The repository's public visibility does not itself grant permission to reuse its contents; licensing and attribution terms remain to be decided by the project owner.
