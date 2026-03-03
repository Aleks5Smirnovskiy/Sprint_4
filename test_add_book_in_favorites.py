from main import BooksCollector


class TestBooksCollectorFavoritesAdd:
    # Тестируем метод add_book_in_favorites. Тесты проверяют, что метод add_book_in_favorites: - добавляет в избранное только существующие книги; - не добавляет одну и ту же книгу в избранное дважды.

    def test_add_book_in_favorites_adds_only_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')

        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Неизвестная книга')

        favorites = collector.get_list_of_favorites_books()

        assert favorites == ['Оно']

    def test_add_book_in_favorites_cannot_add_same_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')

        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Оно')

        favorites = collector.get_list_of_favorites_books()

        assert favorites == ['Оно']
