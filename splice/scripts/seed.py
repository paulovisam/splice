import os
import random
from datetime import datetime

from splice.core.use_cases.user import CreateUser
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
from splice.infra.repositories.order_repository import Order, OrderRepository
from splice.core.models.order import PaymentType
from splice.infra.repositories.product_repository import (
    Product,
    ProductRepository,
)
from splice.infra.repositories.subproduct_repository import (
    Subproduct,
    SubproductRepository,
)
from splice.infra.repositories.user_repository import User, UserRepository
import bcrypt
from uuid import UUID, uuid4

# import uuid
bcrypt.__about__ = bcrypt


async def generate_random_orders(user_id, establishment_id, num_orders=5):
    orders = []
    for _ in range(num_orders):
        order = Order(
            id=uuid4(),
            value=round(
                random.uniform(10.0, 200.0), 2
            ),  # Valor aleatório entre 10 e 200
            payment_method=random.choice(
                [payment_type.value for payment_type in PaymentType]
            ),
            has_paid=random.choice([True, False]),
            user_id=user_id,
            establishment_id=establishment_id,
        )
        orders.append(order)
    return orders


async def seed():
    # Drop tables
    os.system('task alembic_down_up')
    mongo_session.drop_collection('messages')
    async with pg_session() as session:

        # Prepare data
        paulo = User(
            id=UUID('9301da1f-8e69-4312-91dc-ba54b5f47174'),
            first_name='Paulo',
            last_name='Mendonca',
            phone='010101',
            email='paulo@email.com',
            username='paulo',
            password='secret',
            photo='my_photo',
        )
        alice = User(
            id=UUID('2aeefff0-3ac2-4213-9e06-1cba6e4e226f'),
            first_name='Alice',
            last_name='Silva',
            phone='020202',
            email='alice@email.com',
            username='alice',
            password='secret',
            photo='my_photo',
        )

        establishment = Establishment(
            id=UUID('8b434f82-9701-4ac4-82ea-ebd68c2692f2'),
            name='Restaurante do Paulo',
            description='sabor e tradição',
            photo='Rua 1, 123',
            user_id=paulo.id,
        )

        group = Group(name='Grupo de Devs', photo='link_photo')

        # Gera pedidos aleatórios
        random_orders = await generate_random_orders(
            alice.id, establishment.id, num_orders=10
        )

        # Postgres
        user_repo = UserRepository(session)
        use_case = CreateUser(user_repo=user_repo)
        await use_case.execute(**alice.model_dump())
        await use_case.execute(**paulo.model_dump())

        paulo = await user_repo.get_by_username(paulo.username)

        establishment_repo = EstablishmentRepository(session)
        await establishment_repo.save(establishment)

        group_repo = GroupRepository(session)
        await group_repo.save(group)

        order_repo = OrderRepository(session)
        for order in random_orders:
            await order_repo.save(order)

        product = Product(
            id=UUID('123e4567-e89b-12d3-a456-426614174000'),
            name='Pizza de calabresa',
            description='Pizza de calabresa com queijo',
            value=10.00,
            establishment_id=establishment.id,
        )

        product.orders.append(random_orders[0])

        subproduct = Subproduct(
            id=UUID('a8e63f9f-b83c-4644-8bc6-f1d0fd229146'),
            name='Pizza de calabresa',
            description='Pizza de calabresa com queijo',
            value=10.00,
            product_id=product.id,
        )

        product_repo = ProductRepository(session)
        await product_repo.save(product)

        subproduct_repo = SubproductRepository(session)
        await subproduct_repo.save(subproduct)

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
