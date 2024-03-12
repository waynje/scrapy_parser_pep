from collections import defaultdict
import csv
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def open_spider(self, spider):
        """Создаем словарь для статусов."""
        self.counter = defaultdict(int)
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        """По ключу ищем нужное значение и добавляем к счетчику 1."""
        self.counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        """Получаем время, записываем в файл, получаем общее колво статусов."""
        time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        path = self.results_dir / f'status_summary_{time}.csv'
        # total = sum(self.counter.values())
        with open(path, mode="w", encoding="utf-8") as file:
            writer = csv.writer(
                file,
                dialect="unix",
                delimiter=";"
            )
            writer.writerows(
                (
                    ("Статус", "Количество"),
                    *self.counter.items(),
                    ("Total", sum(self.counter.values()))
                )
            )
