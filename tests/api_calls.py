import json


def get_product(api_client, product_id):
    api_client.get(f"/products/{product_id}/")


def get_products(api_client):
    api_client.get("/products/")


def get_order(api_client, order_id):
    api_client.get(f"/orders/{order_id}/")


def get_orders(api_client):
    api_client.get("/orders/")


def create_order(api_client, order):
    api_client.post("/orders/", data=json.dumps(order.dict()))


def update_order(api_client, fields_to_update):
    api_client.patch(
        f"/orders/{fields_to_update.id}/", data=json.dumps(fields_to_update.dict())
    )


def delete_order(api_client, order_id):
    api_client.delete(f"/orders/{order_id}/")
