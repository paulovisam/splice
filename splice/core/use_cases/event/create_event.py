from splice.core.models.event import Event
from splice.infra.repositories.event_repository import EventRepository


class CreateEvent:
    def __init__(self, event_repo: EventRepository):
        self.event_repo = event_repo

    async def execute(
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
        new_event = Event(
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
        return await self.event_repo.save(new_event)
