from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
    path('home/', createTask, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)