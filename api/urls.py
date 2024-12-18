from django.urls import path,include
from api.views import Login,FormDataViewSet,validatorformViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("formdata",FormDataViewSet,basename="formdata")
router.register("get-forms",validatorformViewSet,basename="get-forms")

urlpatterns = [
   path("login/",Login.as_view()),
   path("",include(router.urls))
]
