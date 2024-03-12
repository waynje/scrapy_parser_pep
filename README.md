# Проект асинхронного парсинга документации Python
## **Основная цель проекта**
Изучение возможностей фреймворка [Scrapy](https://docs.scrapy.org/en/latest/index.html) 
## **Описание проекта**
Выполняется парсинг данных со страницы с общей информацией о РЕР (https://peps-python.org/),
переход по ссылкам и сбор данных о каждом РЕР.
Парсер подготавливает данные и сохраняет их в два файла формата ***csv"** в папку
## **Стек**
* Python v3+
* Scrapy 2.5.1
## **Запуск проекта**
Выполните следующие команды в терминале:
1. Клонировать проект из репозитория
```shell
git clone git@github.com:waynje/scrapy_parser_pep.git
```
2. Создать, активировать виртуальное окружение и в него установить зависимости:
```shell
cd scrapy_parser_pep
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Запустить парсер из командной строки:
```shell
scrapy crawl pep
```
## _Вывод результатов_
Результатом работы парсера будет создание двух файлов:
1. содержит список всех PEP (*number", "'name"", ""status"*);
2. _status_ содержит сводку по статусам РЕР:
сколько найдено документов в каждом статусе ("'Статус"*, "Количество"*).
В последней строке этого файла в колонке "Всего" выводится общее количество всех документов.
* Автор: ([Waynje](https://github.com/waynje))