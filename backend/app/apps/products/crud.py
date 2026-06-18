from apps.core.base_crud import BaseCRUDManager
from apps.products.models import Category, Order, Product


class ProductCRUDManager(BaseCRUDManager):
    def __init__(self):
        self.model = Product


class CategoryCRUDManager(BaseCRUDManager):
    def __init__(self):
        self.model = Category


class OrderCRUDManager(BaseCRUDManager):
    def __init__(self):
        self.model = Order


product_manager = ProductCRUDManager()
category_manager = CategoryCRUDManager()
order_manager = OrderCRUDManager()
