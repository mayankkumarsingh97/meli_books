from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

from . import views

app_name = 'home'

router = DefaultRouter()
router.register('homebanner',views.HomeBannerapi)
router.register('HomePageFirstContent',views.HomePageFirstContentapi)
router.register('HomePageSecondContent',views.HomePageSecondContentapi)
router.register('AboutBanner',views.AboutBannerapi)
router.register('AboutPageFirstContent',views.AboutPageFirstContentapi)
router.register('AboutPageSecondContent',views.AboutPageSecondContentapi)


router.register('AboutPageThirdContent',views.AboutPageThirdContentapi)
router.register('AboutPageFourthContent',views.AboutPageFourthContentapi)

router.register('ContactBanner',views.ContactBannerapi)

router.register('ContactPage',views.ContactPageapi)
router.register('socialmedia',views.socialmediaapi)
router.register('ebooks',views.ebooksapi)
router.register('catalouge',views.catalougeapi)
router.register('Contactus',views.Contactusapi)






urlpatterns = [
    path("api/",include(router.urls)),
    path('', views.landing, name='landing'),
    path('about-us', views.aboutus, name='about-us'),
    path('contact-us', views.contactus, name='contact-us'),
    path('category', views.category, name='category'),
    path('product', views.product, name='product'),
    path('landing1', views.landing1, name='landing1'),
    path('landing2', views.landing2, name='landing2'),
]
