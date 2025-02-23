from sqlalchemy.future import select
from sqlalchemy.orm import Session

from splice.core.models.event import Event


class EventRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def save(self, event: Event) -> Event:
        if event.id is None:
            # Inserir novo
            self.db_session.add(event)
        else:
            # Atualizar existente
            await self.db_session.merge(event)
        await self.db_session.commit()
        return event

    async def get_by_id(self, event_id: int) -> Event | None:
        statement = select(Event).filter_by(id=event_id)
        return (await self.db_session.execute(statement)).scalar_one_or_none()

    async def delete(self, event_id: int) -> None:
        statement = select(Event).filter_by(id=event_id)
        event = (await self.db_session.execute(statement)).scalar_one_or_none()
        if event:
            await self.db_session.delete(event)
            await self.db_session.commit()
