from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.list_adminblog, name='list_adminblog'),
    path('search/', views.search_adminblog, name='search_adminblog'),
    path('addblog/', views.add_adminblog, name='add_adminblog'),
    path('detailblog/<int:id>/', views.detail_admin_blog, name='detail_admin_blog'),
    path('<int:id>', views.add_adminblog, name='update_adminblog'),
    path('delete/<int:id>/', views.admin_delete_blog, name = 'admin_delete_blog'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
