from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .settings import MEDIA_URL, MEDIA_ROOT
from content.views import Main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Main.as_view()),
    path('', include('content.urls')),
    path('', include('user.urls'))
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
