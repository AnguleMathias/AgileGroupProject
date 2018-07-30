from ..app import session, store
from app.users import User
from datetime import datetime


def sign_up():
    username = input("SIGN UP: \n\tEnter your username: ")
    password = input("\tEnter your password: ")
    user = {'username': username, "password": password}
    User.save(user)


def login():
    username = input("LOGIN: \n\tEnter your username: ")
    password = input("\tEnter your password: ")

    user = store.users.get(username)
    if user and user.password == password:
        session['user'] = user
        user.isAuthenticated = True
        user.lastLoggedInAt = datetime.now()

    else:
        assert 0, 'Invalid username or password'


def logout():
    user = session.get('user')
    if user:
        print('bye bye {}'.format(user.username))
        session.pop('user')
