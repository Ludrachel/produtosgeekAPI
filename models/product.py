from sqlmodel import Field, SQLModel   # type: ignore
from ulid import ulid                  # type: ignore

class ProductBase(SQLModel):
    name: str = Field(nullable=False)
    description: str | None = None
    price: float | None = None
    quantity: int = Field(default=0)
    category: str | None = None
    franchise: str | None = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass


class Product(ProductBase, table=True):
    id: str = Field(default=ulid(), primary_key=True)

    def decrease_quantity(self):
        if self.quantity < 0:
            raise Exception()
        self.quantity -= 1
    
    def increase_quantity(self):
        self.quantity += 1