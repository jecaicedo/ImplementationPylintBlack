"""
patient.py

This module defines the Pydantic model for a doctor patient relation in the API,
including validations and types for each field.
"""

from pydantic import BaseModel


class DoctorPatient(BaseModel):
    """Pydantic model for representing a doctor model."""

    patient_id: int
    doctor_id: int
    relationship_start_date: str
