from fastapi import APIRouter, Depends

from src.products.models import ProductHypermedia, ProductsHypermedia
from src.products.repositories import InMemoryProductsRepository, ProductsRepository

router = APIRouter()


@router.get("/products/", response_model=ProductsHypermedia)
def products(
    repo: ProductsRepository = Depends(InMemoryProductsRepository),
) -> ProductsHypermedia:
    products = [
        ProductHypermedia.parse_obj(
            {**product.dict(), "_links": {"self": f"/products/{product.id}/"}}
        )
        for product in repo.get_products()
    ]
    return ProductsHypermedia(products=products, _links={"self": "/products/"})


@router.get("/products/{product_id}", response_model=ProductHypermedia)
def product(
    product_id: str, repo: ProductsRepository = Depends(InMemoryProductsRepository)
) -> ProductHypermedia:
    product = repo.get_product(product_id)
    return ProductHypermedia.parse_obj(
        {
            **product.dict(),
            "_links": {"self": f"/products/{product_id}/", "products": "/products/"},
        }
    )
