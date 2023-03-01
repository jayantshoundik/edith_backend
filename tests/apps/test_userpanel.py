from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *
from django.db import models, transaction


class RegisterSerializer(serializers.ModelSerializer):
  role =  serializers.CharField(
        required=True,
        label="Role"
    )
  class Meta:
    model = SwooshUser
    fields = ('id', 'email', 'first_name', 'last_name', 'password','mobile_no','role','ps_id')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    if validated_data['email'] is not None:
      user = SwooshUser.objects.create_user(email=validated_data['email'],mobile_no=validated_data['mobile_no'],first_name=validated_data['first_name'],last_name = validated_data['last_name'], 
      password=validated_data['password'],ps_id=validated_data['ps_id'])
      
      role = Role.objects.filter(role = validated_data['role'])
      if role.count() == 1 :
        userrole = UserRole.objects.create(user = user,role = role.first())
      
      return user
    else:
      user = SwooshUser.objects.create_user(email=validated_data['email'],mobile_no=validated_data['mobile_no'],first_name=validated_data['first_name'],last_name = validated_data['last_name'],
       password=validated_data['password'],ps_id=validated_data['ps_id'])
      return user
class SwooshUserSerializer(serializers.ModelSerializer):
   
    class Meta(object):
        model = SwooshUser
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
   
    class Meta(object):
        model = Role
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    tokens= serializers.CharField(max_length=255, read_only=True)

    class Meta(object):
        model = SwooshUser
        fields = ['email','password','tokens']
    def validate(self, data):
      
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

       
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

     
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

       
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

  
        return user


class AppModuleCategorySerializer(serializers.ModelSerializer):
   
    class Meta(object):
        model = AppModuleCategory
        fields = '__all__'

class AppModuleSerializer(serializers.ModelSerializer):
   
    class Meta(object):
        model = AppModule
        fields = '__all__'

class AppModulePermissionSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = AppModulePermission
        fields = '__all__'

class AppModuleWisePermissionListSerializer(serializers.ModelSerializer):
    module_permissions = serializers.SerializerMethodField()
    class Meta(object):
        model = AppModule
        fields = '__all__'
    def get_module_permissions(self,obj):
        module_permission = AppModulePermission.objects.filter(module = obj)
        return AppModulePermissionSerializer(module_permission,many=True).data


class CustomAppModulePermissionSerializer(serializers.Serializer):
    id=serializers.IntegerField(required=True)
    module_permisson_name = serializers.CharField(required=True)


class CustomAppUserSerializer(serializers.Serializer):
    id=serializers.IntegerField(required=True)
    ps_id = serializers.CharField(required=True)


class UserGroupPermissionSerializer(serializers.ModelSerializer):
    permissions = CustomAppModulePermissionSerializer(many=True,write_only=True)
    users = CustomAppModulePermissionSerializer(many=True,write_only=True)
 
    class Meta(object):
        model = BaseGroup
        fields = ['id','group_name','permissions','users']
    @transaction.atomic
    def create(self, validated_data):
        if 'permissions' in validated_data.keys():
            permissions = validated_data.pop('permissions')
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
        
        if 'users' in validated_data.keys():
            members = validated_data.pop('users')
        if members is not None:
            members_ids = [ member['id'] for member in members ]
            perm_user_obj = SwooshUser.objects.filter(id__in = members_ids)
         
            basegroupmember= GroupMember.objects.get_or_create(
                        base_group=base_group_created
                    )
            
            basegroupmember.user.add(*perm_user_obj)
            
        return base_group_created

class UserProfileListSerializer(serializers.ModelSerializer):
 
    class Meta(object):
        model = BaseGroupPermissions
        fields = '__all__'
    

    
