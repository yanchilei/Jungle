# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required, Length
from flask_pagedown.fields import PageDownField

class EditProfileForm(Form):
	name = StringField('真实姓名', validators=[Length(0, 64)])
	location = StringField('所在地', validators=[Length(0, 64)])
	about_me = TextAreaField('关于我')
	submit = SubmitField('提交')

class PostForm(Form):
	body = PageDownField("有什么新鲜事？", validators=[Required()])
	submit = SubmitField('提交')

class CommentForm(Form):
    body = StringField('', validators=[Required()])
    submit = SubmitField('提交评论')