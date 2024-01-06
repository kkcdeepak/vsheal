
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from vitasana.views import index,BasicInfoViewSet,PhysicalProfileViewSet,MedicalProfileViewSet,HabitsInfoViewSet,BasicInfoOpViewSet,VitalsViewSet,PathologyViewSet,AvParikshaViewSet,DietPlanViewSet,PrescriptionViewSet

router = routers.DefaultRouter()
router.register(r'basicinfo',BasicInfoViewSet)
router.register(r'physicalprofile',PhysicalProfileViewSet)
router.register(r'medicalprofile',MedicalProfileViewSet)
router.register(r'habitinfo',HabitsInfoViewSet)
router.register(r'basicinfoop',BasicInfoOpViewSet)
router.register(r'vitals',VitalsViewSet)
router.register(r'pathology',PathologyViewSet)
router.register(r'avpariksha',AvParikshaViewSet)
router.register(r'prescription',PrescriptionViewSet)
router.register(r'dietplan',DietPlanViewSet)


urlpatterns = [
   
    path('index/', index, name="index"),
    path('',include(router.urls)),
    path('patient_records/<str:mobile_number>/',patient_records_mobnumber, name= "patient_records_mobnumber")

]
