from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
<<<<<<< HEAD
from api.router import api_router

=======

from api.router import api_router
>>>>>>> 1bad0e1c27fbb4bca60ceb33189d127d8eaabc4f
from core.config import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_PREFIX)


@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}
<<<<<<< HEAD

=======
>>>>>>> 1bad0e1c27fbb4bca60ceb33189d127d8eaabc4f

@app.get("/stage2")
async def stage2():
    return {"message": "welcome to stage 2"}
