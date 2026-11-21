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
