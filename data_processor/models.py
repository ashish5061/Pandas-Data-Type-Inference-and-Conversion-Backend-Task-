from django.db import models

class ProcessedData(models.Model):
    # Define your fields based on what you want to store
    column_name = models.CharField(max_length=100)
    data_type = models.CharField(max_length=100)
    # Add more fields as needed
