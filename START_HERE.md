# Лабораторна №1 — варіант №15

Відкрийте папку `Pikhotskyi_Pavlo_Lab01` у VS Code. Основний `README.md` має ту саму структуру, що й приклад у методичці (розділ 21).

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m student_manager.main
.\.venv\Scripts\python.exe -m pytest -v
```

Для роботи з прикладом CSV:

```powershell
.\.venv\Scripts\python.exe -m student_manager.main --input data/experiments_sample.csv
```

Для завантаження на GitHub використайте інструкцію `GIT_COMMANDS.md`.
