from django.urls import path
from blog import views


urlpatterns = [
    
    path('', views.list_blog, name='list_blog'),
    path('search/', views.search_blog, name='search_blog'),
    path('addblog/', views.add_blog, name='add_blog'),
]