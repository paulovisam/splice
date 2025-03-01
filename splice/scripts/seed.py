import os
import random

from splice.infra.database import mongo_session, pg_session
from splice.infra.repositories.establishment_repository import (
    Establishment,
    EstablishmentRepository,
)
from splice.infra.repositories.group_repository import Group, GroupRepository
from splice.infra.repositories.message_repository import (
    MessageCreateSchema,
    MessageRepository,
)
from splice.infra.repositories.user_repository import User, UserRepository
from splice.infra.repositories.order_repository import Order, OrderRepository
from splice.infra.repositories.product_repository import (
    Product,
    ProductRepository,
)


async def seed():
    # Drop tables
    os.system('task alembic_down_up')
    mongo_session.drop_collection('messages')

    # Prepare data
    paulo = User(
        id='9301da1f-8e69-4312-91dc-ba54b5f47174',
        first_name='Paulo',
        last_name='Mendonca',
        phone='010101',
        email='paulo@email.com',
        username='paulo',
        password='123',
        photo='my_photo',
    )
    alice = User(
        id='2aeefff0-3ac2-4213-9e06-1cba6e4e226f',
        first_name='Alice',
        last_name='Silva',
        phone='020202',
        email='alice@email.com',
        username='alice',
        password='123',
        photo='my_photo',
    )

    establishment = Establishment(
        id='8b434f82-9701-4ac4-82ea-ebd68c2692f2',
        name='Restaurante do Paulo',
        description='sabor e tradição',
        photo='Rua 1, 123',
        user_id=paulo.id,
    )

    group = Group(name='Grupo de Devs', photo='link_photo')

    order = Order(
        id='052908b7-a9a0-48a7-a518-77c9316f6416',
        value=157.30,
        payment_method="PIX",
        has_paid=True,
        user_id=paulo.id,
        establishment_id=establishment.id,
    )

    product = Product(
        id='123e4567-e89b-12d3-a456-426614174000',
        name='Pizza de calabresa',
        description='Pizza de calabresa com queijo',
        value=10.00,
        establishment_id=establishment.id,
    )

    product.orders.append(order)

    async with pg_session() as session:

        # Postgres
        user_repo = UserRepository(session)
        await user_repo.save(paulo)
        await user_repo.save(alice)
        paulo = await user_repo.get_by_username(paulo.username)

        establishment_repo = EstablishmentRepository(session)
        await establishment_repo.save(establishment)

        group_repo = GroupRepository(session)
        await group_repo.save(group)

        order_repo = OrderRepository(session)
        await order_repo.save(order)
        print(order.products)

        product_repo = ProductRepository(session)
        await product_repo.save(product)

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
