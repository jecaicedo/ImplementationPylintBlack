from dotenv import load_dotenv
from peewee import *

import os

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user = os.getenv("MYSQL_USER"),
    passwd = os.getenv("MYSQL_PASSWORD"),
    host = os.getenv("MYSQL_HOST"),
    port = os.getenv("MYSQL_PORT"),
)

class DoctorModel(Model):
    id : AutoField(primary_key=True)
    name : CharField(max_length=50)
    phone : IntegerField()

    class Meta:
        database = database
        table_name = "doctor"

class PatientModel(Model):
    id : AutoField(primary_key=True)
    name : CharField(max_length=50)
    phone : IntegerField()

    class Meta:
        database = database
        table_name = "patient"