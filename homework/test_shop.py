
import pytest
from qa_guru_python_5_8.homework.models import *


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart():
    return Cart()


class TestProducts:

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(999) is True, 'this is not sufficient amount'
        assert product.check_quantity(1000) is True, 'this is not sufficient amount'
        assert product.check_quantity(1001) is False, 'this is more than product quantity'

    def test_product_buy(self, product):
        print(product.quantity, 'This is product quantity')
        product.buy(1)
        assert product.quantity == 999, 'buy method does not work for 1'
        product.buy(100)
        assert product.quantity == 899, 'buy method does not work for 100'
        # TODO напишите проверки на метод buy



    def test_product_buy_more_than_available(self, product):
        #print('quantity is',product.quantity)
        product.buy(1000)
        assert product.quantity >= 0, 'it is possible to buy more than available quantity'
        if product.quantity < 0:
            raise ValueError
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии



class TestCart:
    def test_add_product(self, product, cart):
        cart.add_product(product)
        #assert Cart.products[product] == 1, 'Количество продуктов больше, чем количество в корзине'

    def test_remove_product(self, product, cart):
        cart.add_product(product,10)
        cart.remove_product(product, 10)
        print('this is quantity', cart.products)
        assert len(cart.products) == 0, 'Количество продуктов больше, чем количество в корзине'


    def test_clear(self, product, cart):
        cart.clear()
        assert len(cart.products) == 0, 'Товары не удалились из корзины'

    def test_get_total_price(self, product, cart):
        cart.add_product(product)
        total_price = product.price * product.quantity
        assert cart.get_total_price() == product.price , 'Общая цена в корзине рассчитана неверно'


    def test_buy(self, product, cart):
        cart.add_product(product,190)
        with pytest.raises(ValueError):
            assert cart.buy()
