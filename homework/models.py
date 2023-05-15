from dataclasses import dataclass

@dataclass
class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def check_quantity(self, quantity) -> bool:
        if quantity <= self.quantity:
            return True
        else:
            return False
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        #raise NotImplementedError


    def buy(self, quantity):
        if not self.check_quantity(quantity):
            raise ValueError
        else:
            self.quantity -= quantity
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        #raise NotImplementedError

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

        #raise NotImplementedError

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if self.products[product] >= remove_count or remove_count is None:
            del self.products[product]
        else:
            self.products[product] -= remove_count
        #raise NotImplementedError

    def clear(self):
        self.products.clear()
        #raise NotImplementedError

    def get_total_price(self) -> float:
        #products: dict[Product, int]
        total_price = 0
        for key, value in self.products.items():
            total_price += value * key.price
        return total_price
        #raise NotImplementedError

    def buy(self):
        for product, quant in self.products.items():
            if quant > product.quantity:
                raise ValueError
            for i in range(quant):
                product.buy(quant)

        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        raise ValueError