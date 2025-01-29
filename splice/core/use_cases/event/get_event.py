from splice.infra.repositories.event_repository import EventRepository


class GetEvent:
    def __init__(self, event_repo: EventRepository):
        self.event_repo = event_repo

    async def get_by_id(self, event_id: int):
        return await self.event_repo.get_by_id(event_id)
