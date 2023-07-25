from rest_framework import generics
from .serializer import CerealSerializer
from .models import Cereal

class CerealList(generics.ListCreateAPIView):
    queryset = Cereal.objects.all()
    serializer_class = CerealSerializer

class CerealDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cereal.objects.all()
    serializer_class = CerealSerializer