
####################################################################
####################################################################
##
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.authentication import BasicAuthentication,SessionAuthentication

from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly

class ProfileApi(viewsets.ModelViewSet):
    """
    API end point that allow you to Add , Update and Delete Profile API and its Related Fields.
    """
    queryset=Profile.objects.all()
    serializer_class=Profile_seri
    # authentication_classes= [BasicAuthentication]
    # permission_classes= [IsAuthenticated]
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