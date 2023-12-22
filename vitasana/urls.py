
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from vitasana.views import index,BasicInfoViewSet,PhysicalProfileViewSet,MedicalProfileViewSet,HabitsInfoViewSet

router = routers.DefaultRouter()
router.register(r'basicinfo',BasicInfoViewSet)
router.register(r'physicalprofile',PhysicalProfileViewSet)
router.register(r'medicalprofile',MedicalProfileViewSet)
router.register(r'habitinfo',HabitsInfoViewSet)

urlpatterns = [
   
    path('index/', index, name="index"),
    path('',include(router.urls))

]