from sqlalchemy import Boolean, Column, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID as pg_UUID  # noqa
from sqlalchemy.orm import relationship

from backend.core.config import settings
from backend.models.base import AbstractModelForTime
from backend.models.user import User


class Quiz(AbstractModelForTime):
    """Модель квиза.

    - title: Название квиза;
    - description: Описание квиза;
    - active: Активен ли квиз
    - edited_by: Кто изменил квиз;
    - created_by: Кто создал квиз;
    - created_at: Дата и время создания;
    - edited_at: Дата и время редактирования.
    """

    title = Column(String(settings.quiz_name_length), unique=True)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=False)
    edited_by = Column(pg_UUID, ForeignKey('users.unique_id'), nullable=True)
    created_by = Column(
        pg_UUID,
        ForeignKey('users.unique_id'),
    )
    created = relationship(
        User,
        foreign_keys=[created_by],
    )
    edited = relationship(
        User,
        foreign_keys=[edited_by],
    )

    def __repr__(self) -> str:
        return (
            f'{self.title=}; {self.description[:30]=}; {self.active=}; '
            f'{self.edited_by=}; {self.created=}; {super().__repr__()}'
        )
