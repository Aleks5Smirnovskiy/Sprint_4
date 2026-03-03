from main import BooksCollector


class TestBooksCollectorAddTwoBooks:
    # Тестируем метод add_new_book: добавление двух разных книг 
    # Тест проверяет, что при добавлении двух разных книг они обе попадают в общий словарь books_genre.


    def test_add_new_book_add_two_different_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        books = collector.get_books_genre()

        assert len(books) == 2
        assert 'Гордость и предубеждение и зомби' in books
        assert 'Что делать, если ваш кот хочет вас убить' in books
