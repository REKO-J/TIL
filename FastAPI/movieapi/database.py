from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# FastAPI의 "Dependency Injection"
# db 세션 객체를 생성하고 종료하는 반복적인 작업 처리
def get_db():
    db = SessionLocal()
    try:
        yield db  # 제너레이터 함수
    finally:
        db.close()
