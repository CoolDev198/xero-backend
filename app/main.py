
from fastapi import FastAPI
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:3000",  # Allow your frontend to communicate
]
app = FastAPI(
    title="Show Me The Money",
    description="API for fetching Xero Balance Sheet data",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(router)
