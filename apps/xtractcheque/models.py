from django.db import models
from apps.userpanel.models import AppModule,SwooshUser
import os

# Create your models here.


class ExtractChequeFileUploadModel(models.Model):
    
    module = models.ForeignKey(AppModule, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(SwooshUser, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=550, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file= models.FileField(upload_to='media/document/cheque/',default=None,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    status = models.IntegerField(default=1)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        db_table = "extract_cheque_file"

    
    