from main import BooksCollector


class TestBooksCollectorAddNewBookDuplicate:
    # Тестируем метод add_new_book: попытка добавить дубликат. Тест проверяет, что одна и та же книга не добавляется в словарь books_genre дважды.

    def test_add_new_book_cannot_add_same_twice(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.add_new_book('1984')

        books = collector.get_books_genre()

        assert len(books) == 1
        assert '1984' in books
