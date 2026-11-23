# GitHub — ЛР №01

Репозиторій: `https://github.com/Salfraei/Pikhotskyi_Pavlo_Lab01.git`

Для існуючого репозиторію **не запускайте `git init` повторно**. Оновіть файли через скрипт `Update-GitHub-Labs.ps1` із комплекту, або в корені локального репозиторію:

```powershell
git status
git pull --ff-only origin main
git add -A
git commit -m "Lab01: align project with variant 15 and requirements"
git push origin main
```

Для нового репозиторію: `git init -b main`, `git remote add origin URL`, після додавання файлів `git push -u origin main`. Не використовуйте force push.
