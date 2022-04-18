from fastapi import APIRouter
from typing import List
from schemas import CategorySchema, ShowCategorySchema
from fastapi import status, Depends, Response
from sqlalchemy.orm import Session
from repositories import category as category_repository
from common.utils import get_db



router = APIRouter(
    prefix='/categories',
    tags=['categories']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(
    request: CategorySchema,
    db: Session = Depends(get_db)
):
    return category_repository.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id,
    db: Session = Depends(get_db)
):
    return category_repository.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(
    id,
    request: CategorySchema,
    db: Session = Depends(get_db)
):
    return category_repository.update(id, request, db)


@router.get('/', response_model=List[ShowCategorySchema])
def list(db: Session = Depends(get_db)):
    return category_repository.list(db)


@router.get('/{id}', response_model=ShowCategorySchema)
def show(
    id: int,
    response: Response,
    db: Session = Depends(get_db)
):
    return category_repository.show(id, db)