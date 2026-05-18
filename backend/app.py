from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware

from backend.database.init_db import init_database

# Core route modules
from backend.api.routes.auth import router as auth_router
from backend.api.routes.threats import router as threats_router
from backend.api.routes.incidents import router as incidents_router
from backend.api.routes.packets import router as packets_router

# Security modules
from backend.api.routes.malware import router as malware_router
from backend.api.routes.intel import router as intel_router
from backend.api.routes.phishing import router as phishing_router
from backend.api.routes.intrusion import router as intrusion_router
from backend.api.routes.response import router as response_router


# Initialize database
init_database()


# Create FastAPI app
app = FastAPI(
    title="Cyber Threat Detection Platform",
    swagger_ui_parameters={
        "persistAuthorization": True
    }
)

# Security scheme
security = HTTPBearer()


# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register routers
app.include_router(auth_router)
app.include_router(threats_router)
app.include_router(incidents_router)
app.include_router(packets_router)

# Security feature routers
app.include_router(malware_router)
app.include_router(intel_router)
app.include_router(phishing_router)
app.include_router(intrusion_router)
app.include_router(response_router)


# Root endpoint
@app.get("/")
def root():
    return {
        "message":
        "Cyber Threat Detection Platform API running"
    }