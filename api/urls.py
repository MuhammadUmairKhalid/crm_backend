from django.urls import path,include
from api.views import Login,FormDataViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("formdata",FormDataViewSet,basename="formdata")

urlpatterns = [
   path("login/",Login.as_view()),
   path("",include(router.urls))
]
