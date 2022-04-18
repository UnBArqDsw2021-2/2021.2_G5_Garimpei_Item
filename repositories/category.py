from sqlalchemy.orm import Session
from schemas import CategorySchema, CategorySchema
from models import Category
from fastapi import status, HTTPException


def create(request: CategorySchema, db: Session):
    name = request.name
    description = request.description

    category = Category(
        name=name,
        description=description
    )
    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def destroy(id: int, db: Session):
    category = db.query(Category).filter(Category.id == id)

    if not category.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Category with the id {id} does not exists.'
        )

    category.delete(synchronize_session=False)
    db.commit()
    return True


def update(id: int, request: CategorySchema, db: Session):
    category = db.query(Category).filter(Category.id == id)

    if not category.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Category with the id {id} does not exists.'
        )

    category.update(request.dict())
    db.commit()
    return category.first()


def list(db: Session):
    categories = db.query(Category).all()
    return categories


def show(id: int, db: Session):
    category = db.query(Category).filter(Category.id == id).first()

    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Category with the id {id} does not exists.'
        )
    return category
