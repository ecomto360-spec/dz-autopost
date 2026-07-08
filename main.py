from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from loguru import logger

# Importer les modèles pour qu'ils soient reconnus par SQLAlchemy
from models import user, client, post

app = FastAPI(title="AutoPost API")

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://autopost.cbcbusness.com", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Créer les tables automatiquement au démarrage
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    logger.info("✅ Tables de base de données créées/vérifiées")

@app.get("/api/db-status")
def db_status():
    return {"status": "ok", "message": "Backend connecté à PostgreSQL !"}

@app.get("/")
def root():
    return {"message": "AutoPost API Backend"}