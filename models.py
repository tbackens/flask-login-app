from app import db, login_manager
from werkzeug.security import check_password_hash, generate_password_hash



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    def create_pw_hash(self, password):
        self.password_hash = generate_password_hash(password)

    def check_pw_hash(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return '<User {}>'.format(self.username)
