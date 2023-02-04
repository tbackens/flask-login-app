from app import app, db, login_manager
from flask import render_template




#- ROUTES -

@app.route('/')
def index():
    return render_template('index.html')