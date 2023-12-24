from app.sql_app import models
from app.sql_app.crud.answer import AnswerCRUD
from app.sql_app.crud.message import MessageCRUD
from app.sql_app.crud.message_content import MessageContentCRUD
from app.sql_app.crud.question import QuestionCRUD
from app.sql_app.crud.log import LogCRUD
from app.sql_app.database import session


AnswerDB = AnswerCRUD(session, models.Answer)
MessageDB = MessageCRUD(session, models.Message)
MessageContentDB = MessageContentCRUD(session, models.MessageContent)
QuestionDB = QuestionCRUD(session, models.Question)
LogDB = LogCRUD(session, models.Log)


MessageDB.link_db(MessageContentDB)
QuestionDB.link_db(AnswerDB)
AnswerDB.link_db(QuestionDB)
