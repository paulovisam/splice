from sqlalchemy import select

from splice.core.entities.user import User


def test_create_user(session, mock_db_time):
    user_payload = {
        "first_name": "Alice",
        "last_name": "Silva",
        "phone": "00000000000",
        "email": "teste@test",
        "username": "alice",
        "password": "secret",
        "photo": "url_photo",
    }
    with mock_db_time(model=User) as time:
        new_user = User(**user_payload)
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == "alice"))

    assert user.dict() == {
        "id": 1,
        **user_payload,
        "created_at": time,
        "updated_at": None,
    }
    assert user.username == "alice"
    assert user.created_at == time
