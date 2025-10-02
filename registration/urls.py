from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from . import views



app_name = 'registration'

router = DefaultRouter()
##

router.register('profile',views.ProfileApi)
##
##
urlpatterns = [
    path("api/v1/",include(router.urls)),
]