from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as pg_UUID  # noqa
from sqlalchemy.orm import relationship

from .base import AbstractModelForTime
from .quiz_answer import QuizAnswer
from .quiz_question import QuizQuestion
from .telegram_user import TelegramUser
from .user_quizes import UserQuiz


class TakenAnswer(AbstractModelForTime):
    """Модель полученного ответа от пользователя.

    Модель содержит:
    - quiz_id: идентификатор квиза, к которому относится ответ пользователя;
    - question_id: идентификатор вопроса,
            к которому относится ответ пользователя;
    - answer_id: идентификатор ответа, к которому относится ответ пользователя;
    - user_id: идентификатор пользователя, который ответил на вопрос;
    - created_at: дата и время создания;
    - edited_at: дата и время редактирования.
    """

    __tablename__ = "takenanswers"

    user_quiz_id = Column(pg_UUID, ForeignKey('userquizes.unique_id'))
    question_id = Column(pg_UUID, ForeignKey('quizquestions.unique_id'))
    answer_id = Column(pg_UUID, ForeignKey('quizanswers.unique_id'))
    tg_user_id = Column(pg_UUID, ForeignKey('telegramusers.unique_id'))
    quiz = relationship(UserQuiz)
    question = relationship(QuizQuestion)
    answer = relationship(QuizAnswer)
    user = relationship(TelegramUser)

    def __repr__(self) -> str:
        return (
            f'{self.user_quiz_id=}; {self.question_id=};'
            f' {self.answer_id=}; {self.tg_user_id=}; '
            f'{super().__repr__()}'
        )
