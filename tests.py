from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Дон Кихот')
        collector.add_new_book('Дон Кихот')  # Должен игнорироваться
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_book_genre('1984') == 'Фантастика'

    def test_set_nonexistent_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Убить пересмешника')
        collector.set_book_genre('Убить пересмешника', 'Несуществующий Жанр')
        assert collector.get_book_genre('Убить пересмешника') == ''

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.set_book_genre('Преступление и наказание', 'Детективы')
        collector.add_new_book('Месть')
        collector.set_book_genre('Месть', 'Фантастика')
        books = collector.get_books_with_specific_genre('Детективы')
        assert 'Преступление и наказание' in books
        assert 'Месть' not in books

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Книга для детей')
        collector.set_book_genre('Книга для детей', 'Мультфильмы')
        collector.add_new_book('Темные сказки')
        collector.set_book_genre('Темные сказки', 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert 'Книга для детей' in books_for_children
        assert 'Темные сказки' not in books_for_children

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Исчезнувшая')
        collector.add_book_in_favorites('Исчезнувшая')
        assert 'Исчезнувшая' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Сияние')
        collector.add_book_in_favorites('Сияние')  # Должен игнорироваться
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Оно')
        assert 'Оно' not in collector.get_list_of_favorites_books()

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        expected_genre_dict = {'Хоббит': 'Фантастика'}
        assert collector.get_books_genre() == expected_genre_dict
