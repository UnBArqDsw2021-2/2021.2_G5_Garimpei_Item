from fastapi import APIRouter
from typing import List
from schemas import ItemSchema, ShowItemSchema
from fastapi import status, Depends, Response
from sqlalchemy.orm import Session
from repositories import item as item_repository
from common.utils import get_db



router = APIRouter(
    prefix='/items',
    tags=['items']
)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(
    request: ItemSchema,
    db: Session = Depends(get_db)
):
    return item_repository.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id,
    db: Session = Depends(get_db)
):
    return item_repository.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(
    id,
    request: ItemSchema,
    db: Session = Depends(get_db)
):
    return item_repository.update(id, request, db)


@router.get('/', response_model=List[ShowItemSchema])
def list(
    item_id,
    db: Session = Depends(get_db)
):
    return item_repository.list(db)


@router.get('/{id}', response_model=ShowItemSchema)
def show(
    id: int,
    response: Response,
    db: Session = Depends(get_db)
):
    return item_repository.show(id, db)