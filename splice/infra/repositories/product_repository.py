from sqlalchemy.future import select
from sqlalchemy.orm import Session

from splice.core.models.product import Product


class ProductRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def save(self, product: Product) -> Product:
        await self.db_session.merge(product)
        await self.db_session.commit()
        return product

    async def get_by_id(self, product_id: int) -> Product | None:
        statement = select(Product).filter_by(id=product_id)
        return (await self.db_session.execute(statement)).scalar_one_or_none()

    async def delete(self, product_id: int) -> None:
        statement = select(Product).filter_by(id=product_id)
        product = (
            await self.db_session.execute(statement)
        ).scalar_one_or_none()
        if product:
            await self.db_session.delete(product)
            await self.db_session.commit()
