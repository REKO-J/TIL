from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URL = "sqlite:///./myapi.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # autocommit=True -> rollback 불가능!

Base = declarative_base()

# MetData 클래스 - 데이터베이스의 프라이머리 키, 유니크 키, 인덱스 키 등의 이름 규칙을 새롭게 정의(수동)
naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
Base.metadata = MetaData(naming_convention=naming_convention)


# FastAPI의 "Dependency Injection"
# db 세션 객체를 생성하고 종료하는 반복적인 작업 처리
def get_db():
    db = SessionLocal()
    try:
        yield db  # 제너레이터 함수
    finally:
        db.close()
