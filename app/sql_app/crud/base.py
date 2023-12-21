"""
Unsafe CRUD operations. Do not use this class directly.
"""
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


class BaseCRUD:
    """
    A base class for performing unsafe CRUD operations on a database.

    Args:
        async_session (async_sessionmaker[AsyncSession]): an async sessionmaker for the database
        model_class (Model): the SQLAlchemy model class to be used with this CRUD
    """

    def __init__(self, async_session: async_sessionmaker[AsyncSession], model_class):
        self.async_session = async_session
        self.model = model_class

    def link_db(self, db):
        """
        Link the database to this CRUD instance.

        Args:
            db (Any): the database object to link to
        """
        pass

    async def _create(self, _obj):
        """
        Create a new record in the database.

        Args:
            _obj (Model): the model object to create

        Returns:
            Model: the created model object
        """
        async with self.async_session() as session:
            session.add(_obj)
            await session.commit()
            return _obj

    # noinspection PyTypeChecker
    async def _get_one(self, key: str, value: Any, options=None):
        """
        Retrieve a single record from the database based on a key-value pair.

        Args:
            key (str): the key of the field to filter by
            value (Any): the value of the field to filter by
            options (list[orm.Load]): optional SQLAlchemy options to apply to the query

        Returns:
            Any: the retrieved record, or None if no record was found
        """
        async with self.async_session() as session:
            filter_condition = getattr(self.model, key) == value
            # noinspection PydanticTypeChecker
            query = select(self.model).filter(filter_condition)
            if options:
                query = query.options(*options)
            result = await session.execute(query)

            return result

    async def _get_all(self):
        """
        Retrieve all records from the database.

        Returns:
            list[Any]: a list of all records in the database
        """
        async with self.async_session() as session:
            statement = select(self.model).order_by(self.model.id)

            result = await session.execute(statement)

            return result.scalars()

    async def _update(self, _data):
        """
        Update an existing record in the database.

        Args:
            _data (Model): the model object containing the updated fields and values

        Returns:
            Model: the updated model object, or None if the record was not found
        """
        obj = await self._get_one('id', _data.id)

        obj = obj.scalars().one_or_none()

        if obj is None:
            return False

        for key, value in _data.__dict__.items():
            if key == 'id':
                continue
            setattr(obj, key, value)

        async with self.async_session() as session:
            session.add(obj)
            await session.commit()
            return obj

    async def _delete(self, _id: str):
        """
        Delete an existing record from the database.

        Args:
            _id (str): the ID of the record to delete

        Raises:
            ValueError: if the record was not found
        """
        record = await self._get_one('id', _id)
        if record is None:
            raise ValueError("Record not found")

        async with self.async_session() as session:
            await session.delete(record)
            await session.commit()

    async def _get_paginated(self, page: int, page_size: int, order: str):
        """
        Retrieve a paginated list of records from the database.

        Args:
            page (int): the page number (1-indexed)
            page_size (int): the number of items per page
            order (str): the field to order the results by

        Returns:
            list[Any]: a list of items from the specified page
        """
        async with self.async_session() as session:
            statement = select(self.model).order_by(getattr(self.model, order))
            statement = statement.limit(page_size).offset((page - 1) * page_size)

            result = await session.execute(statement)

            return result
