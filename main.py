import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.check import router as check_router
from routers.item import router as item_router
from routers.category import router as category_router
from common.database import engine
from common.settings import ORIGINS


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(check_router)
app.include_router(category_router)
app.include_router(item_router)


if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)