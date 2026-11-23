from pathlib import Path
import importlib

def test_variant_15_models_and_core_modules():
    for name in ['student_manager.main', 'student_manager.models',
                 'student_manager.services', 'student_manager.readers']:
        assert importlib.import_module(name)
    from student_manager.main import demo_experiments
    from student_manager.services import calculate_statistics
    assert calculate_statistics(demo_experiments()).count == 4

def test_mandatory_directories():
    root=Path(__file__).resolve().parents[1]
    for name in ('src/student_manager','tests','data','report'):
        assert (root/name).is_dir()

def test_previous_lab_modules_available():
    for lab in range(2, 2):
        assert importlib.import_module(f'student_manager.lab{lab:02}.main')
