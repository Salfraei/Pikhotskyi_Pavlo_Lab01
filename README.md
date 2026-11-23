# Experiment Manager

Laboratory project for the course "Professional Python".

## Description

Console application for recording scientific experiments and calculating experimental statistics.
Individual variant: **15** — scientific experiment results.

For each experiment, the program stores `experiment_id`, `name`, `researcher`, `parameter`, `result`, and `date`.
It supports adding experiments, searching by researcher or ID, filtering by result range, and calculating average, minimum and maximum values.

## Requirements

Python 3.11+

## Installation

```powershell
python -m venv .venv
```

Activate the virtual environment (Windows PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the project in editable mode:

```powershell
python -m pip install -e .
```

## Run

```powershell
python -m student_manager.main
```

or:

```powershell
student-manager
```

Example with a CSV input file and a researcher filter:

```powershell
python -m student_manager.main --input data/experiments_sample.csv --researcher Іваненко
```

## Project structure

```text
Pikhotskyi_Pavlo_Lab01/
├── pyproject.toml
├── README.md
├── .gitignore
├── src/
│   └── student_manager/
│       ├── __init__.py
│       ├── main.py
│       ├── models.py
│       ├── services.py
│       ├── analytics.py
│       ├── readers.py
│       └── repositories.py
├── data/
│   └── experiments_sample.csv
├── tests/
│   ├── test_services.py
│   ├── test_common.py
│   ├── test_analytics_root.py
│   └── test_project_structure.py
└── report/
    └── Pikhotskyi_Pavlo_Lab01.pdf
```

`src/student_manager/models.py` — data models `Experiment`, `Researcher`, `ExperimentStatistics`.  
`src/student_manager/services.py` — business logic, search, filtering, statistics.  
`src/student_manager/main.py` — application entry point.  
`src/student_manager/analytics.py` — additional statistics.  
`src/student_manager/readers.py` — CSV import and JSON export.  
`src/student_manager/repositories.py` — in-memory repository.  
`tests/` — automated tests.  
`data/` — sample scientific experiment data.  
`report/` — laboratory report.

## Author

Student: Піхоцький Павло  
Group: ФеП-31  
Variant: 15
