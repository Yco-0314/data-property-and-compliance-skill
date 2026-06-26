# Data-Element Lifecycle Compliance Review (English)

> 🌐 English translation of [`SKILL.md`](./SKILL.md). The **operational** skill an agent loads is the Chinese `SKILL.md` (the subject matter is PRC data law). This file is a faithful guide for English readers and is **not** registered as a separate skill.
>
> ⚠️ **Disclaimer**: Reference / educational framework only. **Not legal advice.** Article numbers and rules may have changed — rely on the current in-force text and consult a qualified professional.
>
> 🗂 **About this version**: clean-room rewrite — only ① publicly verifiable sources and ② original methodology; no substance from any confidential internal material; examples are redacted / illustrative.
>
> 🔖 Version v1.0 · last revised 2026-06-26 · License: CC BY 4.0

## Sources & boundaries

Every statement here is one of two kinds, and **none** reproduces the substance of non-public internal material:
1. **Publicly verifiable sources** — published laws, administrative regulations, departmental rules, national standards, national-level plans/measures, plus exchanges' **officially published** trading rules and the national model contracts.
2. **The author's original methodology** — review dimensions, contradiction-detection tools, timeline audit, risk matrix.

Anything that cannot point to a public source is rewritten as analysis based on public law, or annotated "per the locally published rules in force," rather than stated as an authoritative rule. Verify all article numbers against the official text.

## When this triggers

Reviewing the compliance of data-element business, including: data-property registration filings; pre-listing compliance assessment of data products; legal due diligence for data trading/investment; data-sharing agreement review; public-data authorized-operation compliance; data classification/grading; **data-asset capitalization (accounting)**; **data-asset securitization (ABS)**; **trusted-data-space compliance & architecture**; **on-exchange trading compliance**; **data-ecosystem partner qualification**.

## Core capabilities

A systematic review framework across the **whole data-element lifecycle**: from accounting to securitization, from registration to trusted circulation, from exchange trading to ecosystem partnership.

1. **Capitalization review** — accounting treatment, cost accounting, initial/subsequent measurement, impairment, statement impact
2. **Securitization (ABS) review** — SPV, asset pool, credit enhancement, cash-flow projection, valuation difficulty, compliance risk
3. **Data-property registration review** (core) — six-dimension framework, public-law cross-reference, contradiction detection
4. **Trusted-data-space review** — privacy computing (federated learning, MPC, differential privacy), blockchain attestation, access control, "available-but-invisible"
5. **On-exchange trading review** — online/offline/filing rules, service flow, trade registration, ecosystem partners
6. **Hidden-information discovery** — recognizing PDF text-extraction limits; manual re-check to catch dropped fields
7. **Risk matrix & remediation-cost estimation**
8. **Reviewer operating manual**

---

## Domain 1 — Data-asset capitalization (accounting)

Per the *Interim Provisions on Accounting Treatment of Enterprise Data Resources* (MOF, 2023):

**1.1 Prerequisites**

| Condition | Review focus | Common defect |
|---|---|---|
| Control | Does the entity own/control the data? Is the title chain clear? | Vague title, multi-party overlap, contract silent on ownership |
| Expected benefit | Will the data bring future economic benefit? | Unquantifiable benefit, uncertain use case |
| Measurability | Can cost/value be reliably measured? | Hard cost aggregation, unclear indirect-cost allocation |

**1.2 Accounting treatment** — classify as intangible asset (own use) or inventory (held for sale); initial measurement = purchase price + taxes + processing + title-attestation fee + quality-assessment fee + registration/settlement fee + security-management fee; finite-life intangibles amortize, indefinite ones do not but require annual impairment testing.

**1.3 Data-asset traits vs traditional intangibles** — replicable (no loss) → complex title, multiple holders; multi-party ownership; high value volatility (fast obsolescence) → frequent re-valuation; value depends on quality and use case → need a data-quality system (GB/T 36344-2018).

**1.4 Cost-accounting review** — complete cost ledger? indirect costs reasonably allocated? attestation fees actually incurred? quality assessed per GB/T 36344-2018?

**1.5 Valuation methods** — cost method (own-use data; risk: ignores market value); income method (DCF, data with clear revenue; risk: optimistic forecast); market method (comparable trades; risk: immature market, few comparables).

---

## Domain 2 — Data-asset securitization (ABS, financial compliance)

