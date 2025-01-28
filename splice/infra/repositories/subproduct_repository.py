from sqlalchemy.future import select
from sqlalchemy.orm import Session

from splice.core.entities.subproduct import Subproduct


class SubproductRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def save(self, subproduct: Subproduct) -> Subproduct:
        print("save subproduct ",subproduct.dict())
        from uuid import uuid4
        subproduct.id = str(uuid4())
        return subproduct;
        # async with self.db_session() as session:
        #     if subproduct.id is None:
        #         # Inserir novo
        #         session.add(subproduct)
        #     else:
        #         # Atualizar existente
        #         await session.merge(subproduct)
        #     await session.commit()
        #     return subproduct

    async def get_by_id(self, subproduct_id: int) -> Subproduct | None:
        print("get subproduct "+subproduct_id)
        subproduct = Subproduct("","name",1.3,10,"description")
        return subproduct
        # async with self.db_session() as session:
        #     statement = select(Subproduct).filter_by(id=subproduct_id)
        #     return (await session.execute(statement)).scalar_one_or_none()

    async def delete(self, subproduct_id: int) -> None:
        print("delete subproduct "+subproduct_id)
        # async with self.db_session() as session:
        #     statement = select(Subproduct).filter_by(id=subproduct_id)
        #     subproduct = (await session.execute(statement)).scalar_one_or_none()
        # if subproduct:
        #     await session.delete(subproduct)
        #     await session.commit()
