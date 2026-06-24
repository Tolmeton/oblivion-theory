# Changelog

This file records public-edition snapshots. The public edition lags the internal
working archive; entries here mark when the public reading edition was refreshed
or restructured. All papers remain concept drafts.

## 2026-06-24 — Bilingual structure + series refresh + Paper XV

### Changed
- Restructured the repository into a numbered bilingual layout
  (`番号_日本語｜English`): `01_本編シリーズ｜Series`, `02_伴走枝｜Companion`,
  `03_単独論考｜Standalone`, `04_出版証跡｜Publications`, with a reading guide
  under `00_案内｜Guide`. Old paths map to new paths in
  [`00_案内｜Guide/移行表.md`](00_案内｜Guide/移行表.md).
- Refreshed the series papers (0–XIV) from the current source. Paper VII, VIII,
  XIII, and XIV gained substantial revisions since the previous public snapshot.

### Added
- Paper XV — Oblivion Precedes Mathematics and Physics — to the main series
  (a synthesis paper over Papers 0–XIV).
- Public-repository infrastructure: `CITATION.cff`, `CONTRIBUTING.md`,
  this `CHANGELOG.md`, and GitHub issue templates.

### Fixed
- Removed backstage annotations from reference entries in Paper XIII so the
  public edition no longer points at internal working notes.
- Corrected the Public Edition Guard workflow: removed a shell syntax error in
  the email-check step and a `backstage` token that collided with legitimate
  technical vocabulary in Paper II.

### Known follow-ups
- Papers XVI, XVII, and XVIII are held back: they carry internal working
  vocabulary and unfinished (TBD) abstracts, and need a dedicated curation pass.
- The companion branch *Understanding and Prediction as Science*
  (`理解と予測の営みとしての科学`) is held back: its main draft still carries
  internal working vocabulary and needs a dedicated curation pass.
- Some series papers still contain absolute filesystem paths and internal
  vocabulary inherited from the source. These are scheduled for a separate
  cleanup pass, after which the Public Edition Guard can be extended to reject
  them.

## 2026-05-01 — Previous public snapshot

- Series papers refreshed; companion draft series published; published-preprint
  index added. See git history before this changelog for details.
