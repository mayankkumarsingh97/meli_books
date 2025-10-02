from .models import *
from .serializers import *
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from .filters import AgricultureImplementFilter
##        
####################################################################
####################################################################
##
class AgroProductsApi(viewsets.ModelViewSet):
    """
    API end point that allow you to Add , Update and Delete Products and its Related Fields.
    """
    queryset=AgricultureImplement.objects.all()
    serializer_class=AgroProductsSeri
    permission_classes= [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AgricultureImplementFilter
    ##
    ####
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        ##
        #####
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success",
            "error": False,
            "data": serializer.data,
            "meta": {
            "timestamp": timezone.now(),
            "version": "v1"
        }}, status=status.HTTP_200_OK)
        
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()  
        serializer = self.get_serializer(instance)
        ##
        #####
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success",
            "error": False,
            "data": [serializer.data],
            "meta": {
            "timestamp": timezone.now(),
            "version": "v1"
        }
        }, status=status.HTTP_200_OK)    

##        
####################################################################
####################################################################
##
class AgroCategoryListApi(viewsets.ModelViewSet):
    """
    API end point that allow you to Add , Update and Delete Products and its Related Fields.
    """
    queryset=ImplementCategory.objects.all()
    serializer_class=AgroCategoryListSeri
    permission_classes= [IsAuthenticated]
    ##
    ####
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        ##
        #####
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success",
            "error": False,
            "data": [serializer.data],
            "meta": {
            "timestamp": timezone.now(),
            "version": "v1"
        }}, status=status.HTTP_200_OK)
        
        
##        
####################################################################
####################################################################
##
class AgroPostsApi(viewsets.ModelViewSet):
    """
    API end point that allow you to Add , Update and Delete Posts and its Related Fields.
    """
    queryset=Blog.objects.all()
    serializer_class=AgroPostSeri
    permission_classes= [IsAuthenticated]
    ##
    ####
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        ##
        #####
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success",
            "error": False,
            "data": [serializer.data],
            "meta": {
            "timestamp": timezone.now(),
            "version": "v1"
        }}, status=status.HTTP_200_OK)        
        
        

##        
####################################################################
####################################################################
##
class AgroVediosApi(viewsets.ModelViewSet):
    """
    API end point that allow you to Add , Update and Delete Vedios and its Related Fields.
    """
    queryset=ProductVideo.objects.all()
    serializer_class=AgroVediosSeri
    permission_classes= [IsAuthenticated]
    ##
    ####
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        ##
        #####
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success",
            "error": False,
            "data": [serializer.data],
            "meta": {
            "timestamp": timezone.now(),
            "version": "v1"
        }}, status=status.HTTP_200_OK)       





    
            