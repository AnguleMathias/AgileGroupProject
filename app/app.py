from app import session
from auth.func import render_homepage, render_indexViewFor


def main():

    render_homepage()

    user = session['user']
    render_indexViewFor(user)
