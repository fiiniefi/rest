from abc import ABC, abstractmethod
from typing import List

from src.orders.exceptions import BadRequest, NotFound
from src.orders.models import Order, OrderFields


class OrdersRepository(ABC):
    @abstractmethod
    def create(self, order: Order) -> None:
        pass

    @abstractmethod
    def update(self, fields_to_update: OrderFields) -> None:
        pass

    @abstractmethod
    def delete(self, order_id: str) -> None:
        pass

    @abstractmethod
    def get_order(self, order_id: str) -> Order:
        pass

    @abstractmethod
    def get_orders(self) -> List[Order]:
        pass


class InMemoryOrdersRepository(OrdersRepository):
    def __init__(self) -> None:
        self.data = [
            {
                "id": "ord1",
                "customer_id": "cust1",
                "products": [{"id": "prod1", "name": "Name1"}],
            }
        ]

    def create(self, order: Order) -> None:
        self.data.append(order.dict())

    def update(self, fields_to_update: OrderFields) -> None:
        self.data = [
            order if order.id != fields_to_update.id else {**order, **fields_to_update}
            for order in self.data
        ]

    def delete(self, order_id: str) -> None:
        try:
            order_ids = [{"id": order["id"]} for order in self.data]
            self.data.pop(order_ids.index({"id": order_id}))
        except ValueError:
            raise BadRequest("Element not in the data store")

    def get_order(self, order_id: str) -> Order:
        try:
            return next(
                Order.parse_obj(order) for order in self.data if order["id"] == order_id
            )
        except StopIteration:
            raise NotFound(f"Order {order_id} not found")

    def get_orders(self) -> List[Order]:
        return [Order.parse_obj(order) for order in self.data]
