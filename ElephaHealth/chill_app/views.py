import requests
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,)
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, DetailView

from rest_framework.permissions import IsAuthenticated
from .models import User, Analysis
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer


def __init__(self, token: str, url: str):
    self.session = requests.Session()
    self.url = url
    self.session.headers['Authorization'] = 'Bearer ' + token


def homepage(request: HttpRequest) -> HttpResponse:
    html = "ElephaHealth homepage"
    return HttpResponse(html)


class UserProfileListCreateView(ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly, IsAuthenticated]


def get_profile_statistics(request: HttpRequest) -> list:
    if request.method == "Get":
        statistics = Analysis.objects.filter(person=?who?)
        return list(statistics)
