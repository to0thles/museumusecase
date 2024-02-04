from peewee import *
import sys

sys.path.append('C:/museum-use-case/')

import settings

database = SqliteDatabase(f'{settings.DB_PATH}/{settings.DB_NAME}')


class BaseTable(Model):
    class Meta:
        database = database


class Artists(BaseTable):
    name = CharField(default='', max_length=50)
    birth_date = CharField(default='', max_length=50)
    nationally = CharField(default='', max_length=100)
    style = CharField(default='', max_length=75)


class Exhibts(BaseTable):
    artist_id = ForeignKeyField(Artists, backref='exhibts', default=0)
    name = CharField(default='', max_length=50)
    description = CharField(default='', max_length=100)
    date_acquired = CharField(default='', max_length=100)


class Curators(BaseTable):
    name = CharField(default='', max_length=50)
    department = CharField(default='', max_length=100)


class ExhibitCurators(BaseTable):
    exhibit_id = ForeignKeyField(Exhibts, backref='exhibit_curators', default=0)
    curator_id = ForeignKeyField(Curators, backref='exhibit_curators', default=0)


class ExhibitLocations(BaseTable):
    exhibit_id = ForeignKeyField(Exhibts, backref='exhibit_locations', default=0)
    room_number = CharField(default='', max_length=50)
    floor = CharField(default='', max_length=50)



class Collections(BaseTable):
    name = CharField(default='', max_length=50)
    description = CharField(default='', max_length=50)


class ExhibitCollection(BaseTable):
    collection_id = ForeignKeyField(Collections, backref='exhibit_collections', default=0)
    exhibit_id = ForeignKeyField(Exhibts, backref='exhibit_collections', default=0)


class Events(BaseTable):
    name = CharField(default='', max_length=50)
    date = CharField(default='', max_length=50)
    description = CharField(default='', max_length=100)


class Visitors(BaseTable):
    name = CharField(default='', max_length=50)
    email = CharField(default='', max_length=50)
    membership_status = CharField(default='', max_length=50)


class Tickets(BaseTable):
    visitor_id = CharField(default='', max_length=50)
    date_purchased = CharField(default='', max_length=50)
    price = CharField(default='', max_length=50)


database.create_tables(
    [Artists,
     Exhibts,
     Curators,
     ExhibitCurators,
     ExhibitLocations,
     Collections,
     ExhibitCollection,
     Events,
     Visitors,
     Tickets])