from django.urls import path
from api.views import Login

urlpatterns = [
   path("login/",Login.as_view())
]
