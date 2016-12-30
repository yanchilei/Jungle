from flask import g
from . import api
from ..models import AnonymousUser, User
from flask_httpauth import HTTPBasicAuth
from .errors import forbidden
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username_or_token, password):
    if username_or_token == '':
        g.current_user = AnonymousUser()
        return True
    if password == '':
        g.current_user = User.verify_auth_token(username_or_token)
        g.token_used = True
        return g.current_user is not None
    user = User.query.filter_by(username=username_or_token).first()
    if not user:
        g.current_user = user
        g.token_used = False
        return user.verify_password(password)

@auth.error_handler
def auth_error():
    return unauthorized('Invalid credentials.')

@api.route('/posts/')
@auth.login_required
def get_posts():
    pass

@api.before_request
@auth.login_required
def before_request():
    if not g.current_user.is_anonymous:
        return forbidden('Unconfirmed account.')