**Flow**: asset selection → title confirmation → pool assembly → SPV → credit enhancement → rating & issuance → ongoing management.

**2.1 Pool assembly** — clear & transferable title; stable predictable cash flow; privacy/regulatory compliance (consent for personal info; surveying qualification for geographic data); pool homogeneity.

**2.2 SPV** — risk isolation from originator; review charter and isolation clauses; independent legal personality.

**2.3 Credit enhancement** — internal (senior/subordinate; is subordination enough to absorb loss?); external (third-party guarantee — guarantor qualification/scope/term); over-collateralization (data over-valuation risk); cash reserve.

**2.4 vs traditional ABS** — base asset is replicable intangible (weak over-collateral effect); cash flow depends on continued use/scenario value (hard to forecast); complex multi-party title; valuation highly quality-dependent; extra compliance dimensions (Data Security Law / PIPL).

**2.5 Valuation difficulties** — value depends on scenario; replicability → low scarcity; fast iteration → short life; cost-benefit mismatch.

---

## Domain 3 — Data-property registration review (core)

> Note: the six dimensions below are analytical dimensions derived from public law (Data Security Law / PIPL / Surveying & Mapping Law), **not** the statutory checklist of any registration measure.

**3.1.1 Applicant eligibility** — business scope covers data trading/processing? special qualifications (surveying, telecom)? security cert is the statutory MLPS (等保), not CCRC/ISO? former name disclosed, contracting party consistent? legal representative accurate?
- *Key risk*: collecting geographic info (coordinates, road imagery) without surveying qualification → may implicate the surveying-qualification regime (Surveying & Mapping Law Art. 27; issuance Art. 28; no exceeding scope Art. 29). Whether it constitutes "surveying" is for the competent authority to determine — do not draw a violation conclusion outright. (Note: the old "Art. 22" was a mis-citation; Art. 22 is real-estate surveying.)

**3.1.2 Source compliance** (most important) — source type self-consistent (self-produced / public collection / by agreement / derivative)? same product checked inconsistently across tables? full cooperation contract provided? contract term disclosed and covering the rights period? contracting party = registrant (former name/rename)? third-party rights in raw data — disposal right confirmed? personal information: if declared "no," verify field by field; public data: data produced by public-service utilities (utilities, public transport, etc.) in performing duties/services (judge public nature per Data Security Law).
- *Hidden-field tip*: text extraction may drop fields in the image layer; require screenshots or OCR re-check; read the original PDF pages by eye.
- *Key risks*: "self-produced" vs "derivative" contradiction → source untraceable; "no personal info" vs raw data containing identifying fields → risk of mis-/under-declaration (whether a false statement depends on intent and is determined case-by-case); missing contract → source legality unverifiable.

**3.1.3 Description accuracy** — structure self-consistent ("structured" vs "image")? size has units on first mention? cumulative vs snapshot stated? delivery secure (HTTP vs HTTPS)? data flow direction clear (one-way / two-way)? grading declared accurately (general / important / core)?

**3.1.4 Rights-allocation consistency** — allocation note vs declaration consistent (holding-right %)? all right-holders listed? rights period aligned with contract term? post-termination ownership clause? co-party consents to this registration?
- *Key contradictions*: note says a % but declaration lists only one party → outward appearance may differ from actual rights (whether it is a false/misleading statement is determined case-by-case); rights period with no contract support → dangling rights; collection start earlier than rights start → gap period.

**3.1.5 Application scenario** — scope too narrow (actual use may exceed)? "no secondary processing" clause vs real use conflict? two-way interaction (does demand-side data also flow in)? recipient qualification reviewed?

**3.1.6 Scale & processing capability** — performance verified (QPS, latency, concurrency)? security-management system has substance (not title-only)? execution records sufficient (training, drills, audit)? MLPS test report provided (not CCRC/ISO)? emergency plan complete?

