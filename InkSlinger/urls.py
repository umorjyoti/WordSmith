
from django.contrib import admin
from django.urls import path, include
from post import views
from django.views.static import serve
from django.conf.urls import url 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('account/',include('account.urls')),
    path('post/',include('post.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
