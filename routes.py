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
    if current_user.is_authenticated():
        flash('You are already SignedIn')
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.create_pw_hash(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Successfully registered')
        return redirect(url_for('login'))

    return render_template('register.html')

        

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)