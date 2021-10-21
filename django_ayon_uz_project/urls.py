from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django/admin/', admin.site.urls),
    path('django/', include('blog.urls', namespace='blog')),
    path('django/api/', include('blog_api.urls', namespace='blog_api')),
]
