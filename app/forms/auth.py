import re

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, ValidationError
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, Length, Regexp

from ..models.user import User


class UserForm(FlaskForm):
    nickname = StringField(validators=[DataRequired(), Length(min=4, max=20),
                                       Regexp(r"^\w{4,20}$", flags=0, message=u"用户昵称最少4位最多20位字符，并且不能使用特殊字符！")])
    email = EmailField(validators=[DataRequired(), Length(min=6, max=50)])
    phone_number = StringField(validators=[DataRequired(), Length(min=11, max=11), Regexp(
        r"^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$", flags=0, message=u"无效的手机号码")])
    password = PasswordField(validators=[DataRequired(),
                                         Length(min=6, max=32),
                                         Regexp(r"^\w{6,32}$", flags=0, message=u"密码最少6位最多32位字符，并且不能使用特殊字符")])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u"该邮箱已被注册！")

    def validate_phone_number(self, field):
        if User.query.filter_by(phone_number=field.data):
            raise ValidationError(u"该手机号码已被注册！")


class LoginForm(FlaskForm):
    email_or_phone_number = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired(),
                                         Length(min=6, max=32),
                                         Regexp(r"^\w{6,32}$", flags=0, message=u"密码最少6位最多32位字符，并且不能使用特殊字符")])

    def validate_email_or_phone_number(self, field):
        res = re.search(
            r"^((\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)|((13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}))$",
            field.data)
        if not res:
            raise ValidationError("please input email or phone number!")
