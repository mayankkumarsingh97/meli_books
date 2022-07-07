from rest_framework import serializers
from .models import *

class HomeBanner_seri(serializers.ModelSerializer):
    class Meta:
        model=HomeBanner
        fields=['id','bannername','first_banner',
        'first_banner_heading','first_banner_paragraph',
        'second_banner','second_banner_heading','second_banner_paragraph',
        'third_banner','third_banner_heading','third_banner_paragraph']


class HomePageFirstContent_seri(serializers.ModelSerializer):
    class Meta:
        model=HomePageFirstContent
        fields=[
            'id',
            'contentname',
            'heading',
             'paragraph',
            'first_img',
             'second_img',
            'second_heading',
             'second_paragraph',
            'third_paragraph',
            'fourth_paragraph',
            'left_img'
        ]


# HomePageSecondContent HomePageSecondContent

class HomePageSecondContent_seri(serializers.ModelSerializer):
    class Meta:
        model=HomePageSecondContent
        fields=[
            'id',
            'contentname',
            'heading',
            'small_heading',
            'paragraph',
            'left_img',
            'point_1',
            'point_2',
            'point_3',
            'point_4',
            'point_5',
            'point_6',
            'point_7',
            'second_small_heading',
            'second_paragraph',
            'right_img',
            'second_point_1',
            'second_point_2',
            'second_point_3',
            'second_point_4',
            'second_point_5',
            'second_point_6',
            'second_point_7',
            'second_point_8',
            'second_point_9',
            'second_point_10',
            
        ]

class AboutBanner_seri(serializers.ModelSerializer):
    class Meta:
        model=AboutBanner
        fields=['id','bannername','about_banner']      


#AboutPageFirstContent_seri AboutPageFirstContent_seri

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


# AboutPageSecondContent_seri AboutPageSecondContent_seri

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


# AboutPageFourthContent_seri AboutPageFourthContent_seri

class AboutPageFourthContent_seri(serializers.ModelSerializer):
    class Meta:
        model=AboutPageFourthContent
        fields=[
            'id','contentname','heading','paragraph',
            'img_1','img_2','img_3',"img_4",'img_5','link_1',
            'link_2','link_3','link_4','link_5',
        ]


# ContactBanner_seri ContactBanner_seri ContactBanner_seri
class ContactBanner_seri(serializers.ModelSerializer):
    class Meta:
        model=ContactBanner
        fields=[
            'id',
            'bannername',
            'contact_banner'
        ]



# ContactPage_seri ContactPage_seri ContactPage_seri

class ContactPage_seri(serializers.ModelSerializer):
    class Meta:
        model=ContactPage
        fields=[
            'id','address','marketing_phone','marketing_email',
            'production_phone','production_email'
        ]


class socialmedia_seri(serializers.ModelSerializer):
    class Meta:
        model=socialmedia
        fields=[
            'id','social','facebook','instagram','youtube','twitter'
        ]

class ebooks_seri(serializers.ModelSerializer):
    class Meta:
        model=ebooks
        fields=[
            'id','name','ebook'
        ]        


class catalouge_seri(serializers.ModelSerializer):
    class Meta:
        model=catalouge
        fields=['id','cat','cat_pdf']    


# contactus_seri contactus_seri contactus_seri contactus_seri

class contactus_seri(serializers.ModelSerializer):
    class Meta:
        model=Contactus
        fields=[
            'name','email','phone','message'
        ]