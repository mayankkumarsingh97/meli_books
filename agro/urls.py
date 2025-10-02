from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'agro'

router = DefaultRouter()

##
router.register('product',views.AgroProductsApi)
router.register('category',views.AgroCategoryListApi)
router.register('posts',views.AgroPostsApi)
router.register('videos',views.AgroVediosApi)
##
##
urlpatterns = [
    path("api/v1/agro/",include(router.urls)),
]