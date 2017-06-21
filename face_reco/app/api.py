from app.models import Faces
from app.serializers import FacesSerializer
from rest_framework import generics


class FacesList(generics.ListCreateAPIView):
    queryset = Faces.objects.all()
    serializer_class = FacesSerializer

    # def post(self, request, *args, **kwargs):
    #     import pdb
    #     pdb.set_trace()
    #     return self.create(request, *args, **kwargs)
