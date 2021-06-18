from app.models.user import User, db


class UsersRepository:
    @classmethod
    def get_user_by_id(self, id) -> User:
        user = User.query.filter_by(id=id).first()
        return user

    @classmethod
    def get_all_users(self):
        users = User.query.all()
        return users

    @classmethod
    def create_user(self, arguments):
        user = User(**arguments)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def destroy_user(self, id):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        return user
