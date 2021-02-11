from abc import ABC, abstractmethod
from typing import List

from src.products.exceptions import NotFound
from src.products.models import Product


class ProductsRepository(ABC):
    @abstractmethod
    def get_product(self, product_id: str) -> Product:
        pass

    @abstractmethod
    def get_products(self) -> List[Product]:
        pass


class InMemoryProductsRepository(ProductsRepository):
    def __init__(self) -> None:
        self.data = [{"id": "prod1", "name": "Name1", "quantity": 3}]

    def get_product(self, product_id: str) -> Product:
        try:
            return next(
                Product.parse_obj(product)
                for product in self.data
                if product["id"] == product_id
            )
        except StopIteration:
            raise NotFound(f"Product {product_id} not found")

    def get_products(self) -> List[Product]:
        return [Product.parse_obj(product) for product in self.data]
