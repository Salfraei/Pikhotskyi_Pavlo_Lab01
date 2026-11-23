"""CLI for the common scientific-experiments project (variant 15)."""
from __future__ import annotations
import argparse
from pathlib import Path
from student_manager.models import Experiment
from student_manager.readers import read_experiments_csv
from student_manager.services import ExperimentService

def demo_experiments() -> list[Experiment]:
    return [
        Experiment(1,"Температурне дослідження","Олена Іваненко","temperature",23.4,"2026-10-11"),
        Experiment(2,"Контрольна серія","Андрій Петренко","voltage",4.95,"2026-10-12"),
        Experiment(3,"Повторне вимірювання","Олена Іваненко","temperature",25.2,"2026-10-13"),
        Experiment(4,"Вимірювання опору","Ірина Коваль","resistance",101.5,"2026-10-14"),
    ]

def run_demo(input_path: Path | None = None, researcher: str = "Іваненко") -> None:
    records = list(read_experiments_csv(input_path)) if input_path else demo_experiments()
    service = ExperimentService(records)
    print("Professional Python | Lab 01 | Scientific experiments | Variant 15")
    for exp in service.list_all():
        print(f"#{exp.id}: {exp.name}; {exp.researcher}; {exp.parameter}={exp.result}; {exp.date}")
    print("Researcher search:", [x.name for x in service.by_researcher(researcher)])
    stats = service.statistics()
    print(f"Count={stats.count}; Average={stats.average:.3f}; Min={stats.minimum}; Max={stats.maximum}")
    print("Range 20..100:", [e.experiment_id for e in service.in_range(20,100)])

def main() -> None:
    parser = argparse.ArgumentParser(description="Scientific experiment registry / variant 15")
    parser.add_argument("--input", type=Path, help="CSV with variant 15 fields")
    parser.add_argument("--researcher", default="Іваненко")
    args = parser.parse_args()
    run_demo(args.input, args.researcher)

if __name__ == "__main__":
    main()
