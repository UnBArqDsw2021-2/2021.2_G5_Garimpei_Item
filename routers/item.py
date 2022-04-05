from fastapi import APIRouter


router = APIRouter(
    prefix='/item',
    tags=['item']
)


@router.get('/')
def check():
    return dict(ok=True)

@router.post('/')
def check():
    return dict(ok=True)

@router.put('/')
def check():
    return dict(ok=True)

@router.delete('/')
def check():
    return dict(ok=True)
