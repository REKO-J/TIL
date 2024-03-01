from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from content.models import Feed


# Create your views here.
class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all()
        return render(request, 'Hunstargram/main.html', context=dict(feed_list=feed_list))

class UploadFeed(APIView):
    def post(self, request):
        file = request.data.get('file')
        # profile_image = request.data.get('profile_image')
        # user_name = request.data.get('user_name')
        content_image = request.data.get('content_image')
        # like_count = request.data.get('like_count')
        # content = request.data.get('content')

        print(file)
        print(content_image)

        return Response(status=200)


class Login(APIView):
    def get(self, request):
        return render(request, 'Hunstargram/login.html')


class Profile(APIView):
    def get(self, request):
        return render(request, 'Hunstargram/profile.html')
