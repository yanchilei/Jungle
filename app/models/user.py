#coding=utf-8
from .. import db
from dateime import datetime
from ..models import User

class Follow(db.Model):
    __tablename__ = 'follows'
    follower_id = db.Column(db.Integer, db.foreignKey('user.id'), primary_key = True)
    followed_id = db.Column(db.Integer, db.foreignKey('user.id'), primary_key = True)
    timestamp = db.Column(db.Datetime, default = datetime.utcnow)
