from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), # new]
    path('tracker/', include('Tracker.urls')),
    path('blog/', include('blog.urls')),
    path('music/', include('music.urls')),

]

#from django.contrib import admin
from django.urls import include,path
#from django.conf.urls import url
#urlpatterns = (
#    url(r'^admin/', admin.site.urls),
    #url(r'^music/', include('music.urls')),
    # path(r'music', include('music.urls')),
#)
