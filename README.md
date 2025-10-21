# Admission Predict — Setup

Create a Python virtual environment and install dependencies for the notebook on macOS (zsh).

Quick steps:

1. Create venv and activate (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Upgrade pip and install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. If you're using VS Code, select the interpreter at `.venv/bin/python`.

If you prefer an automated script, run `./setup_venv.sh` (make it executable first).
