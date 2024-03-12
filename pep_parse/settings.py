from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
RESULTS = 'results'
RESULTS_PEP = f'{RESULTS}/pep_%(time)s.csv'

BOT_NAME = 'pep_parse'

NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True

FEEDS = {RESULTS_PEP: {
         'format': 'csv',
         'fields': ['number', 'name', 'status'],
         'overwrite': True}, }

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
