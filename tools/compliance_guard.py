#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compliance regression guard.

Scans all Markdown files in the repo for patterns that must NEVER reappear:
- known-wrong legal citations,
- wording reproduced from non-public internal material,
- real company / case-party identifiers (re-identification risk),
- hard legal conclusions that must stay hedged.

Exits non-zero (fails CI) if any pattern is found. Run locally:
    python3 tools/compliance_guard.py
"""
import io
import re
import sys
from pathlib import Path

# (label, regex). Each pattern is something the clean-room rewrite removed and
# that should not creep back in. Keep these specific to avoid false positives on
# legitimate meta-mentions (e.g. the "we deliberately do NOT reproduce …" note).
PATTERNS = [
    ("known-wrong citation (测绘资质应为第27条)", r"违反《测绘法》第22条"),
    ("wrong penalty article",                   r"约第六?十?八?条|约第68条"),
    ("internal taxonomy (采集三类违规)",          r"授权类、公共采集类、管理类"),
    ("internal list (交易可隐藏项)",              r"一般不得隐藏"),
    ("internal fixed naming (三统一)",            r"三统一"),
    ("named exchange",                          r"广州数据交易所"),
    ("real company names",                      r"阿里云|淘宝卖家|腾讯云"),
    ("case-party identifiers",                  r"珍宝巴士|交信投"),
    ("unified social credit code",              r"9144[0-9A-Za-z]{14}"),
    ("contract id pattern",                     r"CT-0\d-\d{6}"),
    ("un-hedged hard conclusion (虚假声明)",      r"→\s*虚假声明"),
    ("un-hedged hard conclusion (权利外观欺诈)",  r"→\s*权利外观欺诈"),
]

ROOT = Path(__file__).resolve().parent.parent
md_files = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)

hits = []
for path in md_files:
    text = io.open(path, encoding="utf-8").read()
    rel = path.relative_to(ROOT)
    for label, pat in PATTERNS:
        for m in re.finditer(pat, text):
            line = text.count("\n", 0, m.start()) + 1
            hits.append((str(rel), line, label, m.group(0)))

if hits:
    print("❌ compliance-guard: forbidden patterns found (clean-room regression):")
    for rel, line, label, frag in hits:
        print(f"   {rel}:{line}  [{label}]  -> {frag!r}")
    print("\nThese were removed during the clean-room rewrite and must not return.")
    print("If a hit is a legitimate corrective/meta mention, tighten the pattern in tools/compliance_guard.py.")
    sys.exit(1)

print(f"✅ compliance-guard passed: scanned {len(md_files)} markdown file(s), no forbidden patterns.")
