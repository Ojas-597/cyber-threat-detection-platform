from fastapi import FastAPI
from api.routes import auth, threats, packets, incidents

app = FastAPI(title="Cyber Threat Detection Platform")

app.include_router(auth.router)
app.include_router(threats.router)
app.include_router(packets.router)
app.include_router(incidents.router)

@app.get("/")
def home():
    return {"message": "Platform Running"}
