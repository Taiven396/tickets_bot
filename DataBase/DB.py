from peewee import SqliteDatabase, Model
from peewee import DateTimeField, IntegerField, \
                   CharField

SmartTripBotDB = SqliteDatabase('SmartTripBot.db')

class Base(Model):

    class Meta:
        database = SmartTripBotDB

class Search(Base):

    search_date = DateTimeField()
    user_id = IntegerField()
    departure = CharField()
    destination = CharField()
    departure_at = CharField()
    return_at = CharField()
    type_of_search = CharField()

    class Meta:
        db_table = 'Tickets_Search'

class Showplaces(Base):

    search_date = DateTimeField()
    user_id = IntegerField()
    city = CharField()

    class Meta:
        db_table = 'Showplaces_Search'

def start_db():
    SmartTripBotDB.create_tables([Search])
    SmartTripBotDB.create_tables([Showplaces])
