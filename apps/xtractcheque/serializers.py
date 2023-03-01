from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *
from django.db import models, transaction


class FileUploadExtractChequeSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True)
    class Meta:
        model = ExtractChequeFileUploadModel
        fields = ['file','module']

    def create(self, validated_data):
        xtract_cheque = ExtractChequeFileUploadModel.objects.create(module=validated_data['module'])
        experiment_id="experiment_"+self.context['request'].user.ps_id
        print("kmkfdjskjkfkdks",experiment_id)
        upload_dir = os.path.join('media/document/cheque/',experiment_id)
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        snap_shot_id = "snap_shot_"+self.context['request'].user.ps_id
        snap_dir = os.path.join(upload_dir,snap_shot_id)
        if not os.path.exists(snap_dir):
            os.makedirs(snap_dir)
        name, extension = os.path.splitext(validated_data['file'].name)
        cheque_number_id = 'Cheque_'+str(xtract_cheque.id)+extension
        file_path = os.path.join(snap_dir, cheque_number_id)
        with open(file_path, 'wb+') as destination:
            for chunk in validated_data['file'].chunks():
                destination.write(chunk)
        if xtract_cheque:
            xtract_cheque.file =file_path
            xtract_cheque.user = self.context['request'].user
            xtract_cheque.save()
        
        return xtract_cheque

   
