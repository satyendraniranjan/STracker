"""mysite URL Configuration

[...]
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

#from django.contrib import admin
from django.urls import include,path
#from django.conf.urls import url
#urlpatterns = (
#    url(r'^admin/', admin.site.urls),
    #url(r'^music/', include('music.urls')),
    # path(r'music', include('music.urls')),
#)
