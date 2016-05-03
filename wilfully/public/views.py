# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from wilfully.extensions import login_manager
from wilfully.public.forms import LoginForm, SpouseRelationshipForm, ChildrenForm, FuneralBodyForm, FuneralServiceForm, FinancialAssetsForm
from wilfully.user.forms import RegisterForm
from wilfully.user.models import User
from wilfully.utils import flash_errors

blueprint = Blueprint('public', __name__, static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash('You are logged in.', 'success')
            redirect_url = request.args.get('next') or url_for('user.members')
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template('public/home.html', form=form)


@blueprint.route('/logout/')
@login_required
def logout():
    """Logout."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    """Register new user."""
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        User.create(username=form.username.data, email=form.email.data, password=form.password.data, active=True)
        flash('Thank you for registering. You can now log in.', 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('public/register.html', form=form)


@blueprint.route('/about/')
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template('public/about.html', form=form)


@blueprint.route('/faq/')
def faq():
    """FAQ page."""
    form = LoginForm(request.form)
    return render_template('public/faq.html', form=form)

@blueprint.route('/user/relations/spouse')
def spouse():
    """Spouse Form page."""
    settings_form = SpouseRelationshipForm(request.form)
    return render_template('public/spouse.html', form=None, settings_form=settings_form)

@blueprint.route('/user/relations/children')
def children():
    """Children Form page."""
    settings_form = ChildrenForm(request.form)
    return render_template('public/children.html', form=None, settings_form=settings_form)

@blueprint.route('/user/relations/dependent')
def dependent():
    """Dependent Form page."""
    settings_form = DependentForm(request.form)
    return render_template('public/dependent.html', form=None, settings_form=settings_form)

@blueprint.route('/user/funeral/funeralbody')
def funeral_body():
    """Funeral: Body Form page."""
    settings_form = FuneralBodyForm(request.form)
    return render_template('public/funeral_body.html', form=None, settings_form=settings_form)

@blueprint.route('/user/funeral/funeralservice')
def funeral_service():
    """Funeral: Service Form page."""
    settings_form = FuneralServiceForm(request.form)
    return render_template('public/funeral_service.html', form=None, settings_form=settings_form)

@blueprint.route('/user/will/financialassets')
def financial_assets():
    """Will: Financial Assets Form page."""
    settings_form = FinancialAssetsForm(request.form)
    return render_template('public/financial_assets.html', form=None, settings_form=settings_form)