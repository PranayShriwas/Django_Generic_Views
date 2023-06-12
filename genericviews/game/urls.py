from django.urls import path, include
from .api import clothcreateapi, clothdeleteapi, clothgeteapi, clothreterive, clothupdateapi
from .models import Cloths

urlpatterns = [
    path('api/create', clothcreateapi.as_view()),
    path('', clothgeteapi.as_view()),
    path('api/<int:pk>', clothupdateapi.as_view()),
    path('api/delete/<int:pk>', clothdeleteapi.as_view()),
    path('api/reterive/<int:pk>', clothreterive.as_view())
]
