from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'tasks'

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id

    id = Column(Integer, Sequence('task_id_seq'), primary_key=True)
    title = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

    # relacion con tabla usuario
    # task = relationship('User', back_populates='tasks')
