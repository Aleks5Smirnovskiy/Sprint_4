from main import BooksCollector


class TestBooksCollectorGetBookGenre:
    # Тестируем метод get_book_genre/ Тесты проверяют, что метод get_book_genre: - возвращает жанр для существующей книги; - возвращает None для отсутствующей книги.

    def test_get_book_genre_returns_genre_if_set(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_get_book_genre_returns_none_for_unknown_book(self):
        collector = BooksCollector()

        assert collector.get_book_genre('Неизвестная книга') is None
