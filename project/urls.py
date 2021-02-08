from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.list_project, name='list_project'),
    path('search/', views.search_project, name='search_project'),
    path('addproject/', views.add_project, name='add_project')
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
