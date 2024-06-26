import scrapy

from ..items import PepParseItem


class PepSpider(scrapy.Spider):

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        """Получаем все ссылки и переходим по ним в методе parse_pep."""
        for link in response.css(
            'tbody tr a[href^="pep-"]'
        ):
            yield response.follow(
                link, callback=self.parse_pep
            )

    def parse_pep(self, response):
        """Обрабатываем данные из страницы PEP."""
        title_text = response.css('h1.page-title::text').get().split()
        yield PepParseItem(
            number=title_text[1],
            name=''.join(title_text[3:]).strip(),
            status=response.css('dt:contains("Status")+dd abbr::text').get()
        )
