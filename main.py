from peewee import *

db = PostgresqlDatabase('countries', user='capitals', password='abc123',
    host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Country(BaseModel):
    name = CharField()
    capital = CharField()