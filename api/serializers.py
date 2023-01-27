from rest_framework import serializers
from .models import (
    Organization, 
    Category,
    Job,
    Position
    )


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'name',
            'description'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description'
        ]


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = [
            'id',
            'name',
            'description'
        ]

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'id',
            'name',
            'description',
            'date_published',
            'job_start_date',
            'no_of_hire',
            'job_category_id',
            'job_position_id',
            'organizations_id',
            'no_of_applicants'
        ]







