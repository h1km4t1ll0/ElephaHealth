import requests
import os

from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,)
from django.http import HttpResponse, HttpRequest, FileResponse, Http404

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework.response import Response
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


class UserProfileDetailView(ListCreateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def get_queryset(self) -> Response:
        data = User.objects.filter(pk=self.request.user.pk)
        return data


class AdminUserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminUser]


class GetProfileStatistics(viewsets.ModelViewSet):
    serializer_class = UserResearchSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def retrieve(self, request, *args, **kwargs) -> Response:
        data = self.request.user.analysis.all()
        return Response({'data': data})

    def list(self, request, *args, **kwargs) -> Response:
        data = self.request.user.analysis.all()
        return Response({'data': data})


class GetFile(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        filename = kwargs['filename']
        file_path = f'ElephaHealth/chill_app/sound_matrices/{filename}'
        if os.path.exists(file_path):
            response = FileResponse(open(file_path, 'rb'))
            return response
        raise Http404
