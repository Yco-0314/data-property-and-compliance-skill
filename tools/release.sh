#!/usr/bin/env bash
# Cut a release. Tags the current commit and pushes the tag; the
# .github/workflows/release.yml workflow then runs the compliance guard and
# creates a GitHub Release with auto-generated, categorized notes
# (.github/release.yml).
#
# Usage:
#   tools/release.sh vX.Y.Z          # e.g. tools/release.sh v1.1.0
#
# Notes:
#   - Run from a clean working tree on the default branch.
#   - Remember to bump the version line in SKILL.md / SKILL.en.md first.
set -euo pipefail

ver="${1:-}"
if [[ ! "$ver" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "usage: tools/release.sh vX.Y.Z   (e.g. tools/release.sh v1.1.0)" >&2
  exit 1
fi

if [[ -n "$(git status --porcelain)" ]]; then
  echo "✗ working tree not clean — commit or stash first." >&2
  exit 1
fi

git fetch --tags --quiet
if git rev-parse -q --verify "refs/tags/${ver}" >/dev/null; then
  echo "✗ tag ${ver} already exists." >&2
  exit 1
fi

echo "→ local compliance guard…"
python3 tools/compliance_guard.py

echo "→ tagging ${ver} and pushing…"
git tag -a "${ver}" -m "${ver}"
git push origin "${ver}"

echo "✓ pushed tag ${ver}."
echo "  The 'release' workflow will publish the GitHub Release with generated notes:"
echo "  https://github.com/Yco-0314/data-property-and-compliance-skill/releases"
