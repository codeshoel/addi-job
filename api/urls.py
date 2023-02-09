from django.urls import path
from .views import (
    job_list_create_view,
    job_rud_view,
)

urlpatterns = [
    path('job/', job_list_create_view),
    path('job/<int:pk>/', job_rud_view),
]


