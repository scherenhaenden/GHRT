# Repository content and publication audit

Audit date: 2026-11-21

## Scope reviewed

The working tree was inspected before Git initialization. It contained project Markdown files, three empty but valid Jupyter notebook scaffolds, a minimal LaTeX scaffold, and `.DS_Store` metadata files. The separate master PDF supplied for review resides in the user's Downloads folder and is not part of this project directory.

## Content decision

The files in this project are appropriate for a research repository provided the repository is private at creation and the scientific status remains explicit:

- Markdown notes and the correction manual are project documentation, not personal records or credentials.
- Empty notebooks are harmless scaffolds, but they currently provide no reproducible calculations.
- `manuscript/GHRT.tex` is only a three-line empty LaTeX document; it is not the source of the supplied master PDF.
- `.DS_Store` files are machine-generated local metadata and are excluded.
- No credentials, API tokens, private keys, personal data, or experimental datasets were present in the audited project file list.
- The downloaded master PDF is outside the repository and is not copied into Git. Generated PDFs and LaTeX build products are ignored.
- No license is added because the project owner has not specified reuse terms.

## Publication cautions

The repository is initialized as **private**. Before making it public, review the scientific notes, cited-source accuracy, copyright and redistribution terms, and whether any future datasets or correspondence may contain restricted information. Private visibility does not replace secret scanning or careful review of future commits.

The working notes explicitly distinguish established literature from GHRT hypotheses. This distinction should be preserved in future contributions. The current checkout does not include the 36-page master-document source, and its LaTeX scaffold must not be mistaken for a compilable manuscript version.

## Ongoing safeguards

- `.gitignore` excludes common operating-system metadata, editor state, Python/Jupyter runtime artifacts, LaTeX build products/PDFs, and common local secret files.
- Keep source data and generated or licensed material out unless redistribution rights and provenance are documented.
- Check `git status` and inspect staged diffs before every commit; never commit tokens, private keys, `.env` files, or personal data.
- Record provenance and license for any imported paper, dataset, figure, or external code.


## Addendum — 2026-11-21: GHRT-VPT research branch

Repository metadata returned by GitHub during this revision identifies the repository visibility as **public**, regardless of the historical entry above about being private at initialization. Treat the present visibility as public and review future changes accordingly.

Branch: research/ghrt-vpt-renovacion-cosmica-2026-11-21, derived from main. The prior manual and historical main files were preserved; no previously published GHRT master PDF is falsely represented as transcribed or regenerated.

New material adds substantive research notes in docs/00–10, docs/12–15, an expanded literature review, a research-oriented README, and an algebraic Python benchmark in models/vpt_benchmark.py. These are exploratory candidate models and critiques, not validated physical predictions. The old Jupyter and LaTeX files remain scaffolds.

Scientific cautions: tuned benchmark nucleation rate; 30-order field-mass mismatch; large unscreened fifth-force coupling or vanishing density response; dark-energy reheating energy deficit; CP baryogenesis not supplied by a real Higgs portal; distinction between descending true-vacuum bubble and creating a high-energy false-vacuum child; no demonstrated information transfer between spaces.

Source provenance: November 2026 GHRT-VPT addendum, author–Gemini dialogue shared by the author, and independent mathematical audit in the related ChatGPT project conversation. The speculative cosmic-intelligence discussion was initiated by the **author** after viewing a science-fiction video. Sources are catalogued in papers/literature-review.md. No claim is made that all external master documents have been reproduced in this branch.

The benchmark script has numerical assertions but is not a gravitational or observational validation. No CI workflow is supplied and the absent master manuscript remains outstanding.
