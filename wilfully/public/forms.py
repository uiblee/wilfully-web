# -*- coding: utf-8 -*-
"""Public forms."""
from flask_wtf import Form
from wtforms import PasswordField, StringField, BooleanField, IntegerField, TextAreaField, RadioField, validators
from wtforms.validators import DataRequired

from wilfully.user.models import User


class SpouseRelationshipForm(Form):
    married = BooleanField('Are you married?', validators=[DataRequired()])
    spousename = StringField('Spouse name')

class ChildrenForm(Form):
    children = BooleanField('Do you have children?', validators=[DataRequired()])
    childrennumber = IntegerField('Children number', [validators.NumberRange(min=0, max=10)])
    childrenname = StringField('Children 1 name')

class FuneralBodyForm(Form):
    funeral = RadioField('Do you want to be buried or cremated?', choices=[('value','Buried'),('value_two','Cremated'), ('value_three','Other')])
    buriallocation = StringField('Burial location')
    burialdetails = TextAreaField('Burial details')
    childrenname = StringField('Children 1 name')

class LoginForm(Form):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        self.user = User.query.filter_by(username=self.username.data).first()
        if not self.user:
            self.username.errors.append('Unknown username')
            return False

        if not self.user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        if not self.user.active:
            self.username.errors.append('User not activated')
            return False
        return True
