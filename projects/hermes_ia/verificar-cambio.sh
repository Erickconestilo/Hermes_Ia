#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

echo "Cambios en projects/hermes_ia:"
git status --short -- projects/hermes_ia || true

echo
echo "Diff estadístico en projects/hermes_ia:"
git diff --stat -- projects/hermes_ia || true
