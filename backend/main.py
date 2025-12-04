from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.api.v1 import router as v1_router

app = FastAPI(
    title="Truthline API",
    description="Backend API for Truthline",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(v1_router)


@app.get("/")
async def root():
    return {"message": "Welcome to Truthline API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}

