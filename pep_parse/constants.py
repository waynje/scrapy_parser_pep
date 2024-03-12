from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'
RESULTS_PEP = f'{RESULTS}/pep_%(time)s.csv'
