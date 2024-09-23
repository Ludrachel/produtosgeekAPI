from fastapi import APIRouter, status, HTTPException # type: ignore
from models.product import Product, ProductCreate, ProductUpdate
from services.product_service import ProductService

router = APIRouter()

product_service = ProductService()

@router.get("/", response_model=list[Product])
def get_products():
    return product_service.get_products()

@router.post("/", response_model=Product)
def create_product(product: ProductCreate):
    db_product = Product.model_validate(product)
    return product_service.save_product(db_product)

@router.get("/{product_id}", response_model=Product)
def get_one_product(product_id: str):
    return product_service.get_one_product(id=product_id)

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: str, product: ProductUpdate):
    db_product = Product.model_validate(product)
    return product_service.update_product(id=product_id, product_update=product)

@router.patch("/{product_id}/decrease", response_model=Product)
def decrease_quantity(product_id: str):
    try:
        result = product_service.reduce_stocke(product_id)
        return result
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ação inválida"
        )
    
@router.patch("/{product_id}/increase", response_model=Product)
def increase_stock(product_id: str):
    try:
        result = product_service.increase_stock(product_id)
        return result
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ação inválida"
        )