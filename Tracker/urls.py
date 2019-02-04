from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [

#path('', views.tracker_list, name='tracker_list'),

path('', views.tracker_list, name='tracker_list'),
path('tracker/<int:pk>/', views.tracker_detail, name='tracker_detail'),
path('tracker/new', views.tracker_new, name='tracker_new'),
path('tracker/<int:pk>/edit/', views.tracker_edit, name='tracker_edit'),
path('tracker/<int:pk>/teamedit/', views.tracker_edit1, name='tracker_edit1'),
url(r'^export/csv/$', views.some_view, name='some_view'),
path('tracker/calculator/', views.Calc_link, name='Calc_link'),
path('tracker/search', views.search, name='search'),

]