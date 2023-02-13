from rest_framework import serializers

from django.contrib.auth.models import User

from api.models import Job



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True, style = {'input_type': 'password'})
    is_staff = serializers.BooleanField(default=True)

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'is_staff',
        ]


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'owner',
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


