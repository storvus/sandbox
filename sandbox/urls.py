from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include("sandbox.home.urls")),
    path('stripe/', include("sandbox.strip.urls", namespace="strip")),
    path('', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
]
