"""ccut_helper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('find_student/(?P<id>\d{1,10})', views.See_Students.as_view()),
    re_path('find_blog/(?P<user_id>\d{1,10})', views.See_Blog.as_view()),
    path('login/',views.Login.as_view()),
    path('changes/',views.Changes.as_view()),
    path('putblog/',views.PutBlog.as_view()),
    re_path('delete_blog/(?P<id>\d{1,100})',views.DeleteBlog.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns = format_suffix_patterns(urlpatterns)
