import os
import pandas as pd
from django.conf import settings
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
import numpy as np
from rest_framework.response import Response
from .utils import process_file
from .serializers import FileUploadSerializer, OverrideDataTypeSerializer

@api_view(['POST'])
def upload_file(request):
    serializer = FileUploadSerializer(data=request.data)  # Use the serializer

    if serializer.is_valid():  # Validate the data
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()  # Initializes file storage
        filename = fs.save(uploaded_file.name, uploaded_file)  # Save the file

        # Get the correct file path
        file_path = os.path.join(settings.MEDIA_ROOT, filename)

        response = process_file(file_path, None, None)
        return response

    return Response(serializer.errors, status=400)  # Return validation errors


@api_view(['POST'])
def overrideDataType(request):
    serializer = OverrideDataTypeSerializer(data=request.data)  # Use the serializer

    if serializer.is_valid():  # Validate the data
        column = serializer.validated_data['column']
        data_type = serializer.validated_data['dataType']
        file_path = serializer.validated_data['filePath']

        response = process_file(file_path, column, data_type)
        return response

    return Response(serializer.errors, status=400)  # Return validation errors
