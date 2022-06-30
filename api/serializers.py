from api.models import Business
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'id',
        ]

class BusinessSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField()

    owner = UserSerializer()

    class Meta:
        model = Business
        fields = [
            # 'url',
            'id',
            'location',
            'name',
            'owner',
            'worth',
        ]
