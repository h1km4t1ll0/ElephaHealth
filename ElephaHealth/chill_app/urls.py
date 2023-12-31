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
    path('profile_edit', views.UserProfileEdit.as_view({'post': 'retrieve'})),
    path("research/", views.GetProfileStatistics.as_view({'get': 'list'}), name="research"),
    # path("getfile/<str:filename>/", views.GetFile.as_view({'get': 'list'}), name="getfile"),
]
