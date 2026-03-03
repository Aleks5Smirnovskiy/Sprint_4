
from main import BooksCollector


class TestBooksCollectorGetBooksForChildren:
    # Тестируем метод get_books_for_children. Тест проверяет, что метод get_books_for_children возвращает только книги с жанрами без возрастных ограничений.

    def test_get_books_for_children_excludes_age_restricted_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Корпорация монстров')
        collector.add_new_book('Один дома')

        collector.set_book_genre('Оно', 'Ужасы')                # 18+
        collector.set_book_genre('Шерлок Холмс', 'Детективы')   # 18+
        collector.set_book_genre('Корпорация монстров', 'Мультфильмы')
        collector.set_book_genre('Один дома', 'Комедии')

        children_books = collector.get_books_for_children()

        assert 'Оно' not in children_books
        assert 'Шерлок Холмс' not in children_books
        assert 'Корпорация монстров' in children_books
        assert 'Один дома' in children_books
