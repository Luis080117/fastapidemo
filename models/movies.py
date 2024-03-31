from mongoengine import Document, StringField, IntField

class Movie(Document):
    title = StringField(required=True)
    year = IntField()

    meta = {'collection': 'movies'}

