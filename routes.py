from app import app, db, login_manager
from flask import render_template, request, flash, redirect, url_for
from forms import RegisterForm, LoginForm
from models import User
from flask_login import current_user, login_user, logout_user, login_required




#- ROUTES -

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        flash('You are already LoggedIn')
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.create_pw_hash(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Successfully registered')
        return redirect(url_for('index'))

    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already LoggedIn')
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_pw_hash(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))

    return render_template('login.html', form=form)
        

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)