import datetime

from pydantic import BaseModel, field_validator


class AnswerCreate(BaseModel):  # BaseModel 상속
    content: str  # 디폴드 값이 없기 때문에 필수값이다. 하지만 ""처럼 빈 문자열이 입력되면 안된다.

    @field_validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v


class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime
