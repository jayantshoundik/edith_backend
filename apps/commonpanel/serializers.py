from rest_framework import serializers
from apps.adminpanel.models import *

class CommonMenuSerializer(serializers.ModelSerializer):
   
    class Meta(object):
        model = SwooshMenu
        fields = '__all__'

class CommonPageSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = SwooshPage
        fields = '__all__'


class HomePageSerializer(serializers.ModelSerializer):
    header_menus = serializers.SerializerMethodField()
    banner = serializers.SerializerMethodField()
    footer1_menus = serializers.SerializerMethodField()
    footer2_menus = serializers.SerializerMethodField()
    footer3_menus = serializers.SerializerMethodField()
    footer4_menus = serializers.SerializerMethodField()
    page_section = serializers.SerializerMethodField()

    class Meta(object):
        model = SwooshPage
        fields = ['header_menus','banner','footer1_menus','footer2_menus','footer3_menus','footer4_menus','page_section']
    
    def get_header_menus(self,obj):
        queryset = SwooshMenu.objects.filter(menu_type__type_name='header',is_active = True)
        if queryset.exists():
            return CommonMenuSerializer(queryset,many=True).data
        return None

    def get_banner(self,obj):
        queryset = SwooshPage.objects.filter(menu_type__type_name='banner',is_active = True)
        if queryset.exists():
            return CommonPageSerializer(queryset,many=True).data
        return None

    def get_footer1_menus(self,obj):
        queryset = SwooshMenu.objects.filter(menu_type__type_name='footer1',is_active = True)
        if queryset.exists():
            return CommonMenuSerializer(queryset,many=True).data
        return None
    
    def get_footer2_menus(self,obj):
        queryset = SwooshMenu.objects.filter(menu_type__type_name='footer2',is_active = True)
        if queryset.exists():
            return CommonMenuSerializer(queryset,many=True).data
        return None
    
    def get_footer3_menus(self,obj):
        queryset = SwooshMenu.objects.filter(menu_type__type_name='footer3',is_active = True)
        if queryset.exists():
            return CommonMenuSerializer(queryset,many=True).data
        return None
    
    def get_footer4_menus(self,obj):
        queryset = SwooshMenu.objects.filter(menu_type__type_name='footer4',is_active = True)
        if queryset.exists():
            return CommonMenuSerializer(queryset,many=True).data
        return None
    
    def get_page_section(self,obj):
        queryset = SwooshPage.objects.all()
        if queryset.exists():
            return CommonPageSerializer(queryset,many=True).data
        return None
