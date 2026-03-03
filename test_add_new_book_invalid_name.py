
from main import BooksCollector
import pytest


class TestBooksCollectorAddNewBookInvalidName:
    # Тестируем метод add_new_book: некорректная длина названия. Тесты проверяют, что книга не добавляется, если длина названия некорректна.

    @pytest.mark.parametrize(
        'name',
        [
            '',          # слишком короткое название
            'A' * 41,    # слишком длинное название
        ],
    )
    def test_add_new_book_name_invalid_by_length(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0
