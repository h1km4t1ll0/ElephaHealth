from django.contrib import admin
from django.urls import path, include
from ElephaHealth.chill_app import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("admin/", admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
