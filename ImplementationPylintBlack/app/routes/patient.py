from fastapi import APIRouter, Body
from models.patient import Patient

patients_route = APIRouter()

#method get for patient
@patients_route.get("/get_patients", tags=["Patient"])
def get_patients():
    return {"patients":[]}

#method post for patient
@patients_route.post("/post_patients", tags=["Patient"])
def post_patients(patient : Patient = Body(...)):
    return {"patients":[]}

#method put for patient
@patients_route.put("/put_patients", tags=["Patient"])
def put_patients():
    return {"patients":[]}

#method delete for patient
@patients_route.delete("/delete_patients", tags=["Patient"])
def delete_patients():
    return {"patients":[]}