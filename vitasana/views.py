from django.shortcuts import render
from rest_framework import viewsets
from vitasana.models import BasicInfo,PhysicalProfile,MedicalProfile,HabitsInfo
from vitasana.serializers import BasinInfoSerializer,PhysicalProfileSerializers,MedicalProfileSerializers,HabitsInfoSerializers
# Create your views here.
def index(request):
    return render(request,'welcome.html')

#RestApi Views HEALTH ASSESSMENT SYSTEM

#BaicInfo RestApi Views
class BasicInfoViewSet(viewsets.ModelViewSet):
    queryset = BasicInfo.objects.all()
    serializer_class = BasinInfoSerializer

#PhysicalProfile RestApi Views
    
    
class PhysicalProfileViewSet(viewsets.ModelViewSet):
    queryset = PhysicalProfile.objects.all()
    serializer_class = PhysicalProfileSerializers

#MedicalProfile RestApi Views
    
class MedicalProfileViewSet(viewsets.ModelViewSet):
    queryset = MedicalProfile.objects.all()
    serializer_class = MedicalProfileSerializers

#HabitsInfo RestApi Views
    
class HabitsInfoViewSet(viewsets.ModelViewSet):
    queryset = HabitsInfo.objects.all()
    serializer_class = HabitsInfoSerializers