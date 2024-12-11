from splice.core.entities.messages import Message
from splice.core.entities.user import User
from splice.infra.database import get_session
from splice.infra.repositories.message_repository import MessageRepository
from splice.infra.repositories.user_repository import UserRepository


async def seed():
    async with get_session() as session:
        user_repo = UserRepository(session)
        message_repo = MessageRepository(session)

        paulo = await user_repo.save(
            User(
                first_name='Paulo',
                last_name='Teste',
                phone='010101',
                email='paulo@email.com',
                username='paulo',
                password='123',
                photo='my_photo',
            )
        )
        alice = await user_repo.save(
            User(
                first_name='Alice',
                last_name='Teste',
                phone='020202',
                email='alice@email.com',
                username='alice',
                password='123',
                photo='my_photo',
            )
        )

        await message_repo.save(
            Message(
                content='Olá, Alice!',
                sender=paulo.username,
                receiver=alice.username,
            )
        )


if __name__ == '__main__':
    import asyncio

    asyncio.run(seed())
