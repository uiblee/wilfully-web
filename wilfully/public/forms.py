# -*- coding: utf-8 -*-
"""Public forms."""
from flask_wtf import Form
from wtforms import PasswordField, StringField, BooleanField, IntegerField, TextAreaField, RadioField, SelectField, validators
from wtforms.validators import DataRequired

from wilfully.user.models import User


class SpouseRelationshipForm(Form):
    married = BooleanField('Are you married?', validators=[DataRequired()])
    spousename = StringField('Spouse name')

class ChildrenForm(Form):
    children = BooleanField('Do you have children?', validators=[DataRequired()])
    childrennumber = IntegerField('Children number', [validators.NumberRange(min=0, max=100)], id="childrennumber")
    childrenname = StringField('Children 1 name')

class DependentForm(Form):
    dependent = BooleanField('Do you have any dependents?', validators=[DataRequired()])
    dependentnumber = IntegerField('Dependent number', [validators.NumberRange(min=0, max=100)], id="dependentnumber")
    dependentname = StringField('Dependent 1 name')

class FuneralBodyForm(Form):
    funeral_body = RadioField('Do you want to be buried or cremated?', choices=[('value','Buried'),('value_two','Cremated'), ('value_three','Other')])
    buriallocation = StringField('Burial location')
    burialdetails = TextAreaField('Burial details')

class FuneralServiceForm(Form):
    funeral_service = RadioField('Do you want to have a service?', choices=[('value','Yes'),('value_two','No')])
    servicelocation = StringField('Service location')
    servicedetails = TextAreaField('Service details')

class FinancialAssetsForm(Form):
    desendants = BooleanField('Split all financial assets evenly among all living desendants?', validators=[DataRequired()])
    fin_assets = StringField('To whom do you leave your financial assets?')
    percent_fin_assets = IntegerField('What percentage do you want to leave to this individual?')
    accountdetails = TextAreaField('Where are all of your accounts (Savings, Checking, IRA, 401k, Trading, etc.')

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
