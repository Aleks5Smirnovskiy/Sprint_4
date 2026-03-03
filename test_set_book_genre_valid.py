from main import BooksCollector
import pytest


class TestBooksCollectorSetBookGenreValid:
    # Тестируем метод set_book_genre: установка допустимого жанра/ Тест проверяет, что существующей книге можно установить один из разрешённых жанров.

    @pytest.mark.parametrize(
        'genre',
        ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'],
    )
    def test_set_book_genre_success_for_existing_book_and_valid_genre(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')

        collector.set_book_genre('Гарри Поттер', genre)

        assert collector.get_book_genre('Гарри Поттер') == genre
