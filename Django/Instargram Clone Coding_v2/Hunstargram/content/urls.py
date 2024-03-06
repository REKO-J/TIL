from django.urls import path

from .views import UploadFeed, UploadReply

urlpatterns = [
    path('upload', UploadFeed.as_view()),
    path('reply', UploadReply.as_view())
]
