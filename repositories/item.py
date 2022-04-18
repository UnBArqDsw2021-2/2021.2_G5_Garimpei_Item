from sqlalchemy.orm import Session
from schemas import ItemSchema
from models import Item
from fastapi import status, HTTPException


def create(request: ItemSchema, db: Session):
    title = request.title
    description = request.description
    category_id = request.category_id
    status = request.status

    item = Item(
        title=title,
        description=description,
        status=status
    )
    db.add(item)
    db.commit()
    db.refresh(item)

    return item


def destroy(id: int, db: Session):
    item = db.query(Item).filter(Item.id == id)

    if not item.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Item with the id {id} does not exists.'
        )

    item.delete(synchronize_session=False)
    db.commit()
    return True


def update(id: int, request: ItemSchema, db: Session):
    item = db.query(Item).filter(Item.id == id)

    if not item.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Item with the id {id} does not exists.'
        )

    item.update(request.dict())
    db.commit()
    return item.first()


def list(db: Session):
    items = db.query(Item).all()
    return items


def show(id: int, db: Session):
    item = db.query(Item).filter(Item.id == id).first()

    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Item with the id {id} does not exists.'
        )
    return item
