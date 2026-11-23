# Запуск ЛР №1 у VS Code

Відкрийте **цю** папку (а не каталог попередньої роботи).

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e ".[dev]"
.\.venv\Scripts\python.exe -m pytest -v
.\.venv\Scripts\python -m student_manager.main
```

Папку `.venv` до GitHub не додавайте. Файли цього пакета викладати саме в корінь репозиторію.
