from main import BooksCollector


class TestBooksCollectorGetBooksWithSpecificGenre:
    # Тестируем метод get_books_with_specific_genre. Тесты проверяют, что метод get_books_with_specific_genre: - возвращает только книги нужного жанра; - возвращает пустой список для жанра, которого нет в списке допустимых.

    def test_get_books_with_specific_genre_returns_only_that_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Корпорация монстров')

        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.set_book_genre('Корпорация монстров', 'Мультфильмы')

        horror_books = collector.get_books_with_specific_genre('Ужасы')

        assert horror_books == ['Оно']

    def test_get_books_with_specific_genre_invalid_genre_returns_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        result = collector.get_books_with_specific_genre('Документалистика')

        assert result == []
