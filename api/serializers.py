from rest_framework import serializers

from django.contrib.auth.models import User

from api.models import Job



class UserSerializer(serializers.ModelSerializer):
    class Mete:
        model = User
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'id', 
            'title', 
            'salary',
            'desc',
            'no_hire',
            'is_available',
            'deactivated_at',
            'post_is_paid',
            'posted_at'
        ]


