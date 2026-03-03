from main import BooksCollector


class TestBooksCollectorFavoritesDeleteAndGet:
    # Тестируем методы delete_book_from_favorites и get_list_of_favorites_books. Тесты проверяют: - удаление книги из избранного, если она там есть; - игнорирование удаления, если книги в избранном нет; - корректное возвращение текущего списка избранных книг.

    def test_delete_book_from_favorites_remove_if_exists(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Шерлок Холмс')

        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Шерлок Холмс')

        collector.delete_book_from_favorites('Оно')

        favorites = collector.get_list_of_favorites_books()

        assert 'Оно' not in favorites
        assert 'Шерлок Холмс' in favorites

    def test_delete_book_from_favorites_ignored_if_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')

        collector.delete_book_from_favorites('Оно')  # не добавляли в избранное

        favorites = collector.get_list_of_favorites_books()

        assert favorites == []

    def test_get_list_of_favorites_books_returns_current_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Шерлок Холмс')

        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Шерлок Холмс')

        favorites = collector.get_list_of_favorites_books()

        assert favorites == ['Оно', 'Шерлок Холмс']
