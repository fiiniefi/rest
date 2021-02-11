from typing import List, Optional

from pydantic import BaseModel

from src.common.models import Hypermedia


class Product(BaseModel):
    id: str
    name: str


class Order(BaseModel):
    id: str
    products: List[Product]
    customer_id: str
    status: str


class OrderFields(BaseModel):
    id: str
    products: Optional[List[Product]] = None
    status: Optional[str] = None


class ProductHypermedia(Product, Hypermedia):
    pass


class OrderHypermedia(Order, Hypermedia):
    pass


class OrdersHypermedia(Hypermedia):
    orders: List[OrderHypermedia]
