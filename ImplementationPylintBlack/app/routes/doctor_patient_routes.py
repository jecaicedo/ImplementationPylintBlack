"""
doctor_routes.py

This module defines the routes for a doctor patient relation in the API.
"""

from fastapi import APIRouter, HTTPException, Depends
from services.doctor_patient_service import DoctorPatientService
from schemas.doctor_patient import DoctorPatient
from auth import get_api_key

router = APIRouter()


@router.post("/doctor_patient/", dependencies=[Depends(get_api_key)])
def create_relationship(relationship: DoctorPatient):
    """Method for create relation"""
    return DoctorPatientService.create_relationship(relationship.model_dump())


@router.get("/doctor_patient/{doctor_patient_id}", dependencies=[Depends(get_api_key)])
def get_relationship(doctor_patient_id: int):
    """Method for get relation"""
    try:
        return DoctorPatientService.get_relationship(doctor_patient_id)
    except DoctorPatient.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Relationship not found") from exc


@router.put("/doctor_patient/{doctor_patient_id}", dependencies=[Depends(get_api_key)])
def update_relationship(doctor_patient_id: int, relationship: DoctorPatient):
    """Method for update relation"""
    DoctorPatientService.update_relationship(
        doctor_patient_id, relationship.model_dump()
    )
    return {"message": "Relationship updated"}


@router.delete(
    "/doctor_patient/{doctor_patient_id}", dependencies=[Depends(get_api_key)]
)
def delete_relationship(doctor_patient_id: int):
    """Method for delete relation"""
    DoctorPatientService.delete_relationship(doctor_patient_id)
    return {"message": "Relationship deleted"}
