from django.urls import path 
from . import views as v 

urlpatterns = [
    path('api/upload_file',v.DataCreateView.as_view(), name="upload-file"),
    path('api/retrieve_data',v.FetchInfoDetectorsView.as_view(), name="retrieve-data"),
]
