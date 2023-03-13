import pandas as pd

from django.http import HttpResponse
from django.core import serializers

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from . serializer import FileSerializer, InfoModelSerializer, FilterInfoSerializer
from . models import InfoModel

class DataCreateView(generics.CreateAPIView):
    serializer_class = FileSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['uploaded_file']
        reader = pd.read_csv(file)
        print(reader)
        rows = reader.iterrows()
        
        data =[
            InfoModel(
                image_name = row['image_name'],
                objects_detected = row['objects_detected'],
                timestamp = row['timestamp']
            )
            for row in rows
        ]
        print(data)
        InfoModel.objects.bulk_create(data)
        return Response({"msg":"Successfully Uploaded!"}, status.HTTP_201_CREATED)


class FetchInfoDetectorsView(generics.ListCreateAPIView):
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return FilterInfoSerializer
        return InfoModelSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            start_date = serializer.validated_data['start_date']
            end_date = serializer.validated_data['end_date']
            
            queryset = InfoModel.objects.filter(timestamp__range=(start_date,end_date))
        
            dt = serializers.serialize('json', queryset)
                
            return HttpResponse(dt, content_type="application/json")
        else:
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        
    def get_queryset(self):
        queryset = InfoModel.objects.all()
        return queryset