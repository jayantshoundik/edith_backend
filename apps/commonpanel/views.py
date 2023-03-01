from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.permissions import *
from .models import *
from apps.userpanel.permissions import *
from .serializers import *
from rest_framework import generics, status,views
from rest_framework.response import Response


# Create your views here.

"""
Get User Profile API View
"""
class HomePageAPIView(views.APIView):
        permission_classes = (AllowAny,)
        serializer_class = HomePageSerializer

        def get(self, request):
            try :
                queryset =SwooshPage.objects.all()
                serializer = self.serializer_class(queryset, many=False)
                errormsg = 'ConfirmSchoolByUserAPIView():error==>' + str(serializer)
                
                data = serializer.data
                msg = {'status': True, 'data': data}
                return Response(msg, status=status.HTTP_200_OK)
            except Exception as e:
                error = {'status': False, 'error':{'message': ["Something Went Wrong"+str(e)] if len(e.args) > 0 else 'Unknown Error'}}
                return Response(error, status=status.HTTP_200_OK)
            

    
