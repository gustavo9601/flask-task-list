from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Sequence

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    def __init__(self, name, password):
        self.name = name
        self.password = password

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    password = Column(String)


