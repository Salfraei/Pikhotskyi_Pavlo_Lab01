# Git — лабораторна №1, варіант №15

У методичці (розділ 22) наведено три послідовні коміти. Якщо репозиторій **новий і порожній**, у корені папки виконайте:

```powershell
git init -b main
git add .gitignore pyproject.toml src/student_manager/__init__.py
git commit -m "Create project structure"
git add src/student_manager/models.py src/student_manager/services.py src/student_manager/analytics.py src/student_manager/readers.py src/student_manager/repositories.py
git commit -m "Add experiment model and business logic"
git add src/student_manager/main.py README.md START_HERE.md RUN_WINDOWS.ps1 data/ tests/ report/ GIT_COMMANDS.md
git commit -m "Add application entry point and documentation"
git status
git log --oneline
```

Підключення нового порожнього репозиторію GitHub:

```powershell
git remote add origin https://github.com/Salfraei/Pikhotskyi_Pavlo_Lab01.git
git push -u origin main
```

**Якщо репозиторій уже існує** (ти вже робив коміти), не виконуй `git init` знову, не переписуй історію та не повторюй штучно початкові коміти. Спочатку переконайся, що не маєш власних незбережених змін, потім у **наявній локальній папці з `.git`** онови файли з ZIP і запусти:

```powershell
git status
git add -A
git commit -m "Lab01: align README and variant 15 with methodology"
git push origin main
git log --oneline
```

Не копіюйте `.venv/`, `__pycache__/` і службові файли зі старого проєкту. Для реального PDF доказу Git використовуйте `git status` та `git log --oneline` саме зі свого репозиторію після комітів.
