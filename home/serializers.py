from rest_framework import serializers
from .models import *

class HomeBanner_seri(serializers.ModelSerializer):
    class Meta:
        model=HomeBanner
        fields = '__all__'


class HomePageFirstContent_seri(serializers.ModelSerializer):
    class Meta:
        model=HomePageFirstContent
        fields= '__all__'

##
# HomePageSecondContent 
##
class HomePageSecondContent_seri(serializers.ModelSerializer):
    class Meta:
        model=HomePageSecondContent
        fields='__all__'

class AboutBanner_seri(serializers.ModelSerializer):
    class Meta:
        model=AboutBanner
        fields=['id','bannername','about_banner']      

##
#AboutPageFirstContent_seri 
##
class AboutPageFirstContent_seri(serializers.ModelSerializer):
    class Meta:
        model=AboutPageFirstContent
        fields=[
            'id',
            'contentname','heading','paragraph',
            'first_small_heading','first_paragraph',
            'second_small_heading','second_paragraph',
            'third_small_heading','third_paragraph'
        ]

##
# AboutPageSecondContent_seri 
##
class AboutPageSecondContent_seri(serializers.ModelSerializer):
    class Meta:
        model=AboutPageSecondContent
        fields=[
            'id','contentname','heading','paragraph',
            'first_small_heading','first_paragraph',
            'second_small_heading','second_paragraph',
            'third_small_heading','third_paragraph',
            'left_img','img_heading','img_paragraph'
        ]

##
# AboutPage Third Content
##
class AboutPageThirdContent_seri(serializers.ModelSerializer):
    class Meta:
        model=AboutPageThirdContent
        fields=[
            'id','contentname','first_small_heading',
            'first_paragraph','second_small_heading',
            'second_paragraph','third_small_heading',
            'third_paragraph','right_img','img_heading',
            'img_paragraph'
        ]

##
# AboutPageFourthContent_seri 
##
class AboutPageFourthContent_seri(serializers.ModelSerializer):
    class Meta:
        model=AboutPageFourthContent
        fields=[
            'id','contentname','heading','paragraph',
            'img_1','img_2','img_3',"img_4",'img_5','link_1',
            'link_2','link_3','link_4','link_5',
        ]

##
# ContactBanner_seri 
##
class ContactBanner_seri(serializers.ModelSerializer):
    class Meta:
        model=ContactBanner
        fields=[
            'id',
            'bannername',
            'contact_banner'
        ]



###
# ContactPage_seri
###
class ContactPage_seri(serializers.ModelSerializer):
    class Meta:
        model=ContactPage
        fields=[
            'id','address','marketing_phone','marketing_email',
            'production_phone','production_email'
        ]

###
# socialmedia_seri
###
class socialmedia_seri(serializers.ModelSerializer):
    class Meta:
        model=socialmedia
        fields=[
            'id','social','facebook','instagram','youtube','twitter'
        ]
###
# ebooks_seri
###
class ebooks_seri(serializers.ModelSerializer):
    class Meta:
        model=ebooks
        fields=[
            'id','name','ebook'
        ]        

###
# catalouge_seri
###
class catalouge_seri(serializers.ModelSerializer):
    class Meta:
        model=catalouge
        fields=['id','cat','cat_pdf']    


# 
###
# contactus_seri
###
class contactus_seri(serializers.ModelSerializer):
    class Meta:
        model=Contactus
        fields=[
            'name','email','phone','message'
        ]