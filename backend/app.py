from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database.init_db import init_database

from backend.api.routes.auth import router as auth_router
from backend.api.routes.threats import router as threats_router
from backend.api.routes.incidents import router as incidents_router
from backend.api.routes.packets import router as packets_router

# Initialize database tables
init_database()

app = FastAPI(
    title="Cyber Threat Detection Platform",
    version="1.0.0"
)

# CORS for frontend React app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # tighten later for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register route modules
app.include_router(auth_router)
app.include_router(threats_router)
app.include_router(incidents_router)
app.include_router(packets_router)


@app.get("/")
def root():
    return {
        "message": "Cyber Threat Detection Platform API running"
    }
