from django.db.models.query_utils import Q
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.permissions import *  
from .models import *
from .serializers import *
from rest_framework.generics import *
from apps.userpanel.paginations import SwooshPagination
from rest_framework.generics import GenericAPIView
from django.conf import settings
import requests
from rest_framework_simplejwt.tokens import RefreshToken


class AdminRegisterationAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=False):
                serializer.save()
                context = {'status': True,'message': 'Successfully Register'}
                return Response(context, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_200_OK)
        except Exception as e:
            error = {'status': False, 'error':{'message': ["Something Went Wrong"+str(e)] if len(e.args) > 0 else 'Unknown Error'}}
            return Response(error, status=status.HTTP_200_OK)

class RoleCreateAPIView(generics.ListCreateAPIView):

    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    def get_queryset(self):
        queryset = Role.objects.all()
        return queryset

class LoginAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    def post(self, request):
        try:
            print(request.data)
            url = 'http://swoosh-dev-infox.apps.swoosh-np.ocp.dev.net/api/v1/infox/user/authentication'
            payload = {
                "username": request.data["username"],
                "password":request.data["password"]
            }
            headers={ 'Authorization': 'eyJ1c2VyX2lkljoiMTYwMzUzNClslmV4cCl6MTYwODI3MDkxNn0' }
            response = requests.post(url, json = payload,headers=headers)
            if response:
                if SwooshUser.objects.filter(ps_id= payload["username"]).exists():
                    user = SwooshUser.objects.get(ps_id=payload["username"])    
                else:
                    user = SwooshUser.objects.create(ps_id= payload["username"],password=payload["password"])    
                refresh = RefreshToken.for_user(user)
                user_details = {}
                user_details['name'] = "%s %s" % ( user.first_name, user.last_name)
                user_details['ps_id'] = user.ps_id
                user_details['access_token'] = str(refresh.access_token)
                user_details['refresh_token'] = str(refresh)
                msg = {'status': True, 'data': user_details}
                return Response(msg, status=status.HTTP_200_OK)
            error = {'status': False, 'error':{'message': ["Invalid Credentials"] }}
            return Response(error, status=status.HTTP_200_OK)
        except Exception as e:
                error = {'status': False, 'error':{'message': ["Something Went Wrong"+str(e)] if len(e.args) > 0 else 'Unknown Error'}}
                return Response(error, status=status.HTTP_200_OK)

        
'''
Module Permissions Create and list

'''
class CreateModuleAPIView(generics.ListCreateAPIView):

    serializer_class = AppModuleSerializer
    queryset = AppModule.objects.all()
    def get_queryset(self):
        queryset = AppModule.objects.all()
        return queryset

class CreateModuleCategoryAPIView(generics.ListCreateAPIView):

    serializer_class = AppModuleCategorySerializer
    queryset = AppModuleCategory.objects.all()
    def get_queryset(self):
        queryset = AppModuleCategory.objects.all()
        return queryset

'''
Create Module Permission  and Lists 
'''
class CreateModulePermissionAPIView(generics.ListCreateAPIView):

    serializer_class = AppModulePermissionSerializer
    queryset = AppModulePermission.objects.all()
    def get_queryset(self):
        queryset = AppModulePermission.objects.all()
        return queryset

'''
Module wise Permission list

'''
class CreateModulePermissionListAPIView(generics.ListAPIView):
    pagination_class = SwooshPagination
    serializer_class = AppModuleWisePermissionListSerializer
    queryset = AppModule.objects.all()
    def get_queryset(self):
        queryset = AppModule.objects.all()
        return queryset

'''
Create Module Permission  and Lists 
'''
class CreateUserProfileAPIView(generics.CreateAPIView):

    serializer_class = UserGroupPermissionSerializer
    queryset = BaseGroup.objects.all()
    def get_queryset(self):
        queryset = BaseGroup.objects.all()
        return queryset

class UserProfileListAPIView(generics.ListAPIView):

    serializer_class = UserProfileListSerializer
    queryset = BaseGroupPermissions.objects.all()
    def get_queryset(self):
        queryset = BaseGroupPermissions.objects.all()
        return queryset
    

class RetrieveUpdateModuleAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AppModuleSerializer
    queryset = AppModule.objects.all()
    permission_classes = [AllowAny,]


class AssignGroupMemberPermissionAPIView(generics.CreateAPIView):

    serializer_class = UserGroupPermissionSerializer
    queryset = BaseGroup.objects.all()
    def get_queryset(self):
        queryset = BaseGroup.objects.all()
        return queryset
    
    def post(self, request):
        try:
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=False):
                serializer.save()
                data = serializer.data
                context = {'status': True,'data':data, 'message': 'Successfully SubPage Added'}
                return Response(context, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_200_OK)
        except Exception as e:
            error = {'status': False, 'error':{'message': ["Something Went Wrong"+str(e)] if len(e.args) > 0 else 'Unknown Error'}}
            return Response(error, status=status.HTTP_200_OK)