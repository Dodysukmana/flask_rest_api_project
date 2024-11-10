 # app/controllers.py
from .models import db, User

def get_users():
    return User.query.all()

def create_user(data):
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return new_user
