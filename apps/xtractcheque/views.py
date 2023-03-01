from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.permissions import *
from .models import *
from apps.userpanel.permissions import *
from .serializers import *
from rest_framework import generics, status,views
from rest_framework.response import Response
from rest_framework import filters
from apps.userpanel.paginations import SwooshPagination


# Create your views here.


class FileUploadExtractChequeAPIView(ListCreateAPIView):
    serializer_class = FileUploadExtractChequeSerializer
    queryset = ExtractChequeFileUploadModel.objects.all()
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        queryset = ExtractChequeFileUploadModel.objects.filter(user=self.request.user)
        
        return queryset

    def post(self, request):
        try:
            
            serializer = self.serializer_class(data=request.data,context={'request': request})
            if serializer.is_valid(raise_exception=False):
                serializer.save()
                data = serializer.data
                context = {'status': True,'data':data, 'message': 'Successfully Cheque Uploaded'}
                return Response(context, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_200_OK)
        except Exception as e:
            error = {'status': False, 'error':{'message': ["Something Went Wrong"+str(e)] if len(e.args) > 0 else 'Unknown Error'}}
            return Response(error, status=status.HTTP_200_OK)

class ListFileUploadExtractChequeAPIView(ListAPIView):
    serializer_class = FileUploadExtractChequeSerializer
    queryset = ExtractChequeFileUploadModel.objects.all()
    permission_classes = [AllowAny,]
    pagination_class = SwooshPagination