from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import Routes
from backend.api.routes import auth
from backend.api.routes import threats
from backend.api.routes import packets
from backend.api.routes import incidents

# ---------------------------------------------------
# FastAPI App Initialization
# ---------------------------------------------------

app = FastAPI(

    title="Cyber Threat Detection Platform",

    description="""
    AI-Powered Cybersecurity Platform

    Features:
    - Threat Detection
    - Intrusion Detection
    - Incident Response
    - Threat Intelligence
    - Blockchain Log Integrity
    - AI Analytics
    """,

    version="1.0.0"
)

# ---------------------------------------------------
# CORS Configuration
# ---------------------------------------------------

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

# ---------------------------------------------------
# Register API Routes
# ---------------------------------------------------

app.include_router(auth.router)
app.include_router(threats.router)
app.include_router(packets.router)
app.include_router(incidents.router)

# ---------------------------------------------------
# Root Endpoint
# ---------------------------------------------------

@app.get("/")
def home():

    return {

        "message": "Cyber Threat Detection Platform Running",
        "status": "active",
        "version": "1.0.0"
    }

# ---------------------------------------------------
# Health Check Endpoint
# ---------------------------------------------------

@app.get("/health")
def health_check():

    return {

        "server": "running",
        "backend": "online",
        "api_status": "healthy"
    }
