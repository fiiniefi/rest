from typing import List

from pydantic import BaseModel

from src.common.models import Hypermedia


class Product(BaseModel):
    id: str
    name: str
    quantity: int


class ProductHypermedia(Product, Hypermedia):
    pass


class ProductsHypermedia(Hypermedia):
    products: List[ProductHypermedia]
