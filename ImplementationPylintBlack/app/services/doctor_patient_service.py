"""
doctor_patient_service.py

This module defines the services for a doctor patient relation in the API.
"""

from models.doctor_patient import DoctorPatientModel


class DoctorPatientService:
    """class for doctor patient relation services"""

    @staticmethod
    def create_relationship(data):
        """method for create doctor patient relation"""
        relationship = DoctorPatientModel.create(**data)
        return relationship

    @staticmethod
    def get_relationship(doctor_patient_id):
        """method for get doctor patient relation"""
        return DoctorPatientModel.get_by_id(doctor_patient_id)

    @staticmethod
    def update_relationship(doctor_patient_id, data):
        """method for update doctor patient relation"""
        query = DoctorPatientModel.update(**data).where(
            DoctorPatientModel.doctor_patient_id == doctor_patient_id
        )
        query.execute()

    @staticmethod
    def delete_relationship(doctor_patient_id):
        """method for delete doctor patient relation"""
        DoctorPatientModel.get_by_id(doctor_patient_id).delete_instance()
