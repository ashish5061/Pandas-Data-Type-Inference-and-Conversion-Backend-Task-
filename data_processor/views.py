import os
import pandas as pd
from django.conf import settings
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
import numpy as np
from rest_framework.response import Response
from dateutil import parser
from .utils import process_file

@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST' and request.FILES:
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()  # Initializes file storage
        filename = fs.save(uploaded_file.name, uploaded_file)  # Save the file

        # Get the correct file path
        file_path = os.path.join(settings.MEDIA_ROOT, filename)

        response = process_file(file_path, None, None)

        return response

    return JsonResponse({'error': 'No file uploaded'}, status=400)

@api_view(['POST'])
def overrideDataType(request):
    if request.method == 'POST' and request.body:
        column = request.data.get('column')
        data_type = request.data.get('dataType')
        file_path = request.data.get('filePath')

        response = process_file(file_path, column, data_type)

        return response

    return JsonResponse({'error': 'Something went wrong'}, status=400)
