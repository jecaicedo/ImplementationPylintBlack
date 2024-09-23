"""
patient.py

This module defines the model for a patient in the API.
"""

from peewee import AutoField, CharField, DateField, Model


class PatientModel(Model):
    """Model for representing a patient."""

    patient_id = AutoField()
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    date_of_birth = DateField()
    gender = CharField(max_length=10, null=True)
    phone = CharField(max_length=20, null=True)
    email = CharField(max_length=100, null=True)
    address = CharField(max_length=255, null=True)

    class Meta:  # pylint: disable=too-few-public-methods
        """Class to represent the table in the database."""

        table_name = "Patients"
