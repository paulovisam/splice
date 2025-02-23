import os
import random

from splice.core.models.group import Group
from splice.core.models.establishment import establishment
from splice.core.models.user import User
from splice.infra.database import mongo_session, pg_session
from splice.infra.repositories.group_repository import GroupRepository
from splice.infra.repositories.message_repository import (
    MessageCreateSchema,
    MessageRepository,
)
from splice.infra.repositories.establishment_repository import (
    establishmentRepository,
)
from splice.infra.repositories.user_repository import UserRepository


async def seed():
    # Drop tables
    os.system('task alembic_down_up')
    mongo_session.drop_collection('messages')

    # Prepare data
    paulo = User(
                first_name='Paulo',
                last_name='Mendonca',
                phone='010101',
                email='paulo@email.com',
                username='paulo',
                password='123',
                photo='my_photo',
            )
    alice = User(
                first_name='Alice',
                last_name='Silva',
                phone='020202',
                email='alice@email.com',
                username='alice',
                password='123',
                photo='my_photo',
            )

    establishment = establishment(
            name='establishmente do Paulo',
            description='establishmente do Paulo',
            photo='Rua 1, 123',
            user_id=paulo.id,
        )

    group = Group(
        name='Grupo do Paulo',
        photo='link_photo',
    )

    # Postgres
    user_repo = UserRepository(pg_session)
    await user_repo.save(paulo)
    await user_repo.save(alice)
    paulo = await user_repo.get_by_username(paulo.username)

    establishment_repo = establishmentRepository(pg_session)
    await establishment_repo.save(establishment)

    group_repo = GroupRepository(pg_session)
    await group_repo.save(group)

    # Mongo
    message_repo = MessageRepository(mongo_session=mongo_session)
    for _ in range(10):
        await message_repo.save(
            MessageCreateSchema(
                content=f'Mensagem {random.randint(1, 100)}',
                sender=paulo.username,
                receiver=alice.username,
            )
        )


if __name__ == '__main__':
    import asyncio

    asyncio.run(seed())
