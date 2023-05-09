"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import *


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(999) is True, 'this is not sufficient amount'
        assert product.check_quantity(1000) is True, 'this is not sufficient amount'
        assert product.check_quantity(1001) is False, 'this is more than product quantity'

    def test_product_buy(self, product):
        product.buy(1)
        assert Product.quantity == 999, 'buy method does not work for 1'
        product.buy(100)
        assert Product.quantity == 899, 'buy method does not work for 100'
        # TODO напишите проверки на метод buy


    def test_product_buy_more_than_available(self, product):
        product.buy(1500)
        assert Product.quantity >= 0, 'it is possible to buy more than available quantity'
        if Product.quantity >= 0:
            raise ValueError
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии



class TestCart:
    def test_add_product(self, product ):
        Cart.add_product(product, 1)
        assert Cart.products[product] == 1, 'Количество продуктов больше, чем количество в корзине'

    def test_remove_product(self, product):
        Cart.remove_product(1)
        assert Cart.products[product] == 0, 'Количество продуктов больше, чем количество в корзине'
        Cart.remove_product(10)
        assert Cart.products[product] > 0, 'Отрицательное количество продуктов в корзине'

    def test_clear(self, product):
        Cart.clear()
        assert len(Cart.products[product]) == 0, 'Товары не удалились из корзины'

    def test_get_total_price(self, product):
        Cart.add_product(product, 5)
        total_price = product.price * product.quantity
        assert Cart.get_total_price() == product.price * product.quantity, 'Общая цена в корзине рассчитана неверно'


    def test_buy(self, product):
        product_quantity = 5
        Cart.add_product(1)
        Cart.buy(1)
        assert  product.quantity == 5, 'Оставшееся количество продуктов совпадает'


    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
