from rest_framework import serializers

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

class OverrideDataTypeSerializer(serializers.Serializer):
    column = serializers.CharField(required=True)
    dataType = serializers.CharField(required=True)
    filePath = serializers.CharField(required=True)
