import stripe

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import generics, permissions, authentication
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Job

from api.serializers import JobSerializer, UserSerializer


class JobListAPIView(generics.ListAPIView):

    authentication_classes = []
    permission_classes = []
    serializer_class = JobSerializer

    def get_queryset(self):
        queryset = Job.objects.all().order_by('-post_is_paid', '-posted_at')
        sq = self.request.GET.get('q')

        if sq is not None:
            qs = queryset.filter(title__contains=sq, is_available=True)
            return qs
        else:
            qs = queryset.filter(is_available=True)
            return qs

job_list_view = JobListAPIView.as_view()



class JobRudAPIView(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Job.objects.all().order_by('-post_is_paid', '-posted_at')
    serializer_class = JobSerializer


    def retrieve(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            instance = self.queryset.get(id=pk)
        except Job.DoesNotExist:
            return Response({"message": "Job is not available."})
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


job_rud_view = JobRudAPIView.as_view()


class AuthUserJobListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = JobSerializer
    
    def get_queryset(self):
        queryset = Job.objects.all().order_by('-id')
        try:
            user_id = self.request.user.id
            qs = queryset.filter(owner=user_id)
            return qs
        except queryset.DoesNotExist:
            return Response({'message': 'You no have Job Posts.'})

auth_user_list_create_endpoint = AuthUserJobListCreateAPIView.as_view()


class UserRegistrationAPIView(generics.CreateAPIView):
    permission_classes = []
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if (first_name and last_name and username) and (email and password) is not None:

            user = User.objects.create(
                first_name=first_name, 
                last_name=last_name,
                username=username,
                email=email, 
                password=make_password(password),
                is_staff=True
                )
            user.save()
            return Response({'message': f'{username} was registered successfully.'})
        return Response({'error': 'All fields are expected to be filled.'})

user_signup_apiview = UserRegistrationAPIView.as_view()


class StripePaymentAPIView(APIView):
    pass


