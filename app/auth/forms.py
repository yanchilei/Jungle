# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
	username = StringField("用户名", validators=[Required(), Length(1, 32)])
	password = PasswordField("密码", validators=[Required()])
	remember_me = BooleanField("记住我")
	submit = SubmitField("登录")

class RegistrationForm(Form):
	username = StringField('用户名', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, '用户名只能由字母，数字，下划线和点组成')])
	password = PasswordField('密码', validators=[Required(), EqualTo('password2', message='两次密码必须匹配。')])
	password2 = PasswordField('再次确认', validators=[Required()])
	submit = SubmitField('注册')

	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('用户名已被使用。')