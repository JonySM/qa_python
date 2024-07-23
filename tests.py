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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    import pytest
    @pytest.mark.parametrize('name', ['  ', 'оооченьоченьоченьоченьдлинноеназваниекниги'])
    def test_add_new_book_invalid_names(self, name):
        collector = BooksCollector()
        assert name not in collector.get_books_genre()

    def test_set_book_genre_for_book(self):
        collector = BooksCollector()

        new_book = 'Метод'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, 'Детективы')
        assert collector.get_book_genre(new_book) == 'Детективы'

    def test_get_books_with_specific_genre_for_returned_books(self):
        collector = BooksCollector()

        new_book = 'Оно'
        new_book_2 = 'Кладбище домашних животных'
        collector.add_new_book(new_book)
        collector.add_new_book(new_book_2)
        collector.set_book_genre(new_book, 'Ужасы')
        collector.set_book_genre(new_book_2, 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Оно', 'Кладбище домашних животных']

    def test_get_books_genre_get_one_book(self):
        collector = BooksCollector()

        new_book = 'Вторая жизнь Уве'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, 'Комедии')

        assert collector.get_books_genre() == {'Вторая жизнь Уве': 'Комедии'}

    def test_get_books_for_children_for_returned_books(self):
        collector = BooksCollector()

        new_book = 'Оно'
        new_book_2 = 'Колобок'
        collector.add_new_book(new_book)
        collector.add_new_book(new_book_2)
        collector.set_book_genre(new_book, 'Ужасы')
        collector.set_book_genre(new_book_2, 'Мультфильмы')
        assert collector.get_books_for_children() == [new_book_2] and collector.get_books_for_children() != [new_book]

    def test_add_book_in_favorites_one_book(self):
        collector = BooksCollector()

        new_book = 'Приключения Электроника'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, 'Фантастика')
        collector.add_book_in_favorites(new_book)
        assert collector.get_list_of_favorites_books() == [new_book]

    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()

        new_book = 'Приключения Электроника'
        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, 'Фантастика')
        collector.add_book_in_favorites(new_book)
        collector.delete_book_from_favorites(new_book)
        assert collector.get_list_of_favorites_books() != [new_book]

    def test_get_list_of_favorites_books_without_book(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

























































