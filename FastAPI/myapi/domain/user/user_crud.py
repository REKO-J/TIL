from passlib.context import CryptContext
from sqlalchemy.orm import Session
from domain.user.user_schema import UserCreate
from models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # 비밀번호 복호화


def create_user(db: Session, user_create: UserCreate):
    db_user = User(username=user_create.username,
                   password=pwd_context.hash(user_create.password1),  # 복호화된 비밀번호 저장
                   email=user_create.email)
    db.add(db_user)
    db.commit()


# 중복 username, email check
def get_existing_user(db: Session, user_create: UserCreate):
    return db.query(User).filter(
        (User.username == user_create.username) | (User.email == user_create.email)
    ).first()


# user 비밀번호 비교
def get_user(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()
