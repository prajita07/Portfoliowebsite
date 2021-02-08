from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.list_adminproject, name='list_adminproject'),
    path('search/', views.search_adminproject, name='search_adminproject'),
    path('addproject/', views.add_adminproject, name='add_adminproject'),
    path('detailproject/<int:id>/', views.detail_admin_project, name='detail_admin_project'),
    path('<int:id>', views.add_adminproject, name='update_adminproject'),
    path('delete/<int:id>/', views.admin_delete_project, name = 'admin_delete_project'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
