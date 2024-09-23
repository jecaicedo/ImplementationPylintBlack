"""
patient_routes.py

This module defines the routes for a patient in the API.
"""

from fastapi import APIRouter, HTTPException, Depends
from services.patient_service import PatientService
from schemas.patient import Patient
from auth import get_api_key

router = APIRouter()


@router.post("/patients/", dependencies=[Depends(get_api_key)])
def create_patient(patient: Patient):
    """Method for create patients"""
    return PatientService.create_patient(patient.model_dump())


@router.get("/patients/{patient_id}", dependencies=[Depends(get_api_key)])
def get_patient(patient_id: int):
    """Method for get patients"""
    try:
        return PatientService.get_patient(patient_id)
    except Patient.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Patient not found") from exc


@router.put("/patients/{patient_id}", dependencies=[Depends(get_api_key)])
def update_patient(patient_id: int, patient: Patient):
    """Method for update patients"""
    PatientService.update_patient(patient_id, patient.model_dump())
    return {"message": "Patient updated"}


@router.delete("/patients/{patient_id}", dependencies=[Depends(get_api_key)])
def delete_patient(patient_id: int):
    """Method for delete patients"""
    PatientService.delete_patient(patient_id)
    return {"message": "Patient deleted"}
