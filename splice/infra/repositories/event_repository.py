from sqlalchemy.future import select
from sqlalchemy.orm import Session

from splice.core.entities.event import Event


class EventRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def save(self, event: Event) -> Event:
        print("save event ",event.dict());
        from uuid import uuid4
        event.id = str(uuid4())
        return event
        # async with self.db_session() as session:
        #     if event.id is None:
        #         # Inserir novo
        #         session.add(event)
        #     else:
        #         # Atualizar existente
        #         await session.merge(event)
        #     await session.commit()
        #     return event

    async def get_by_id(self, event_id: int) -> Event | None:
        print("get event "+event_id);
        event = Event("","","","","","","","","")
        return event
        # async with self.db_session() as session:
        #     statement = select(Event).filter_by(id=event_id)
        #     return (await session.execute(statement)).scalar_one_or_none()

    async def delete(self, event_id: int) -> None:
        print("delete event "+event_id);
        # async with self.db_session() as session:
        #     statement = select(Event).filter_by(id=event_id)
        #     event = (await session.execute(statement)).scalar_one_or_none()
        # if event:
        #     await session.delete(event)
        #     await session.commit()
