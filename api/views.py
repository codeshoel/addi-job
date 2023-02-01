from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import (
    authentication, 
    permissions, 
    generics, 
    viewsets
    )


from .serializers import (
    OrganizationSerializer,
    JobSerializer,
    CategorySerializer,
    PositionSerializer,
    UserSerializer,
)

from .models import (
    Job,
    Organization,
    Category,
    Position
)


class UserViewset(viewsets.ModelViewSet):
    # authentication_classes = [
    #     # authentication.BasicAuthentication,
    #     authentication.TokenAuthentication,
    #     ]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

user_viewset_view = UserViewset.as_view({'get': 'list', 'post': 'create'})


class OrganizationSerializerAPIView(generics.ListCreateAPIView):

    """
    The API View handles the post and get organization data.
    """

    authentication_classes = [
        authentication.BasicAuthentication,
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
        ]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def perform_create(self, serializer):
        serializer.save()

organization_list_create_view = OrganizationSerializerAPIView.as_view()


class CategorySerializerListCreateAPIView(generics.ListCreateAPIView):
    
    """
    The API View handles the post and get job category data.
    """

    # authentication_classes = [
    #     authentication.BasicAuthentication,
    #     authentication.SessionAuthentication,
    #     authentication.TokenAuthentication
    #     ]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save()

category_list_create_view = CategorySerializerListCreateAPIView.as_view()


class PositionSerializerListCreateAPIView(generics.ListCreateAPIView):
    
    """
    The API View handles the post and get job position data.
    """

    # authentication_classes = [
    #     authentication.BasicAuthentication,
    #     authentication.SessionAuthentication,
    #     authentication.TokenAuthentication
    #     ]
    
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def perform_create(self, serializer):
        serializer.save()

position_list_create_view = PositionSerializerListCreateAPIView.as_view()


class JobSerializerListAPIView(generics.ListAPIView):
    
    """
    The API View permmits read-only endpoint (GET request method) to job model instance.
    """

    queryset = Job.objects.all()
    serializer_class = JobSerializer

job_list_view = JobSerializerListAPIView.as_view()


class JobSerializerCreateAPIView(generics.CreateAPIView):
    
    """
    The API View permmits create-only endpoint (POST request method) to job model instance.
    """

    authentication_classes = [
        authentication.BasicAuthentication,
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
        ]

    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        serializer.save()

job_create_view = JobSerializerCreateAPIView.as_view()


