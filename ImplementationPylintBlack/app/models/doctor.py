"""
doctor.py

This module defines the model for a doctor in the API.
"""

from peewee import AutoField, CharField, Model


class DoctorModel(Model):
    """Model for representing a doctor."""

    doctor_id = AutoField()
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    specialty = CharField(max_length=100, null=True)
    phone = CharField(max_length=20, null=True)
    email = CharField(max_length=100, null=True)

    class Meta:  # pylint: disable=too-few-public-methods
        """Class to represent the table in the database."""

        table_name = "Doctors"
