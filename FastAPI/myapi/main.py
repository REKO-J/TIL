from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.question import question_router
from domain.answer import answer_router

app = FastAPI()

# CORS 예외 URL 등록
origins = [
    "http://localhost:5173",  # 또는 "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(question_router.router)
app.include_router(answer_router.router)
