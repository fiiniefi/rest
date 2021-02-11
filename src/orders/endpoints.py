from fastapi import APIRouter, Depends
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_200_OK,
    HTTP_202_ACCEPTED,
    HTTP_204_NO_CONTENT,
)

from src.common.models import Hypermedia
from src.orders.models import Order, OrderFields, OrderHypermedia, OrdersHypermedia
from src.orders.repositories import InMemoryOrdersRepository, OrdersRepository

router = APIRouter()


@router.post("/orders/", status_code=HTTP_201_CREATED, response_model=Hypermedia)
def create_order(
    order: Order, repo: OrdersRepository = Depends(InMemoryOrdersRepository)
) -> Hypermedia:
    repo.create(order)
    return Hypermedia(_links={"self": f"/orders/{order.id}", "orders": "/orders/"})


@router.patch(
    "/orders/{order_id}", status_code=HTTP_202_ACCEPTED, response_model=Hypermedia
)
def update_order(
    fields_to_update: OrderFields,
    repo: OrdersRepository = Depends(InMemoryOrdersRepository),
) -> Hypermedia:
    repo.update(fields_to_update)
    return Hypermedia(_links={"self": f"/orders/{order.id}", "orders": "/orders/"})


@router.delete(
    "/orders/{order_id}", status_code=HTTP_204_NO_CONTENT, response_model=Hypermedia
)
def delete_order(
    order_id: str, repo: OrdersRepository = Depends(InMemoryOrdersRepository)
) -> Hypermedia:
    repo.delete(order_id)
    return Hypermedia(_links={"orders": "/orders/"})


@router.get("/orders/", status_code=HTTP_200_OK, response_model=OrdersHypermedia)
def orders(
    repo: OrdersRepository = Depends(InMemoryOrdersRepository),
) -> OrdersHypermedia:
    orders = [
        OrderHypermedia.parse_obj(
            {**order.dict(), "_links": {"self": f"/orders/{order.id}/"}}
        )
        for order in repo.get_orders()
    ]
    return OrdersHypermedia(orders=orders, _links={"self": "/orders/"})


@router.get(
    "/orders/{order_id}", status_code=HTTP_200_OK, response_model=OrderHypermedia
)
def order(
    order_id: str, repo: OrdersRepository = Depends(InMemoryOrdersRepository)
) -> OrderHypermedia:
    order = repo.get_order(order_id)
    return OrderHypermedia.parse_obj(
        {
            **order.dict(),
            "_links": {"self": f"/orders/{order.id}/", "orders": "/orders/"},
        }
    )
