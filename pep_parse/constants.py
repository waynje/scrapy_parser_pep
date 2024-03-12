from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = BASE_DIR / 'results'
RESULTS_PEP = 'results/pep_%(time)s.csv'