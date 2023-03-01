from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *
from django.db import models, transaction

class MenuTypeSerializer(serializers.ModelSerializer):
   
    class Meta(object):
        model = SwooshMenuType
        fields = '__all__'

class PageTypeSerializer(serializers.ModelSerializer):
   
    class Meta(object):
        model = SwooshMenuType
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
   
    class Meta(object):
        model = SwooshMenu
        fields = '__all__'

class SubPageSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = SwooshSubSectionPage
        fields = '__all__'

class PageSerializer(serializers.ModelSerializer):
    subsection = serializers.SerializerMethodField()
    class Meta(object):
        model = SwooshPage
        fields = '__all__'
    def get_subsection(self,obj):
        queryset = SwooshSubSectionPage.objects.filter(section = obj)
        return SubPageSerializer(queryset,many=True).data 

class InfoxAIEngineSerializer(serializers.ModelSerializer):
    
 
    class Meta(object):
        model = SwooshSubSectionPage
        fields = '__all__'
    @transaction.atomic
    def create(self, validated_data):
        members = None
        print("fdkjfsdjfkdsjkf",validated_data)
        if 'permissions' in validated_data.keys():
            permissions = validated_data.pop('permissions')
            print(permissions)

        # Create the base group
        base_group_created = BaseGroup.objects.create(**validated_data)

        # Deal with members data
        if permissions is not None:
            res_ids = [ permission['id'] for permission in permissions ]
            perm_obj = AppModulePermission.objects.filter(id__in = res_ids)
            basegrouppermission = BaseGroupPermissions.objects.create(
                        base_group=base_group_created
                    )
            
            basegrouppermission.app_module_permission.add(*perm_obj)
            
        return base_group_created


class UseCaseCategorySerializer(serializers.ModelSerializer):
   
    class Meta(object):
        model = SwooshUseCaseCategory
        fields = '__all__'
class RelatedUseCaseSerializer(serializers.ModelSerializer):
   
    class Meta(object):
        model = SwooshUseCase
        fields = '__all__'

class UseCaseSerializer(serializers.ModelSerializer):
    related_usecase = serializers.SerializerMethodField()
   
    class Meta(object):
        model = SwooshUseCase
        fields = '__all__'
 
    def get_related_usecase(self,obj):
        queryset = SwooshUseCase.objects.filter(category = obj.category).exclude(id = obj.id)
        return RelatedUseCaseSerializer(queryset,many=True).data 