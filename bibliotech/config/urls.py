from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),

    # auth (logowanie)
    path('accounts/', include('django.contrib.auth.urls')),

    # API BiblioTech (dodamy za chwilę)
    path('api/v1/', include('library.api_urls')),

    # dokumentacja OpenAPI / Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # frontend HTML
    path('', include('library.urls')),
]
