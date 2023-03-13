from rest_framework import serializers 
from . models import InfoModel

class FileSerializer(serializers.Serializer):
    uploaded_file = serializers.FileField()

class InfoModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InfoModel
        fields = '__all__'

class FilterInfoSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()