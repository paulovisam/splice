from datetime import datetime
from typing import List, Optional

from bson import ObjectId
from pymongo import errors
from pymongo.database import Database

from splice.interface.schemas.message_schema import (
    MessageCreateSchema,
    MessageResponseSchema,
)


class MessageRepository:
    def __init__(self, mongo_session: Database):
        self.collection = mongo_session.get_collection('messages')

    async def save(self, data: MessageCreateSchema) -> str:
        try:
            result = await self.collection.insert_one(data.model_dump())
            return str(result.inserted_id)
        except (ValueError, TypeError) as e:
            raise e
        except errors.PyMongoError as e:
            raise Exception(f'Erro ao inserir mensagem: {e}')

    async def get_by_id(
        self, message_id: str
    ) -> Optional[MessageResponseSchema]:
        """
        Busca uma mensagem pelo ID.
        Retorna um modelo Pydantic MessageModel ou None se não encontrada.
        """
        try:
            message = await self.collection.find_one({
                '_id': ObjectId(message_id)
            })
            if message:
                return MessageResponseSchema(**message)
            return None
        except errors.PyMongoError as e:
            raise Exception(
                f'Erro ao buscar mensagem com ID {message_id}: {e}'
            )

    async def get_by_sender_id(
        self, sender_username: str
    ) -> List[MessageResponseSchema]:
        """
        Busca mensagens enviadas por um determinado usuário.
        """
        try:
            messages = self.collection.find({'sender': sender_username})
            return [
                MessageResponseSchema(**{**msg, 'id': str(msg['_id'])})
                async for msg in messages
            ]
        except errors.PyMongoError as e:
            raise Exception(
                f'Erro ao buscar mensagens enviadas por {sender_username}: {e}'
            )

    async def get_by_receiver_id(
        self, receiver_username: str
    ) -> List[MessageResponseSchema]:
        """
        Busca mensagens recebidas por um determinado usuário.
        """
        try:
            messages = await self.collection.find({
                'receiver': receiver_username
            })
            return [
                MessageResponseSchema(**{**msg, 'id': str(msg['_id'])})
                for msg in messages
            ]
        except errors.PyMongoError as e:
            raise Exception(
                f'Erro ao buscar mensagens recebidas por {receiver_username}: {e}'
            )

    async def update(self, message_id: str, new_content: str) -> bool:
        """
        Atualiza o conteúdo de uma mensagem existente, dado o seu ID.
        Retorna True se a atualização for bem-sucedida, False caso contrário.
        """
        try:
            if not message_id or not new_content:
                raise ValueError(
                    'Message ID and new content are required for update.'
                )

            update_result = await self.collection.update_one(
                {'_id': message_id},
                {
                    '$set': {
                        'content': new_content,
                        'timestamp': datetime.now(),
                    }
                },
            )
            return (
                update_result.modified_count > 0
            )  # Retorna True se a mensagem foi modificada

        except errors.PyMongoError as e:
            raise Exception(
                f'Erro ao atualizar mensagem com ID {message_id}: {e}'
            )
        except ValueError as e:
            raise e

    async def delete(self, message_id: str) -> bool:
        """
        Exclui uma mensagem com base no seu ID.
        Retorna True se a exclusão for bem-sucedida, False caso contrário.
        """
        try:
            if not message_id:
                raise ValueError('Message ID is required for delete.')

            delete_result = await self.collection.delete_one({
                '_id': message_id
            })
            return (
                delete_result.deleted_count > 0
            )  # Retorna True se a mensagem foi deletada

        except errors.PyMongoError as e:
            raise Exception(
                f'Erro ao excluir mensagem com ID {message_id}: {e}'
            )
        except ValueError as e:
            raise e
