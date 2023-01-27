from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import authentication, permissions, generics


from .serializers import (
    OrganizationSerializer,
    JobSerializer,
    CategorySerializer,
    PositionSerializer,
)
from .models import (
    Job,
    Organization,
    Category,
    Position
)



class OrganizationSerializerAPIView(generics.ListCreateAPIView):

    """
    The API View handles the post and get organization data.
    """

    authentication_classes = [
        authentication.BasicAuthentication,
        # authentication.SessionAuthentication,
        ]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def perform_create(self, serializer):
        serializer.save()

organization_list_create_view = OrganizationSerializerAPIView.as_view()


class CategorySerializerListCreateAPIView(generics.ListCreateAPIView):
    
    """
    The API View handles the post and get job category data.
    """

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save()

category_list_create_view = CategorySerializerListCreateAPIView.as_view()


class PositionSerializerListCreateAPIView(generics.ListCreateAPIView):
    
    """
    The API View handles the post and get job position data.
    """

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def perform_create(self, serializer):
        serializer.save()

position_list_create_view = PositionSerializerListCreateAPIView.as_view()


class JobSerializerListCreateAPIView(generics.ListCreateAPIView):
    
    """
    The API View handles the post and get of job job data.
    """

    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        serializer.save()

job_list_create_view = JobSerializerListCreateAPIView.as_view()


