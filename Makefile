# On Windows without make: run the underlying commands directly (see README).

.PHONY: install test lint dataset transforms detectors report reproduce

install:
	pip install -e ".[dev]"

test:
	pytest -q

lint:
	ruff check src tests scripts

dataset:
	python scripts/01_build_dataset.py

transforms:
	python scripts/02_apply_transforms.py

detectors:
	python scripts/03_run_detectors.py

report:
	python scripts/04_make_report.py

reproduce: dataset transforms detectors report
