from app import app, db
from flask import render_template




#- ROUTES -

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)