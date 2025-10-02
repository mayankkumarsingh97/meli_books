from rest_framework import serializers
from .models import *

class AgroSubCategorySeri(serializers.ModelSerializer):
    class Meta:
        model=ImplementSubCategory
        fields = ['name']

class AgroCategoryListSeri(serializers.ModelSerializer):
    class Meta:
        model=ImplementCategory
        fields = ['name']     


class AgroProductsSeri(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    subcategory = serializers.CharField(source='subcategory.name', read_only=True)
    class Meta:
        model=AgricultureImplement
        fields = '__all__'
        
class AgroPostSeri(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields = '__all__'     
        
        
        
class StateSerializer(serializers.Serializer):
   
    name = serializers.CharField(max_length=100)
    

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Snippet.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance        
    
class AgroVediosSeri(serializers.ModelSerializer):
    class Meta:
        model=ProductVideo
        fields = '__all__'       