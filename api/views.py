from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Job

from api.serializers import JobSerializer


class JobListCreateAPIView(generics.ListCreateAPIView):
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

    def perform_create(self, serializer):
        serializer.save()

job_list_create_view = JobListCreateAPIView.as_view()



class JobRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all().order_by('-post_is_paid', '-posted_at')
    serializer_class = JobSerializer


    def retrieve(self, request, *args, **kwargs):
        pk = kwargs['pk']
        try:
            instance = self.queryset.get(id=pk, is_available=True)
        except Job.DoesNotExist:
            return Response({"message": "Job is not available."})
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

job_rud_view = JobRUDAPIView.as_view()


class LoginAPIView(APIView):
    pass



class RegistrationAPIView(APIView):
    pass


