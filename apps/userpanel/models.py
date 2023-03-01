from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from rest_framework_simplejwt.tokens import RefreshToken
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail  

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, password, first_name, last_name,**other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, password, first_name, last_name, **other_fields)

    def create_user(self, email, password, first_name, last_name, **other_fields):
        other_fields.setdefault('is_superuser', True)

        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)    
        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')  
          
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name,**other_fields)
        user.set_password(password)
        user.save()
        return user

class Role(models.Model):
    
    role = models.CharField(
        max_length=45,
        default='ADMIN',
        null=False
    )
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "roles"

    def __str__(self):
        return self.role



class SwooshUser(AbstractBaseUser, PermissionsMixin):
    ps_id = models.CharField(blank=False, null=False, unique=True,max_length=8, default=00000000)
    mobile_no = models.CharField(max_length=11, null=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    joining_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_mobile_no_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)   
    address = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=False, blank=False)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    # permissions = jsonfield.JSONField(null=True, blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = "Users"

    def get_full_name(self):
        if not self.first_name and not self.last_name:
            return self.username
        else:
            return "%s %s" % (self.first_name, self.last_name)

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

class UserRole(models.Model):
    user = models.ForeignKey(SwooshUser, on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "user_roles"

class AppModuleCategory(models.Model):
    name = models.CharField(max_length=550, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "app_module_category"

        
class AppModule(models.Model):
    category = models.ForeignKey(AppModuleCategory, on_delete=models.SET_NULL, null=True)
    module = models.CharField(blank=False, null=False, max_length=21,unique=True)
    title = models.CharField(blank=False, null=False, max_length=300 )
    description = models.TextField(blank=True, null=True)
    icon = models.FileField(upload_to="media/document/",default=None,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "app_module"

class AppModulePermission(models.Model):
    module = models.ForeignKey(AppModule, on_delete=models.SET_NULL, null=True)
    module_permisson_name = models.CharField(max_length=550, blank=False, null=False,unique=True)
    module_permisson_description = models.CharField(max_length=550, blank=False, null=False)
    slug = models.SlugField(max_length=100) 
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "app_module_permissions"


class BaseGroup(models.Model):
    group_name = models.CharField(max_length=200,unique=True)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "base_group"

class GroupMember(models.Model):
    base_group = models.ForeignKey(BaseGroup, on_delete=models.SET_NULL, null=True)
    user = models.ManyToManyField(SwooshUser, related_name='group_member')
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "group_member"


class BaseGroupPermissions(models.Model):
    base_group = models.ForeignKey(BaseGroup, on_delete=models.SET_NULL, null=True)
    app_module_permission = models.ManyToManyField(AppModulePermission, related_name='permission_list')
    is_access = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "group_permission"
        

    