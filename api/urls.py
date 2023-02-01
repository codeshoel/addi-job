from django.urls import path
from .views import (
    user_viewset_view,
    organization_list_create_view,
    category_list_create_view,
    position_list_create_view,
    job_list_view,
    job_create_view,
)

# rest_framework imports.
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# from rest_framework.routers import DefaultRouter

urlpatterns = [
    
    path('user/', user_viewset_view),
    path('organizations/', organization_list_create_view),
    path('categories/', category_list_create_view),
    path('positions/', position_list_create_view),
    path('jobs/', job_list_view),
    path('jobs/create/', job_create_view),
    
    # Login/Registration urls
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

# router = DefaultRouter()
# router.register('user', user_viewset_view)

# urlpatterns += router.urls

