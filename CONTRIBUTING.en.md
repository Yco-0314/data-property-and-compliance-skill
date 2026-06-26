# Contributing

🌐 [中文](./CONTRIBUTING.md) · **English**

Thanks for contributing to **Data Property and Compliance Skill**.

## Red lines (must follow)
1. **Do not submit any confidential / non-public material**: internal question banks, unpublished trial-version guidance texts, real registration cases, real filing materials, or anything with real party identifiers (name / unified social credit code / contract number).
2. **Do not present inference as a legal conclusion**: for "is it illegal / does it constitute surveying / is it false," use hedged wording — "may involve / to be determined by the competent authority or a court case-by-case."
3. **All citations must be publicly verifiable**: state the regulation name, version, effective date, and an official source link.

## How to contribute
- **Regulation update / citation fix**: in the PR, state "name + version + effective date + official link."
- **New review tool / checklist item**: place under the matching domain in `SKILL.md`, keep it "abstract methodology, public sources only, no confidentiality-bound details."
- **Code tools** (PDF extraction / OCR / validation): place under `tools/`, MIT-licensed (see `tools/README.md`).

## License & attribution
- **Content** (`SKILL.md`, docs): [CC BY 4.0](./LICENSE).
- **Code** (`tools/`): MIT.
- Opening a PR is deemed acceptance of licensing your contribution under the corresponding license above.

## Commit conventions
- One PR, one focused change; include rationale and sources.
- For changes to legal content, tick the PR box: "this change contains no confidential / non-public material."

## Automated checks
Every push/PR runs CI (`.github/workflows/ci.yml`):
- **compliance-guard** — fails if removed confidential / case / wrong-citation patterns reappear (`tools/compliance_guard.py`).
- **link-check** — verifies documentation links resolve.

Run the guard locally before pushing:
```bash
python3 tools/compliance_guard.py
```
