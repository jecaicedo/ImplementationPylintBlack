"""
patient_service.py

This module defines the services for a doctor patient relation in the API.
"""

from models.patient import PatientModel


class PatientService:
    """class for patient services"""

    @staticmethod
    def create_patient(data):
        """method for create patient"""
        patient = PatientModel.create(**data)
        return patient

    @staticmethod
    def get_patient(patient_id):
        """method for get patient"""
        return PatientModel.get_by_id(patient_id)

    @staticmethod
    def update_patient(patient_id, data):
        """method for update patient"""
        query = PatientModel.update(**data).where(PatientModel.patient_id == patient_id)
        query.execute()

    @staticmethod
    def delete_patient(patient_id):
        """method for delete patient"""
        PatientModel.get_by_id(patient_id).delete_instance()
