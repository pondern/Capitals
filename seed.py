from peewee import *
from main import Country
from main import db
import json

db.connect()
db.drop_tables([Country])
db.create_tables([Country])

file = open('countries.json')
data = json.load(file)

Country.insert_many(data).execute()