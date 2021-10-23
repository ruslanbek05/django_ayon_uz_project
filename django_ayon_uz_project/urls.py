from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django/admin/', admin.site.urls),
    path('django/', include('blog.urls', namespace='blog')),
    path('django/api/', include('blog_api.urls', namespace='blog_api')),
    path('django/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
