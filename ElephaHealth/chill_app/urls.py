from django.contrib import admin
from django.urls import path, include
from ElephaHealth.chill_app import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("admin/", admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('profile/', views.UserProfileDetailView.as_view(), name="profile"),
    path('profile/<int:pk>/', views.AdminUserProfileDetailView.as_view(), name="pk_profile"),
    path("all-profiles/", views.UserProfileListCreateView.as_view(), name="all-profiles"),
    path("research/", views.GetProfileStatistics.as_view({'get': 'list'}), name="research")
]
