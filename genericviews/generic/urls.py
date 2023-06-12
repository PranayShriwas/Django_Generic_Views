from django.urls import path
from .api import GameCreateApi, GameGetApi, GameDelteApi, GameUpdateApi, GameReteriveApi
urlpatterns = [
    path('api/create', GameCreateApi.as_view()),
    path('', GameGetApi.as_view()),
    path('api/<int:pk>', GameUpdateApi.as_view()),
    path('api/delete/<int:pk>', GameDelteApi.as_view()),
    path('api/Reterive/<int:pk>', GameReteriveApi.as_view())
]
