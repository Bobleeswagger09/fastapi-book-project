from fastapi import APIRouter

from api.routes import books

api_router = APIRouter()
<<<<<<< HEAD
api_router.include_router(books.router, prefix="/books", tags=["books"])
=======
api_router.include_router(books.router, prefix="/books", tags=["books"])
>>>>>>> 1bad0e1c27fbb4bca60ceb33189d127d8eaabc4f
