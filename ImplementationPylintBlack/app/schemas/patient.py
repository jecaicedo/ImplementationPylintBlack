"""
patient.py

This module defines the Pydantic model for a patient in the API,
including validations and types for each field.
"""

from typing import Optional
from pydantic import BaseModel


class Patient(BaseModel):
    """Pydantic model for representing a patient."""

    patient_id: Optional[
        int
    ]  # Optional since it might not be provided when creating a new patient
    first_name: str
    last_name: str
    date_of_birth: str  # Consider using a date type if you're using datetime
    gender: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
