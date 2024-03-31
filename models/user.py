from mongoengine import Document, StringField, EmailField, BooleanField

class User(Document):
    username = StringField(required=False, unique=True)
    password = StringField(required=True)
    email = EmailField(required=False, unique=True)
    is_active = BooleanField(default=True)

    meta = {'collection': 'users'}