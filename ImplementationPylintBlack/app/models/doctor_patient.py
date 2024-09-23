"""
doctor.py

This module defines the model for a doctor in the API.
"""

from peewee import AutoField, ForeignKeyField, DateField, Model
from .patient import PatientModel
from .doctor import DoctorModel


class DoctorPatientModel(Model):
    """Model for representing a doctor."""

    doctor_patient_id = AutoField()
    patient_id = ForeignKeyField(
        PatientModel, backref="doctor_relationships", on_delete="CASCADE"
    )
    doctor_id = ForeignKeyField(
        DoctorModel, backref="patient_relationships", on_delete="CASCADE"
    )
    relationship_start_date = DateField()

    class Meta:  # pylint: disable=too-few-public-methods
        """class to represent the table in the database"""

        table_name = "DoctorPatient"
