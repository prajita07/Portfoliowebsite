from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.dashbaord, name='dashboard'),
    path('admincontact/', views.contact, name='contact'),
    path('adminhome/', views.home_admin,name='home_admin'),
    path('<int:id>',views.update_homeadmin, name='update_homeadmin'),
    path('adminAboutMe/', views.list_aboutadmin, name='list_aboutadmin'),
    path('detailabout/<int:id>/', views.detail_adminabout, name='detail_adminabout'),
    path('update-about/<int:id>/', views.update_adminabout, name='update_adminabout'),
    path('delete/<int:id>/', views.admin_delete_about, name = 'admin_delete_about'),
    path('addexperience/', views.update_adminExperiences, name = 'add_adminExperiences'),
    path('skills/create/', views.create_skill, name='create_skill'),
    path('updateexperience/<int:id>/', views.update_adminExperiences, name = 'update_adminExperiences'),
    path('users/', views.showthis, name= 'users'),
    path('password/$', views.change_password, name='change_password' ),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
