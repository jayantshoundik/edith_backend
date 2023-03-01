from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView,)

urlpatterns = [ 
    
    path('home-page', views.HomePageAPIView.as_view()),
]