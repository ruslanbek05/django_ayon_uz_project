from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('django/admin/', admin.site.urls),
    path('django/', include('blog.urls', namespace='blog')),
    path('django/api/', include('blog_api.urls', namespace='blog_api')),
    path('django/api/user/', include('users.urls', namespace='users')),
    path('django/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('django/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('django/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
