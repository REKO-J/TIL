import os
from uuid import uuid4

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from Hunstargram.settings import MEDIA_ROOT
from content.models import Feed, Reply, Like
from user.models import User


# Create your views here.
class Main(APIView):
    def get(self, request):
        email = request.session.get("email", None)
        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, "user/login.html")

        feed_object_list = Feed.objects.all()
        feed_list = []

        for feed in feed_object_list:
            user = User.objects.filter(email=feed.email).first()
            reply_object_list = Reply.objects.filter(feed_id=feed.id)
            reply_list = []
            for reply in reply_object_list:
                user = User.objects.filter(email=reply.email).first()
                reply_list.append(dict(reply_content=reply.reply_content,
                                       nickname=user.nickname
                                       ))
            like_count = Like.objects.filter(feed_id=feed.id, is_like=True).count()
            is_liked = Like.objects.filter(feed_id=feed.id, email=email, is_like=True).exists()
            feed_list.append(dict(id=feed.id,
                                  content_image=feed.content_image,
                                  content=feed.content,
                                  like_count=like_count,
                                  profile_image=user.profile_image,
                                  nickname=user.nickname,
                                  reply_list=reply_list,
                                  is_liked=is_liked
                                  ))

        return render(request, "Hunstargram/main.html", context=dict(feeds=feed_list, user=user))


class UploadFeed(APIView):
    def post(self, request):
        # 일단 파일 불러와
        file = request.FILES['file']

        uuid_name = uuid4().hex  # 랜덤한 글자 생성(이미지 파일 이름 생성)
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        email = request.session.get('email', None)
        content_image = uuid_name
        content = request.data.get('content')

        Feed.objects.create(email=email, content_image=content_image, content=content, like_count=0)

        return Response(status=200)


class UploadReply(APIView):
    def post(self, request):
        feed_id = request.data.get('feed_id', None)
        reply_content = request.data.get('reply_content', None)
        email = request.session.get('email', None)

        Reply.objects.create(feed_id=feed_id, reply_content=reply_content, email=email)

        return Response(status=200)

    class ToggleLike(APIView):
        def post(self, request):
            feed_id = request.data.get('feed_id', None)
            is_like = request.data.get('is_like', True)

            if is_like == 'true' or is_like == 'True':
                is_like = True
            else:
                is_like = False

            email = request.session.get('email', None)

            Like.objects.create(feed_id=feed_id, is_like=is_like, email=email)

            return Response(status=200)
