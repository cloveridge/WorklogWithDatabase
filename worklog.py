from entry import Entry
from entry import db


def connect_db():
    db.connect()
    db.create_tables([Entry], safe=True)


def extract_db():
    connect_db()
    db_as_list = Entry.select().order_by(Entry.entry_date.desc())
    return db_as_list


if __name__ == "__main__":
    pass
