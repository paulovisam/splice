from unittest.mock import MagicMock

import pytest
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from splice.infra.repositories.establishment_repository import (
    Establishment,
    EstablishmentRepository,
)


async def test_save_new_establishment_success(session, user):
    repo = EstablishmentRepository(db_session=session)

    establishment = Establishment(
        name='Restaurante do Zeca',
        description='uma descrição',
        photo='url_photo',
        user_id=user.id,
    )
    await repo.save(establishment)

    res = await session.scalar(
        select(Establishment).where(
            Establishment.name == 'Restaurante do Zeca'
        )
    )
    assert res
    assert res == establishment


async def test_save_establishment_missing_required_fields(session, user):
    session.add = MagicMock()
    repo = EstablishmentRepository(db_session=session)

    establishment = Establishment(
        description='uma descrição',
        photo='url_photo',
        user_id=user.id,
    )
    with pytest.raises(IntegrityError):
        await repo.save(establishment)

    session.add.assert_not_called()


async def test_get_establishment_by_id(session, establishment):
    repo = EstablishmentRepository(db_session=session)

    result = await repo.get_by_id(establishment.id)

    assert isinstance(result, Establishment)
    assert result.id == establishment.id


async def test_get_establishment_by_id_invalid(session):
    repo = EstablishmentRepository(db_session=session)

    result = await repo.get_by_id(0)

    assert result is None


async def test_get_establishment_by_user_id(session, establishment, user):
    repo = EstablishmentRepository(db_session=session)
    result = await repo.get_by_user_id(user.id)
    assert isinstance(result, Establishment)
    assert result.id == establishment.id


async def test_get_establishment_by_invalid_user_id(session, establishment):
    repo = EstablishmentRepository(db_session=session)
    result = await repo.get_by_user_id(0)
    assert result is None


async def test_delete_establishment(session, establishment):
    repo = EstablishmentRepository(db_session=session)
    await repo.delete(establishment.id)

    result = await session.scalar(
        select(Establishment).where(Establishment.id == establishment.id)
    )
    assert result is None
