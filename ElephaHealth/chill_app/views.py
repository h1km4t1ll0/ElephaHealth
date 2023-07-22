import requests
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,)
from django.http import HttpResponse, HttpRequest
from rest_framework import viewsets
from rest_framework.response import Response
from django.views.generic import ListView, DetailView

from rest_framework.permissions import IsAuthenticated
from .models import User, Analysis
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import UserProfileSerializer, UserResearchSerializer


def __init__(self, token: str, url: str):
    self.session = requests.Session()
    self.url = url
    self.session.headers['Authorization'] = 'Bearer ' + token


def homepage(request: HttpRequest) -> HttpResponse:
    html = "ElephaHealth homepage"
    return HttpResponse(html)


class UserProfileListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class GetProfileStatistics(viewsets.ModelViewSet):
    serializer_class = UserResearchSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        data = self.request.user.analysis.all()
        return Response({'data': data})

    def list(self, request, *args, **kwargs):
        data = self.request.user.analysis.all()
        return Response({'data': data})
