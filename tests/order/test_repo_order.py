from unittest.mock import AsyncMock, MagicMock

from splice.infra.repositories.order_repository import (
    Order,
    OrderRepository,
)


async def test_create_order(session, user, establishment):
    order_repo = OrderRepository(session)
    result = await order_repo.save(
        Order(
            value=155.87,
            payment_method='money',
            has_paid=False,
            user_id=user.id,
            establishment_id=establishment.id,
        )
    )
    assert result.user_id == user.id

    # Returns Order object when valid order_id is provided


async def test_get_by_id_returns_order_for_valid_id(
    session, user, establishment, order
):
    session.execute = AsyncMock()
    repo = OrderRepository(db_session=session)

    mock_order = order

    session.execute.return_value.scalar_one_or_none = MagicMock()
    session.execute.return_value.scalar_one_or_none.return_value = mock_order

    result = await repo.get_by_id(mock_order.id)

    assert result == mock_order
    session.execute.assert_called_once()


# async def test_get_by_id_raises_type_error_for_invalid_id_type(session):
#     repo = OrderRepository(db_session=session)

#     with pytest.raises(StatementError):
#         await repo.get_by_id('invalid_id')

#     session.execute.assert_not_called()


async def test_delete_existing_order(session, order):
    # Arrange
    repo = OrderRepository(db_session=session)
    session.execute = AsyncMock()
    session.delete = AsyncMock()
    session.commit = AsyncMock()

    session.execute.return_value.scalar_one_or_none = MagicMock()
    session.execute.return_value.scalar_one_or_none.return_value = order

    # Act
    await repo.delete(order.id)

    # Assert
    session.delete.assert_called_once_with(order)
    session.commit.assert_called_once()
