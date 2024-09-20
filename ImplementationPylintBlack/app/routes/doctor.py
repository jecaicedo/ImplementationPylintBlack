from fastapi import APIRouter, Body
from models.doctor import Doctor

doctors_route = APIRouter()

#method get for doctor
@doctors_route.get("/get_doctors", tags=["Doctor"])
def get_doctors():
    return {"message": "ok"}

#method post for doctor
@doctors_route.post("/post_doctors", tags=["Doctor"])
async def post_doctors(doctor : Doctor = Body(...)):
    return {"message": "ok"}

#method put for doctor
@doctors_route.put("/put_doctors", tags=["Doctor"])
def put_doctors():
    return {"message": "ok"}

#method delete for doctor
@doctors_route.delete("/delete_doctors", tags=["Doctor"])
def delete_doctors():
    return {"message": "ok"}