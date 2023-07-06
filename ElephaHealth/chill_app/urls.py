from django.contrib import admin
from django.urls import path, include
from ElephaHealth.chill_app import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("admin/", admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('profile/<int:pk>/', views.UserProfileDetailView.as_view(), name="profile"),
    path("all-profiles/", views.UserProfileListCreateView.as_view(), name="all-profiles"),

]
