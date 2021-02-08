from django.urls import path
from . import views
urlpatterns = [  
    path('', views.list_about, name='list_about'),
]