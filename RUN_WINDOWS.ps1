$ErrorActionPreference = "Stop"
if (-not (Test-Path ".venv\Scripts\python.exe")) { py -3 -m venv .venv }
& .\.venv\Scripts\python.exe -m pip install -e ".[dev]"
& .\.venv\Scripts\python.exe -m pytest -q
& .\.venv\Scripts\python.exe -m student_manager.main
