import os
from uuid import uuid4

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from Hunstargram.settings import MEDIA_ROOT
from content.models import Feed
from user.models import User


# Create your views here.
class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all()

        print('로그인한 사용자 :', request.session['email'])

        email = request.session['email']
        if email is None:
            return render(request, 'user/login.html')

        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, 'user/login.html')

        return render(request, 'Hunstargram/main.html', context=dict(feeds=feed_list, user=user))


class UploadFeed(APIView):
    def post(self, request):
        # 일단 파일 불러와
        file = request.FILES['file']

        uuid_name = uuid4().hex  # 랜덤한 글자 생성(이미지 파일 이름 생성)
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        profile_image = request.data.get('profile_image')
        user_name = request.data.get('user_name')
        content_image = uuid_name
        content = request.data.get('content')

        Feed.objects.create(profile_image=profile_image, user_name=user_name, content_image=content_image, like_count=0, content=content)

        return Response(status=200)


class Profile(APIView):
    def get(self, request):
        return render(request, 'Hunstargram/profile.html')
