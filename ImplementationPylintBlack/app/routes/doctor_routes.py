"""
doctor_routes.py

This module defines the routes for a doctor in the API.
"""

from fastapi import APIRouter, HTTPException, Depends
from services.doctor_service import DoctorService
from schemas.doctor import Doctor
from auth import get_api_key

router = APIRouter()


@router.post("/doctors/", dependencies=[Depends(get_api_key)])
def create_doctor(doctor: Doctor):
    """Method for create patients"""
    return DoctorService.create_doctor(doctor.model_dump())


@router.get("/doctors/{doctor_id}", dependencies=[Depends(get_api_key)])
def get_doctor(doctor_id: int):
    """Method for get patients"""
    try:
        return DoctorService.get_doctor(doctor_id)
    except Doctor.DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="Doctor not found") from exc


@router.put("/doctors/{doctor_id}", dependencies=[Depends(get_api_key)])
def update_doctor(doctor_id: int, doctor: Doctor):
    """Method for update patients"""
    DoctorService.update_doctor(doctor_id, doctor.model_dump())
    return {"message": "Doctor updated"}


@router.delete("/doctors/{doctor_id}", dependencies=[Depends(get_api_key)])
def delete_doctor(doctor_id: int):
    """Method for delete doctors"""
    DoctorService.delete_doctor(doctor_id)
    return {"message": "Doctor deleted"}
