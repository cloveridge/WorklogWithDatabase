from peewee import *
from datetime import datetime

db = SqliteDatabase('tasks.db')

class Entry(Model):
    entry_date = DateField()
    project = CharField(max_length=255)
    notes = CharField(max_length=1000)
    employee = CharField(max_length=255)
    minutes = IntegerField()

    class Meta:
        database = db

    def get_project(self):
        project = ""
        while not project:
            project = input("Enter the project name (Required):\n> ")
        return project
    
    def get_employee(self):
        employee = ""
        while not employee:
            employee = input("Enter the employee name (Required):\n> ")
        return employee

    def get_notes(self):
        notes = ""
        while not notes:
            notes = input("Enter the notes:\n> ")
        return notes

    def display_date(self):
        return datetime.strftime(self.entry_date, "%m-%d-%Y")


def add_entry(self):
    Entry.create(entry_date=datetime.now(),
                 employee=self.get_employee(),
                 project=self.get_project(),
                 notes=self.get_notes())


def connect_db():
    db.connect()
    db.create_tables([Entry], safe=True)
