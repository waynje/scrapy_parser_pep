from .constants import RESULTS_PEP

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
ROBOTSTXT_OBEY = True

FEEDS = {RESULTS_PEP: {
         'format': 'csv',
         'fields': ['number', 'name', 'status'],
         'overwrite': True}, }

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
