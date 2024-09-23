"""
doctor_service.py

This module defines the services for a doctor in the API.
"""

from models.doctor import DoctorModel


class DoctorService:
    """class for doctor services"""

    @staticmethod
    def create_doctor(data):
        """method for create doctor"""
        doctor = DoctorModel.create(**data)
        return doctor

    @staticmethod
    def get_doctor(doctor_id):
        """method for get doctor"""
        return DoctorModel.get_by_id(doctor_id)

    @staticmethod
    def update_doctor(doctor_id, data):
        """method for update doctor"""
        query = DoctorModel.update(**data).where(DoctorModel.doctor_id == doctor_id)
        query.execute()

    @staticmethod
    def delete_doctor(doctor_id):
        """method for delete doctor"""
        DoctorModel.get_by_id(doctor_id).delete_instance()
