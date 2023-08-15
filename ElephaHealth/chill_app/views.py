import requests
import os
import json

from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,)
from django.http import HttpResponse, HttpRequest, FileResponse, Http404

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets, status
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


class UserProfileEdit(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        cur_user = User.objects.filter(pk=self.request.user.pk)[0]
        req_data = json.loads(request.body)
        cur_user.username = req_data['username']
        cur_user.first_name = req_data['first_name']
        cur_user.last_name = req_data['last_name']
        cur_user.date_of_birth = req_data['date_of_birth']
        cur_user.gender = req_data['gender']
        cur_user.phone_number = req_data['phone_number']
        cur_user.email = req_data['email']
        cur_user.company = req_data['company']
        cur_user.height = req_data['height']
        cur_user.weight = req_data['weight']
        cur_user.avg_heart_rate = req_data['avg_heart_rate']
        cur_user.password = req_data['password']
        cur_user.save()

        return HttpResponse(status=status.HTTP_201_CREATED)


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
