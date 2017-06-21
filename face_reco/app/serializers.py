from app.models import Faces
from rest_framework import serializers


class FacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faces
        fields = '__all__'
