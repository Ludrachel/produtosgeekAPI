from sqlmodel import Session, select                   # type: ignore
from models.product import Product, ProductCreate
from database.db import get_engine

class ProductService():
    def __init__(self):
        engine = get_engine()
        self.session = Session(engine)
    
    def get_one_product(self, id: str):
        sttm = select(Product).where(Product.id == id)
        return self.session.exec(sttm).one()


    def get_products(self):
        sttm = select(Product)
        return self.session.exec(sttm).all()
    
    def save_product(self, product: Product):
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product
    
    def update_product(self, id: str, product_update: Product):
        sttm = select(Product).where(Product.id == id)
        product = self.session.exec(sttm).one()

        product.name = product_update.name
        product.description = product_update.description
        product.category = product_update.category
        product.franchise = product_update.franchise
        product.price = product_update.price

        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product

    def reduce_stocke(self, id: str):
        sttm = select(Product).where(Product.id == id)
        product = self.session.exec(sttm).one()

        product.decrease_quantity()
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product

    def increase_stock(self, id: str):
        sttm = select(Product).where(Product.id == id)
        product = self.session.exec(sttm).one()

        product.increase_quantity()
        self.session.add(product)
        self.session.commit()
        self.session.refresh(product)
        return product 