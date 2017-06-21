from app.models import Faces
from app.serializers import FacesSerializer
from rest_framework import generics


class FacesList(generics.ListCreateAPIView):
    queryset = Faces.objects.all()
    serializer_class = FacesSerializer
