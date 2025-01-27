from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from src.extensions import db
from src.models import BaseModel


class User(BaseModel, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email_address = db.Column(db.String)
    phone_number = db.Column(db.String)
    _password = db.Column(db.String)
    human_id = db.Column(db.Integer, db.ForeignKey("people.id"))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    human = db.relationship("Human", uselist=False)
    role = db.relationship("Role", uselist=False)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self._password, password)

    def __init__(self, username, email_address, phone_number, password, human_id, role_id):
        self.username = username
        self.email_address = email_address
        self.phone_number = phone_number
        self.password = password
        self.human_id = human_id
        self.role_id = role_id

    def __repr__(self):
        return f"{self.username} (User)"


class Role(BaseModel):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name} (Role)"
