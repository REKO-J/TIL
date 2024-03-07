# Instargram Clone Coding

## 프로젝트 소개
인스타그램을 클론코딩한 Django 웹 애플리케이션입니다. 사용자는 사진 업로드, 좋아요, 댓글 작성 등의 기능을 활용할 수 있습니다.

## 주요 기능
1. 회원가입 및 로그인: 사용자는 회원가입을 통해 계정을 생성하고, 로그인하여 서비스를 이용할 수 있습니다.
2. 프로필 관리: 사용자는 프로필 페이지에서 자신의 프로필 이미지를 변경할 수 있습니다.
3. 사진 업로드: 사용자는 사진을 업로드하여 다른 사용자들에게 공유할 수 있습니다.
4. 좋아요 및 댓글: 사용자는 게시물에 좋아요를 누르거나 댓글을 작성할 수 있습니다.
5. 북마크: 사용자는 다른 사용자의 게시물을 저장할 수 있습니다.

## 설치 및 실행
1. 프로젝트를 클론합니다. <br>
- https://github.com/REKO-J/TIL/tree/main/Django/InstargramCloneCoding
2. 가상환경을 설정하고 의존성을 설치합니다. <br>
- cd instagram-clone
- python -m venv venv
- source venv/bin/activate  # Windows의 경우: venv\Scripts\activate
- pip install -r requirements.txt
3. 데이터베이스 마이그레이션을 수행합니다. <br>
- python manage.py migrate
4. 개발 서버를 실행합니다. <br>
- python manage.py runserver
5. 웹 브라우저에서 http://localhost:8000/main으로 접속합니다.
