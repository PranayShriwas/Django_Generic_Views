from .serializer import clothserializer
from .models import Cloths
from rest_framework import generics


class clothcreateapi(generics.CreateAPIView):
    queryset = Cloths.objects.all()
    serializer_class = clothserializer


class clothgeteapi(generics.ListAPIView):
    queryset = Cloths.objects.all()
    serializer_class = clothserializer


class clothupdateapi(generics.UpdateAPIView):
    queryset = Cloths.objects.all()
    serializer_class = clothserializer


class clothdeleteapi(generics.DestroyAPIView):
    queryset = Cloths.objects.all()
    serializer_class = clothserializer


class clothreterive(generics.RetrieveAPIView):
    queryset = Cloths.objects.all()
    serializer_class = clothserializer
