from fastapi import FastAPI

from src.orders.endpoints import router as orders_router
from src.products.endpoints import router as products_router


class APIBuilder:
    @staticmethod
    def build() -> FastAPI:
        api = FastAPI()
        api.include_router(orders_router)
        api.include_router(products_router)
        return api
