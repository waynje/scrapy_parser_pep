from collections import defaultdict
import csv
from datetime import datetime

from .constants import BASE_DIR, RESULTS

RESULTS_DIR = BASE_DIR / RESULTS


class PepParsePipeline:

    def open_spider(self, spider):
        """Создаем словарь для статусов."""
        self.counter = defaultdict(int)
        RESULTS_DIR.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        """По ключу ищем нужное значение и добавляем к счетчику 1."""
        self.counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        """Получаем время, записываем в файл, получаем общее колво статусов."""
        time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        path = RESULTS_DIR / f'status_summary_{time}.csv'
        with open(path, mode="w", encoding="utf-8") as file:
            writer = csv.writer(
                file,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            )
            writer.writerows(
                (
                    ("Статус", "Количество"),
                    *self.counter.items(),
                    ("Всего", sum(self.counter.values()))
                )
            )
