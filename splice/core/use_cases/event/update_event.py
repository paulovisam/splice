from splice.infra.repositories.event_repository import EventRepository


class UpdateEvent:
    def __init__(self, event_repo: EventRepository):
        self.event_repo = event_repo

    async def execute(self, event_id: str, **kwargs):
        # Obtém  pelo ID
        event = await self.event_repo.get_by_id(event_id)

        # Atualiza somente os atributos fornecidos
        for key, value in kwargs.items():
            if value is not None and hasattr(event, key):
                setattr(event, key, value)

        return await self.event_repo.save(event)
