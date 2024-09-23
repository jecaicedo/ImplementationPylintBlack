"""
database.py

This module defines the database config in the API.
"""

import os
from dotenv import load_dotenv
from peewee import MySQLDatabase, Model

load_dotenv()

API_KEY = os.getenv("API_KEY")

# Configuración de la base de datos
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


class BaseModel(Model):
    """class for the base model"""

    class Meta:  # pylint: disable=too-few-public-methods
        """class for the instance to database"""

        database = database
