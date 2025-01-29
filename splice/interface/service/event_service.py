# app/api/services/event_service.py
from splice.core.use_cases.event import CreateEvent, DeleteEvent, GetEvent, UpdateEvent
from splice.infra.repositories.event_repository import EventRepository


class EventService:
    def __init__(self, repo: EventRepository):
        self.repo = repo

    async def create(
        self,
        id_establishment,
        type_establishment,
        title,
        photo,
        description,
        link,
        type_event,
        entry_hour,
        ending_time,

    ):
        use_case = CreateEvent(self.repo)
        return await use_case.execute(
            id_establishment=id_establishment,
            type_establishment=type_establishment,
            title=title,
            photo=photo,
            description=description,
            link=link,
            type_event=type_event,
            entry_hour=entry_hour,
            ending_time=ending_time
        )
    async def get_by_id(self, event_id: int):
        use_case = GetEvent(self.repo)
        return await use_case.get_by_id(event_id)

    async def update(self, event_id: int, **kwargs):
        use_case = UpdateEvent(self.repo)
        return await use_case.execute(event_id=event_id, **kwargs)

    async def delete(self, event_id: int):
        use_case = DeleteEvent(self.repo)
        return await use_case.execute(event_id)
