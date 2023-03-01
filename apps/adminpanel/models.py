from django.db import models

# Create your models here.


class SwooshMenuType(models.Model):
    type_name =  models.CharField(max_length=50, blank=False, null=False)
    title = models.CharField(max_length=550, blank=True, null=True)
    description = models.CharField(max_length=550, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "swoosh_menu_type"


        

class SwooshMenu(models.Model):
    menu_type = models.ForeignKey(SwooshMenuType, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=550, blank=True, null=True)
    link = models.CharField(max_length=550, blank=True, null=True)
    ordering_value = models.IntegerField(default=0)
    image_field = models.FileField(upload_to="media/document/",default=None,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "swoosh_menu"




class SwooshPage(models.Model):
    menu_type = models.ForeignKey(SwooshMenuType, on_delete=models.SET_NULL, null=True,blank=False)
    title = models.CharField(max_length=550, blank=True, null=True)
    link = models.CharField(max_length=550, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image_field = models.FileField(upload_to="media/document/",default=None,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "swoosh_page"

class SwooshSubSectionPage(models.Model):
    section = models.ForeignKey(SwooshPage, on_delete=models.SET_NULL, null=True,blank=False)
    title = models.CharField(max_length=550, blank=True, null=True)
    link = models.CharField(max_length=550, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image_field = models.FileField(upload_to="media/document/",default=None,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "swoosh_sub_page"

class SwooshUseCaseCategory(models.Model):
    name = models.CharField(max_length=550, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "swoosh_usecase_category"

        
class SwooshUseCase(models.Model):
    category = models.ForeignKey(SwooshUseCaseCategory, on_delete=models.SET_NULL, null=True,blank=False)
    title = models.CharField(max_length=550, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    file= models.FileField(upload_to="media/document/",default=None,blank=True, null=True)
    working_hour =  models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "swoosh_usecase"

    



