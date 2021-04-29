import datetime

from loguru import logger

from pony.orm import Database, Required, set_sql_debug, db_session, OperationalError

from worker.config import DB_NAME, DB_PASS, DB_USER, DB_HOST, DB_SCHEMA

db = Database()


class Logged(db.Entity):
    _table_ = (DB_SCHEMA, "logged")

    user_id = Required(int)
    image_id = Required(int)
    user_name = Required(str)
    endpoint = Required(str)
    date_from_api = Required(datetime.datetime)

    create_at = Required(datetime.datetime, default=datetime.datetime.utcnow)


try:
    db.bind(provider='postgres',
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            database=DB_NAME,
            options='-c search-path=SCHEMA')

    db.generate_mapping(create_tables=True)
    set_sql_debug(True)
except OperationalError:
    logger.error("CONNECTION ERROR: FROM DATA BASE")


@db_session
def add_logged(logg):
    Logged(
        user_id=logg['user_id'],
        image_id=logg['image_id'],
        user_name=logg['user_name'],
        endpoint=logg['endpoint'],
        date_from_api=datetime.datetime.strptime(logg['datetime'], '%Y-%m-%d %H:%M:%S')
    )
