from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView,)

urlpatterns = [ 
    path('create-menu-type', views.ListCreateMenuTypeAPIView.as_view()),
    path('menu-type/<int:pk>/', views.RetrieveUpdateDestroyMenuTypeAPIView.as_view(), name='get_delete_update_menu_type'),


    path('create-menu', views.ListCreateMenuAPIView.as_view()),
    path('menu/<int:pk>/', views.RetrieveUpdateDestroyMenuAPIView.as_view(), name='get_delete_update_menu'),
    path('create-page', views.ListCreatePageAPIView.as_view()),
    path('page/<int:pk>/', views.RetrieveUpdateDestroyPageAPIView.as_view(), name='get_delete_update_page'),
    path('create-icon-section', views.ListCreateSubPageAPIView.as_view()),
    path('sub-page/<int:pk>/', views.RetrieveUpdateDestroySubSectionAPIView.as_view(), name='get_delete_update_page'),

    path('infox-ai-engine', views.ListInfoxAPIView.as_view()),
    path('imagex-ai-engine', views.ListImagexAPIView.as_view()),
    path('create-usecase-category', views.ListCreateUseCaseCategoryAPIView.as_view()),
    path('create-usecase', views.ListCreateUseCaseAPIView.as_view()),
    path('usecase-detail/<int:pk>/', views.RetrieveUpdateDestroyUseCaseAPIView.as_view(), name='get_delete_update_usecase'),
    path('globel-search', views.ListGlobelSearchView.as_view()),



]
