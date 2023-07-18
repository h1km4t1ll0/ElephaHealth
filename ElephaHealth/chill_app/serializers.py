from rest_framework import serializers
from .models import User, Analysis


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'


class UserResearchSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Analysis
        fields = '__all__'
