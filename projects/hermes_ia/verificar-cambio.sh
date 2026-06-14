#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

echo "Cambios en projects/hermes_ia:"
git status --short -- projects/hermes_ia || true

echo
echo "Diff estadístico en projects/hermes_ia:"
git diff --stat -- projects/hermes_ia || true

echo
echo "Comprobando cambios fuera de projects/hermes_ia..."
outside_changes="$(git status --short | grep -v 'projects/hermes_ia/' || true)"

if [[ -n "$outside_changes" ]]; then
  echo "AVISO: hay cambios fuera de projects/hermes_ia:"
  echo "$outside_changes"
  exit 2
fi

echo "OK: no hay cambios fuera de projects/hermes_ia."
