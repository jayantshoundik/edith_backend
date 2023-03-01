from django.urls import path, include
from .views import *
from . import views

urlpatterns = [ 
    # path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('file-upload', views.FileUploadExtractChequeAPIView.as_view()),
    path('file-upload-list', views.ListFileUploadExtractChequeAPIView.as_view()),
    path('search-file-upload-list', views.FileUploadExtractChequeAPIView.as_view()),


]