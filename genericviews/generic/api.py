from .serializer import GameSerializer
from .models import Game
from rest_framework import generics


class GameCreateApi(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameGetApi(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameUpdateApi(generics.UpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDelteApi(generics.DestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameReteriveApi(generics.RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
