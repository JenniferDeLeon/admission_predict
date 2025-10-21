#!/usr/bin/env bash
# Creates a Python venv in .venv, activates it, upgrades pip, and installs requirements.
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$PROJECT_DIR/.venv"

if [ ! -d "$VENV_DIR" ]; then
  python3 -m venv "$VENV_DIR"
  echo "Created venv at $VENV_DIR"
else
  echo "Using existing venv at $VENV_DIR"
fi

# Activate venv for this script
source "$VENV_DIR/bin/activate"

pip install --upgrade pip
pip install -r "$PROJECT_DIR/requirements.txt"

echo "All done. Activate with: source $VENV_DIR/bin/activate"
