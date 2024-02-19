from rest_framework import serializers
from CrudApp.models import CrudExample

class CrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrudExample
        fields = '__all__'