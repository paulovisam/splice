from uuid import UUID

import pytest
from sqlalchemy import select

from splice.core.entities.user import User
from splice.infra.database import get_db


# Successfully creates and yields a database session
async def test_successful_session_creation(mocker):
    mock_session = mocker.patch(
        'splice.infra.database.async_session', autospec=True
    )
    async with get_db() as session:
        assert session == mock_session.return_value.__aenter__.return_value


# Handles exceptions during session creation
async def test_exception_handling_during_session_creation(mocker):
    mock_session = mocker.patch(
        'splice.infra.database.async_session', autospec=True
    )
    mock_session.side_effect = Exception('Session creation failed')
    with pytest.raises(Exception, match='Session creation failed'):
        async with get_db() as session:
            pass


async def test_create_user(session, mock_db_time):
    user_payload = {
        'first_name': 'Alice',
        'last_name': 'Silva',
        'phone': '00000000000',
        'email': 'teste@test',
        'username': 'alice',
        'password': 'secret',
        'photo': 'url_photo',
    }
    with mock_db_time(model=User) as time:
        new_user = User(**user_payload)
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert user.dict() == {
        'id': UUID('188581a2-2903-49fb-87c3-a30a4598b760'),
        **user_payload,
        'created_at': time,
        'updated_at': None,
    }
    assert user.username == 'alice'
    assert user.created_at == time
