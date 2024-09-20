from fastapi import FastAPI
from starlette.responses import RedirectResponse
from routes import doctor,patient

#DataBase
from contextlib import asynccontextmanager
from database import database as connection

@asynccontextmanager
async def lifespan(app: FastAPI):

    #connect to database if connection is closed
    if connection.is_closed():
        connection.connect()
    try:
        yield
    finally:
        #close the connection when the app stops
        if not connection.is_closed():
            connection.close()

app = FastAPI(lifespan=lifespan)

#Config
app.title = "ImplementationPylintBlack"
app.version = "1.0.0"

#Routes
app.include_router(doctor.doctors_route, prefix="/doctor", tags=["Doctor"])
app.include_router(patient.patients_route, prefix="/patient", tags=["Patient"])

#Documentation
@app.get("/")
async def docs():
    return RedirectResponse(url='/docs')