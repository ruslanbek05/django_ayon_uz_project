from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('django/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('django/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('django/admin/', admin.site.urls),
    path('django/api/', include('blog_api.urls', namespace='blog_api')),
    path('django/api/user/', include('users.urls', namespace='users')),
    path('django/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('django/', include('blog.urls', namespace='blog')),
    path('django/docs/', include_docs_urls(title='BlogAPI')),
    path('django/schema', get_schema_view(
        title="BlogAPI",
        description="API for the BlogAPI",
        version="1.0.0"
    ), name='openapi-schema'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
