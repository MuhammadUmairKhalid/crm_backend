from django.urls import path,include
from api.views import Login,FormDataViewSet,validatorformViewSet,ChangePasswordView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("formdata",FormDataViewSet,basename="formdata")
router.register("get-forms",validatorformViewSet,basename="get-forms")

urlpatterns = [
   path("login/",Login.as_view()),
   path('update_password',ChangePasswordView.as_view()),
   path("",include(router.urls))
]