**3.2 Cross-reference with public law & published rules** (public sources only; each locality's "refusal" grounds per its officially published measure):
1. **Source legality** — Data Security Law / PIPL / Surveying & Mapping Law (see 3.3). For geographic-info collection, qualification obtained or non-surveying determination from the authority?
2. **Personal-information compliance** (judged from public law, not internal rules) — truthful declaration; processing sensitive personal info (e.g. biometric, vehicle info linkable to a person) requires **separate consent** (PIPL Art. 29) and a **PIA** (Art. 55); image/identification devices in public places must be "necessary for public security" (Art. 26) — if the purpose is not public security, that exception does not automatically apply; "masking" must not be mistaken for anonymization (Art. 73: anonymized = unidentifiable and **irreversible**).
3. **Public / important data** — classify/grade per Data Security Law; if important data, meet important-data-processor duties (risk assessment, designate a data-security officer and body). Any "declared general but possibly important" gap?
4. **Truthfulness** — are the tables self-consistent (source type, personal-info flag, rights %, grading); any contradiction, falsity or concealment?

**3.3 Article-level cross-reference**
- *Data Security Law* Arts. 21, 27, 30, 32, 41
- *PIPL* Arts. 4, 13, 26, 28, 29; Art. 51 (security obligations), Art. 54 (compliance audit), Art. 55 (PIA for sensitive PI), Art. 73 (de-identification / anonymization)
- *Surveying & Mapping Law* — definition (Art. 2); qualification regime (Arts. 27–29); liability ("Legal Liability" chapter; penalty for unqualified surveying = Art. 55). ⚠️ Verify against the in-force 2017 revision.
- *Regulations on Surveying & Mapping Results* — invoked for result submission, secrecy grading, important geographic data; verify article numbers against the current text.
- *Several Provisions on Automobile Data Security (Trial)* Arts. 3, 8, 9, 10, 12 (still a Trial version as of revision date; verify per cac.gov.cn).
- Applicable local data-property registration measures / guidance (numbers per each locality's in-force text).

---

## Domain 4 — Trusted data space (tech + compliance)

Per the *Trusted Data Space Development Action Plan (2024–2028)*: goal — trusted multi-party circulation while protecting security and rights; break data silos; build a trust system (rule trust + tech trust). The public plan describes core capabilities such as **trusted control, resource interaction, value co-creation** (other items below are general understanding — defer to the published plan text).

**Capability review** (directions, per the published plan): catalog & identity; participant identity authentication & registration; interface standardization & interoperability; multi-party fusion / joint modeling / value co-creation; query–discover–request–respond interaction; rule-bound usage with full traceability.

**Core tech review** — privacy computing (federated learning, MPC, differential privacy → "available-but-invisible"; risk: privacy-budget overrun, intermediate leakage); blockchain (attestation/traceability); identity & permission management (fine-grained, dynamic); encryption (algorithm strength, key management).

**"Available-but-invisible" review** — real privacy computing vs mere masking? differential-privacy budget (ε) set per scenario (no single statutory threshold; smaller ε = stronger; some practice references ε<1, not a mandatory standard)? output not reversible to raw data? user confined to authorized use, cannot copy/download raw data?

**Space types** — city (public-data authorized operation), industry (sector regulation, cross-org), enterprise (supply-chain, trade secrets), personal (consent, portability), cross-border (export assessment, destination-country law).

---

## Domain 5 — On-exchange trading (trading compliance)

On-exchange trading is generally distinguished by **subject state** and **matching/order method** (e.g. "listed / on-floor," "online matched order / offline contract submission / on-floor filing"). **Each exchange's exact trade types, flow nodes and material requirements differ — always defer to the *Trading Rules* published on the target exchange's official site.** This framework reproduces no non-public wording.

General review principles (compliance logic, not any specific exchange's rules):
- Did the subject complete compliance review / property registration **before** entering the floor and listing?
- Are contract terms consistent with listing/disclosure info; any hidden adverse terms?
- Is payment settled through the exchange's **regulated account** (avoid private payment that evades oversight)?
- Does the disclosure/redaction scope of registration materials follow the exchange's **published disclosure rules** and trade-secret protection (what must be disclosed vs may be redacted — per the published rules)?

**Ecosystem roles & partners** — exchanges generally have channel / supply / product / trading-partner roles with qualification thresholds and benefits; **the exact role split, admission thresholds, appraisal and revenue rules differ by exchange — defer to the official published partner/partner-program rules.** Review: partner meets the exchange's **published** admission qualification; its products passed compliance review and registration; revenue-share/appraisal follow **published** rules and are auditable.

---

## Cross-domain tools

1. **PDF hidden-field discovery** — extract with `pypdf`/`PyPDF2`, record quality; full-text search for key fields; if a key field (e.g. a personal-info flag) is missing, require original screenshots / OCR (`tesseract`/`paddleocr`) / read original pages. *Illustrative example*: a scanned filing where key fields exist only in the image layer — text-only extraction drops them; do manual/OCR re-check.
2. **Cross-table contradiction detection** — build an attribute × table × page matrix; compare the same attribute across tables; common conflicts: source type (self-produced vs derivative), holding-right % (note vs declaration), grading (declared vs actual), personal info (flag vs actual processing).
3. **Timeline audit** — extract all timestamps (collection start, rights start/end, contract sign/expiry, capitalization, securitization maturity); spot misalignment: collection vs rights start → gap; rights end vs contract expiry → dangling; sign vs now → expired? capitalization vs collection → cost period.
4. **SaaS / service-provider role** — a tech service provider (system operator) claiming a data "holding right" via a service contract: distinguish service provider vs data producer. Analogy: a cloud provider generally does not acquire a "holding right" over its platform merchants' data merely by providing compute/storage. Generally, data produced in public service should have its holding right determined by law and public-data rules, not created/transferred by a private service contract alone — determined case-by-case. The provider may hold processing-use and product-operation rights based on substantive processing.
5. **MLPS (等保) vs CCRC/ISO** — MLPS = statutory security regime (public-security authority; obligations per the operator's grading and rating under the Cybersecurity Law etc.); CCRC = market service qualification; ISO27001/20000 = international management-system certs (not statutory). Placing CCRC/ISO under an "MLPS" heading is conceptual confusion and may mislead; whether it is a false statement is for the reviewer/authority to judge case-by-case.
6. **Anonymization vs de-identification** — de-identification (cannot identify without extra info; masking/pseudonymization → still personal info, governed by PIPL) vs anonymization (unidentifiable **and irreversible** → not personal info). If only the picture is masked while the back end retains recoverable raw data, it generally remains de-identification, not anonymization (PIPL Art. 73); reaching anonymization needs a case-by-case technical assessment.

---

## Risk matrix & remediation cost

> Note: the probabilities/levels below are **methodology illustrations**, not a prediction about any specific party; actual outcomes depend on the case and the authority's determination.

| Risk event | Prob. | Impact | Level | Domain |
|---|---|---|---|---|
| Registration refused | high | high | very high | 3 |
| Surveying-qualification penalty | high | high | very high | 3 |
| Personal-information compliance risk | med | high | high | 3,5 |
| Capitalization error | med | high | high | 1 |
| Securitization failure | med | high | high | 2 |
| Trusted-space trust collapse | low | high | med | 4 |
| On-exchange trading breach | med | med | med | 5 |
| Data breach | med | high | high | all |

> Note: the figures below are **rough illustrations, not a quote**; actual cost depends on vendor pricing and local standards. (e.g. surveying qualification ≈ several hundred k CNY / 6–12 months; PIA ≈ tens of k / 1–2 months; MLPS testing ≈ tens of k / 3–6 months — illustrative ranges only.)

---

## Output format

A review record should contain: (1) case background & file overview; (2) Domain 1 capitalization; (3) Domain 2 securitization; (4) Domain 3 registration (six dimensions, public-law cross-reference); (5) Domain 4 trusted data space; (6) Domain 5 on-exchange trading; (7) key findings (hidden info, image evidence, timeline, data flow); (8) core legal views (holding-right characterization, grading, surveying qualification, personal info); (9) error list (by severity); (10) conclusion & recommendations (review conclusion, remediation list, DD advice, regulatory advice); (11) annex (file list, method, key findings); (12) material-accuracy verification (100% against source, marked CONFIRMED / PENDING / NOT FOUND).

## Notes

1. Text-extraction limits — scanned-PDF extraction can fail; do manual/OCR re-check.
2. Hidden-information risk — applicants may hide key fields in the image layer.
3. Timeline audit — trace collection start and contract term, not just the declared rights date.
4. SaaS-role trap — beware a service provider claiming a public-data holding right.
5. Reference-material authority — training/explainer materials are reference only, not legally binding; check against formal law.
6. Fact vs inference — distinguish CONFIRMED facts from PENDING items; do not present inference as certainty.
7. Cross-domain consistency — capitalization, securitization, registration and circulation interlock.
8. Data quality — assess per GB/T 36344-2018.
9. Model contracts — the 2025 model data-circulation contracts are a key reference.
10. High-quality datasets — note whether the data falls under high-quality-dataset policy (may affect valuation/priority).
