# from django.shortcuts import render
from django.shortcuts import render
from .models import HomeBanner,HomePageFirstContent,HomePageSecondContent,HomePageSecondContent

from .serializers import *
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly

#
# Create your views here.
#
class HomeBannerapi(viewsets.ModelViewSet):
    """
    API end point that allow you to Add , Update and Delete Home Banner and its Related Fields.
    """
    queryset=HomeBanner.objects.all()
    serializer_class=HomeBanner_seri
    authentication_classes= [SessionAuthentication]
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
            "message": "success!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

##        
####################################################################
####################################################################
##
class HomePageFirstContentapi(viewsets.ModelViewSet):
    """
    API end point that allow you to Add , Update and Delete HomePageFirstContent and its Related Fields.
    """
    queryset=HomePageFirstContent.objects.all()
    serializer_class=HomePageFirstContent_seri
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
##        
####################################################################
####################################################################
##
class HomePageSecondContentapi(viewsets.ModelViewSet):
    queryset=HomePageSecondContent.objects.all()
    serializer_class=HomePageFirstContent_seri
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
##        
####################################################################
####################################################################
##
class AboutBannerapi(viewsets.ModelViewSet):
    queryset=AboutBanner.objects.all()
    serializer_class=AboutBanner_seri
    authentication_classes= [BasicAuthentication]
    permission_classes= [AllowAny]
    ###
    #####
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
##        
####################################################################
####################################################################
##
class AboutPageFirstContentapi(viewsets.ModelViewSet):
    queryset=AboutPageFirstContent.objects.all()
    serializer_class=AboutPageFirstContent_seri
    #
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
##        
####################################################################
####################################################################
##
class AboutPageSecondContentapi(viewsets.ModelViewSet):
    queryset=AboutPageSecondContent.objects.all()
    serializer_class=AboutPageSecondContent_seri
    #
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)


##        
####################################################################
####################################################################
##
class AboutPageThirdContentapi(viewsets.ModelViewSet):
    queryset=AboutPageThirdContent.objects.all()
    serializer_class=AboutPageThirdContent_seri
    #
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

##        
####################################################################
####################################################################
##
class AboutPageFourthContentapi(viewsets.ModelViewSet):
    queryset=AboutPageFourthContent.objects.all()
    serializer_class=AboutPageFourthContent_seri
    #
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
##        
####################################################################
####################################################################
##
class ContactBannerapi(viewsets.ModelViewSet):
    queryset=ContactBanner.objects.all()
    serializer_class=ContactBanner_seri
    #
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
##        
####################################################################
####################################################################
##
class ContactPageapi(viewsets.ModelViewSet):
    queryset=ContactPage.objects.all()
    serializer_class=ContactPage_seri
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
##        
####################################################################
####################################################################
##    

class socialmediaapi(viewsets.ModelViewSet):
    queryset=socialmedia.objects.all()
    serializer_class=socialmedia_seri
    #
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
##
####################################################################
####################################################################
##
class ebooksapi(viewsets.ModelViewSet):
    queryset=ebooks.objects.all()
    serializer_class=ebooks_seri
    #
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
##        
####################################################################
####################################################################
##
class catalougeapi(viewsets.ModelViewSet):
    queryset=catalouge.objects.all()
    serializer_class=catalouge_seri
    #
    #
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)


##        
####################################################################
####################################################################
##
class Contactusapi(viewsets.ModelViewSet):
    queryset=Contactus.objects.all()
    serializer_class=contactus_seri
    #
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status": status.HTTP_200_OK,
            "message": "success!",
            "data": serializer.data
        }, status=status.HTTP_200_OK)



