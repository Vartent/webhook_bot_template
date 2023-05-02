from database import session_scope
from tables import User


class AuthService:
    def add_user(self, user_id, user_name):
        with session_scope() as session:
            if not self.get_user(user_id):
                user = User(id=user_id, user_name=user_name)
                session.add(user)
                session.commit()

    def get_user(self, user_id):
        with session_scope() as session:
            user = (
                session
                .query(User)
                .filter(User.id == user_id)
                .first()
            )
        return user

    def delete_user(self):
        pass

    def update_user(self):
        pass
