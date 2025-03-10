
from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Rafiur'} 
    tasks =[{'taskname':'homework1', 
             'description':'finish calc stuff'},
            {'taskname':'homework2', 
             'description':'finish cs stuff'},
            {'taskname':'homework3', 
             'description':'finish science stuff'},
            ]
    return render_template('index.html', title='Home', user=user, tasks=tasks)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

