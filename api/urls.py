from django.urls import path
from api.views import (
    job_list_view,
    job_rud_view,
    user_signup_apiview,
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('job/', job_list_view, name='job-listing-api'),
    path('job/<int:pk>/', job_rud_view, name='job-retrieve-update-delete-api'),
    path('user/registeration/', user_signup_apiview, name='user-registration-api'),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]


