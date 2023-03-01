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


class ListCreateMenuAPIView(ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset = SwooshMenu.objects.all()
    permission_classes = [AllowAny,]

    def post(self, request):
        try:
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=False):
                serializer.save()
                data = serializer.data
                context = {'status': True,'data':data, 'message': 'Successfully Menu Added'}
                return Response(context, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_200_OK)
        except Exception as e:
            error = {'status': False, 'error':{'message': ["Something Went Wrong"+str(e)] if len(e.args) > 0 else 'Unknown Error'}}
            return Response(error, status=status.HTTP_200_OK)


class RetrieveUpdateDestroyMenuAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer
    queryset = SwooshMenu.objects.all()
    permission_classes = [AllowAny,]


class ListCreateSubPageAPIView(ListCreateAPIView):
    serializer_class = SubPageSerializer
    queryset = SwooshSubSectionPage.objects.all()
    permission_classes = [AllowAny,]

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

class ListCreatePageAPIView(ListCreateAPIView):
    serializer_class = PageSerializer
    queryset = SwooshPage.objects.all()
    permission_classes = [AllowAny,]
    pagination_class = SwooshPagination

    def post(self, request):
        try:
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=False):
                serializer.save()
                data = serializer.data
                context = {'status': True,'data':data, 'message': 'Successfully Page Added'}
                return Response(context, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_200_OK)
        except Exception as e:
            error = {'status': False, 'error':{'message': ["Something Went Wrong"+str(e)] if len(e.args) > 0 else 'Unknown Error'}}
            return Response(error, status=status.HTTP_200_OK)


class ListCreateMenuTypeAPIView(ListCreateAPIView):
    serializer_class = MenuTypeSerializer
    queryset = SwooshMenuType.objects.all()
    permission_classes = [AllowAny,]

    def post(self, request):
        try:
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=False):
                serializer.save()
                data = serializer.data
                context = {'status': True,'data':data, 'message': 'Successfully Page Added'}
                return Response(context, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_200_OK)
        except Exception as e:
            error = {'status': False, 'error':{'message': ["Something Went Wrong"+str(e)] if len(e.args) > 0 else 'Unknown Error'}}
            return Response(error, status=status.HTTP_200_OK)


class RetrieveUpdateDestroyPageAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PageSerializer
    queryset = SwooshPage.objects.all()
    permission_classes = [AllowAny,]



class RetrieveUpdateDestroyMenuTypeAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MenuTypeSerializer
    queryset = SwooshMenuType.objects.all()
    permission_classes = [AllowAny,]

class RetrieveUpdateDestroySubSectionAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SubPageSerializer
    queryset = SwooshSubSectionPage.objects.all()
    permission_classes = [AllowAny,]



class ListInfoxAPIView(ListAPIView):
    pagination_class = SwooshPagination
    serializer_class =PageSerializer
    queryset = SwooshPage.objects.filter(menu_type__type_name ='ai_engine_infox')
    permission_classes = [AllowAny,]


class ListImagexAPIView(ListAPIView):
    pagination_class = SwooshPagination
    serializer_class =PageSerializer
    queryset = SwooshPage.objects.filter(menu_type__type_name ='ai_engine_image_x')
    permission_classes = [AllowAny,]



class ListCreateUseCaseCategoryAPIView(ListCreateAPIView):
    serializer_class = UseCaseCategorySerializer
    queryset = SwooshUseCaseCategory.objects.all()
    permission_classes = [AllowAny,]
    pagination_class = SwooshPagination

    def post(self, request):
        try:
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=False):
                serializer.save()
                data = serializer.data
                context = {'status': True,'data':data, 'message': 'Successfully Menu Added'}
                return Response(context, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_200_OK)
        except Exception as e:
            error = {'status': False, 'error':{'message': ["Something Went Wrong"+str(e)] if len(e.args) > 0 else 'Unknown Error'}}
            return Response(error, status=status.HTTP_200_OK)

class ListCreateUseCaseAPIView(ListCreateAPIView):
    search_fields = ['title','category__name','content']
    filter_backends = (filters.SearchFilter,)
    serializer_class = UseCaseSerializer
    pagination_class = SwooshPagination
    permission_classes = [AllowAny,]

    def get_queryset(self):
        query =  self.request.query_params.get('category',None)
        if query:
            itemlist = SwooshUseCase.objects.filter(category__name = query)
        else:
            itemlist = SwooshUseCase.objects.all()
        return itemlist


    def post(self, request):
        try:
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid(raise_exception=False):
                serializer.save()
                data = serializer.data
                context = {'status': True,'data':data, 'message': 'Successfully Menu Added'}
                return Response(context, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_200_OK)
        except Exception as e:
            error = {'status': False, 'error':{'message': ["Something Went Wrong"+str(e)] if len(e.args) > 0 else 'Unknown Error'}}
            return Response(error, status=status.HTTP_200_OK)


class RetrieveUpdateDestroyUseCaseAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UseCaseSerializer
    queryset = SwooshUseCase.objects.all()
    permission_classes = [AllowAny,]


class ListGlobelSearchView(ListAPIView):
    pagination_class = SwooshPagination
    serializer_class =PageSerializer
    queryset = SwooshPage.objects.filter(menu_type__type_name ='ai_engine_image_x')
    permission_classes = [AllowAny,]