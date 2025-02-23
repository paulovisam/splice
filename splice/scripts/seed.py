import os
import random

from splice.core.models.group import Group
from splice.core.models.restaurant import Restaurant
from splice.core.models.user import User
from splice.infra.database import pg_session, mongo_session
from splice.infra.repositories.group_repository import GroupRepository
from splice.infra.repositories.message_repository import (
    MessageCreateSchema,
    MessageRepository,
)
from splice.infra.repositories.restaurant_repository import (
    RestaurantRepository,
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

    restaurant = Restaurant(
            name='Restaurante do Paulo',
            description='Restaurante do Paulo',
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

    restaurant_repo = RestaurantRepository(pg_session)
    await restaurant_repo.save(restaurant)

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
