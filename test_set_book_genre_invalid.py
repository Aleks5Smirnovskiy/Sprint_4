from main import BooksCollector


class TestBooksCollectorSetBookGenreInvalid:
    # Тестируем метод set_book_genre: некорректные случаи/ Тесты проверяют, что жанр не устанавливается, если книга не добавлена или жанр не из списка допустимых.

    def test_set_book_genre_not_set_for_unknown_book(self):
        collector = BooksCollector()

        collector.set_book_genre('Несуществующая книга', 'Ужасы')

        assert collector.get_book_genre('Несуществующая книга') is None

    def test_set_book_genre_not_set_for_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга без жанра')

        collector.set_book_genre('Книга без жанра', 'Документалистика')

        assert collector.get_book_genre('Книга без жанра') == ''
