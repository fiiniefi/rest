from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from src.orders.models import Order
from src.orders.repositories import InMemoryOrdersRepository
from tests.api_calls import get_order, delete_order


def test_get_order_returns_404_when_not_found():
    pass


def test_get_order_returns_order_correctly(app, api_client):
    # given
    order_id = "o1"
    order = Order(id=order_id, products=[], customer_id="c1")
    repo = InMemoryOrdersRepository()
    repo.create(order)
    app.dependency_overrides[InMemoryOrdersRepository] = lambda: repo

    # when
    response = get_order(api_client, order_id)

    # then
    assert response.status_code == HTTP_200_OK
    assert Order.parse_obj(response.json()) == Order(
        id=order_id, products=[], customer_id="c1"
    )


def test_get_orders_returns_empty_list_when_there_is_no_orders():
    pass


def test_get_orders_returns_orders_correctly():
    pass


def test_delete_order_raises_400_when_order_with_given_id_does_not_exist(
    app, api_client
):
    # given
    order_id = "unexisting"
    repo = InMemoryOrdersRepository()
    app.dependency_overrides[InMemoryOrdersRepository] = lambda: repo

    # when
    response = delete_order(api_client, order_id)

    # then
    assert response.status_code == HTTP_400_BAD_REQUEST


def test_delete_order_raises_400_when_wrong_order_status():
    pass


def test_delete_order_successfully_deletes_given_order():
    pass


def test_update_order_raises_400_when_order_with_given_id_does_not_exist():
    pass


def test_update_order_raises_400_when_added_item_not_in_store():
    pass


def test_update_order_raises_400_when_wrong_order_status():
    pass


def test_update_order_successfully_updates_order():
    pass


def test_create_order_raises_400_when_order_with_given_id_already_exists():
    pass


def test_create_order_raises_400_when_at_least_one_product_not_in_store():
    pass


def test_create_order_successfully_creates_valid_order():
    pass
