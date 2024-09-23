"""
main.py

This module configures and runs the FastAPI application for the ImplementationPylintBlack project.
It includes the configuration of the database and the routes for the different resources.
"""
# DataBase
from contextlib import asynccontextmanager
from database import database as connection

from fastapi import FastAPI
from starlette.responses import RedirectResponse
from routes import (
    patient_routes,
    doctor_routes,
    doctor_patient_routes,
)

@asynccontextmanager
async def lifespan(app_instance:FastAPI):  # pylint: disable=unused-argument
    """connect to database if connection is closed"""
    if connection.is_closed():
        connection.connect()
    try:
        yield
    finally:
        # close the connection when the app stops
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=lifespan)  # pylint: disable=redefined-outer-name

# Config
app.title = "ImplementationPylintBlack"
app.version = "1.0.0"

# Routes
app.include_router(doctor_routes.router, prefix="/doctor", tags=["Doctor"])
app.include_router(patient_routes.router, prefix="/patient", tags=["Patient"])
app.include_router(
    doctor_patient_routes.router, prefix="/doctor_patient", tags=["DoctorPatient"]
)

# Documentation
@app.get("/")
async def docs():
    """if you enter root /, you will be redirected to docs."""
    return RedirectResponse(url="/docs")
