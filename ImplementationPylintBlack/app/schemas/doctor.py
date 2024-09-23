"""
doctor.py

This module defines the Pydantic model for a doctor in the API,
including validations and types for each field.
"""

from typing import Optional
from pydantic import BaseModel


class Doctor(BaseModel):
    """Pydantic model for representing a doctor."""

    doctor_id: Optional[
        int
    ]  # Optional since it might not be provided when creating a new doctor
    first_name: str
    last_name: str
    specialty: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
