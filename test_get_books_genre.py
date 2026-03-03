from main import BooksCollector


class TestBooksCollectorGetBooksGenre:
    # Тестируем метод get_books_genre. Тесты проверяют, что метод get_books_genre определяет жанр по книге.

    def test_get_books_genre_returns_full_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Шерлок Холмс')

        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        result = collector.get_books_genre()

        assert result == {
            'Оно': 'Ужасы',
            'Шерлок Холмс': 'Детективы',
        }
