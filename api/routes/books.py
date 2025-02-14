<<<<<<< HEAD

from typing import OrderedDict

from fastapi import APIRouter, status,HTTPException
=======
from typing import OrderedDict

from fastapi import APIRouter, status, HTTPException
>>>>>>> 1bad0e1c27fbb4bca60ceb33189d127d8eaabc4f
from fastapi.responses import JSONResponse

from api.db.schemas import Book, Genre, InMemoryDB

router = APIRouter()

db = InMemoryDB()
db.books = {
    1: Book(
        id=1,
        title="The Hobbit",
        author="J.R.R. Tolkien",
        publication_year=1937,
        genre=Genre.SCI_FI,
    ),
    2: Book(
        id=2,
        title="The Lord of the Rings",
        author="J.R.R. Tolkien",
        publication_year=1954,
        genre=Genre.FANTASY,
    ),
    3: Book(
        id=3,
<<<<<<< HEAD
        title="The Return of the King",
=======
        title='The Return of the King',
>>>>>>> 1bad0e1c27fbb4bca60ceb33189d127d8eaabc4f
        author="J.R.R. Tolkien",
        publication_year=1955,
        genre=Genre.FANTASY,
    ),
}

<<<<<<< HEAD

=======
>>>>>>> 1bad0e1c27fbb4bca60ceb33189d127d8eaabc4f
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_book(book: Book):
    db.add_book(book)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED, content=book.model_dump()
    )


@router.get(
    "/", response_model=OrderedDict[int, Book], status_code=status.HTTP_200_OK
)
async def get_books() -> OrderedDict[int, Book]:
    return db.get_books()


<<<<<<< HEAD
@router.put("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def update_book(book_id: int, book: Book) -> Book:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=db.update_book(book_id, book).model_dump(),
=======
@router.get(
    "/{book_id}", response_model=Book, status_code=status.HTTP_200_OK
)
async def get_book_by_id(book_id: int) -> Book:
    book = db.get_book(book_id)
    if book:
        return book
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )


@router.put("/{book_id}", response_model=Book, status_code=status.HTTP_200_OK)
async def update_book(book_id: int, book: Book) -> Book:
    updated_book = db.update_book(book_id, book)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=updated_book.model_dump(),
>>>>>>> 1bad0e1c27fbb4bca60ceb33189d127d8eaabc4f
    )


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int) -> None:
    db.delete_book(book_id)
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)

<<<<<<< HEAD


@router.get("/{book_id}",response_model=Book,status_code=status.HTTP_200_OK)
async def get_single_book(book_id: int) :
    getbook = db.books.get(book_id)
    if not getbook:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book not found")
    return getbook
=======
>>>>>>> 1bad0e1c27fbb4bca60ceb33189d127d8eaabc4f
