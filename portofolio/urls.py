from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('home.urls')),
    path('djangoadmin/', admin.site.urls),
    path('admin/', include('siteadmin.urls')),
    path('auth/', include('authentication.urls')),
    path('blogs/', include('blog.urls')),
    path('projects/', include('project.urls')),
    path('about-me/', include('AboutMe.urls')),
    path('contact-me/', include('ContactMe.urls')),
    path('admin-project/', include('admin_project.urls')),
    path('admin-blog/', include('admin_blog.urls')),
    
    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

