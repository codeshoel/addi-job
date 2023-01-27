from django.urls import path
from .views import (
    organization_list_create_view,
    category_list_create_view,
    position_list_create_view,
    job_list_create_view,
)


urlpatterns = [
    path('organizations/', organization_list_create_view),
    path('categories/', category_list_create_view),
    path('positions/', position_list_create_view),
    path('jobs/', job_list_create_view),
    # path(''),
    # path(''),
]



