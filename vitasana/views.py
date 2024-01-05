from django.shortcuts import render
from rest_framework import viewsets
from vitasana.models import BasicInfo,PhysicalProfile,MedicalProfile,HabitsInfo,BasicInfoOp,Vitals,Pathology,AvPariksha,Prescription
from vitasana.serializers import BasinInfoSerializer,PhysicalProfileSerializer,MedicalProfileSerializer,HabitsInfoSerializer,DietPlanSerializer
from vitasana.serializers import BasicInfoOpSerializer,VitalsSerializer,PathologySerializer,AvParikshaSerializer,DietPlan,PrescriptionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
def index(request):
    return render(request,'welcome.html')

#RestApi Views HEALTH ASSESSMENT SYSTEM
#Record based on Mobilenumber


#BaicInfo RestApi Views
class BasicInfoViewSet(viewsets.ModelViewSet):
    queryset = BasicInfo.objects.all()
    serializer_class = BasinInfoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Item deleted successfully."}, status=status.HTTP_200_OK)
    
    
#url:vitasana/basicinfo/patientid/patient
    
    @action(detail=True, methods=['get', 'put'])
    def patient(self, request, pk=None):
        try:
            patient = BasicInfo.objects.get(patientid=pk)
        except BasicInfo.DoesNotExist:
            return Response({'message': 'Patient does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            basic_info_serializer = BasinInfoSerializer(patient, context={'request': request})
            phyprofile = PhysicalProfile.objects.filter(patientid=pk)
            phyprofile_serializer = PhysicalProfileSerializer(phyprofile, many=True, context={'request': request})
            medprofile = MedicalProfile.objects.filter(patientid=pk)
            medprofile_serializer = MedicalProfileSerializer(medprofile, many=True, context={'request': request})
            habitsinfo = HabitsInfo.objects.filter(patientid=pk)
            habitsinfo_serializer = HabitsInfoSerializer(habitsinfo, many=True, context={'request': request})

            return Response({
                'basic_info': basic_info_serializer.data,
                'physical_profile': phyprofile_serializer.data,
                'medical_profile': medprofile_serializer.data,
                'habits_info': habitsinfo_serializer.data,
            })

        elif request.method == 'PUT':
            basic_info_serializer = BasinInfoSerializer(patient, data=request.data.get('basic_info'), partial=True)
            basic_info_serializer.is_valid(raise_exception=True)
            basic_info_serializer.save()

            phyprofile_data = request.data.get('physical_profile')
            phyprofile = PhysicalProfile.objects.filter(patientid=pk)  # Fetch phyprofile queryset
            phyprofile_serializer = PhysicalProfileSerializer(data=phyprofile_data, many=True, partial=True)
            phyprofile_serializer.is_valid(raise_exception=True)
            for index, data in enumerate(phyprofile_data):
                instance = phyprofile[index] if index < len(phyprofile) else None
                phyprofile_serializer.save(patientid=patient, instance=instance)

            medprofile_data = request.data.get('medical_profile')
            medprofile = MedicalProfile.objects.filter(patientid=pk)  # Fetch medprofile queryset
            medprofile_serializer = MedicalProfileSerializer(data=medprofile_data, many=True, partial=True)
            medprofile_serializer.is_valid(raise_exception=True)
            for index, data in enumerate(medprofile_data):
                instance = medprofile[index] if index < len(medprofile) else None
                medprofile_serializer.save(patientid=patient, instance=instance)

            habitsinfo_data = request.data.get('habits_info')
            habitsinfo = HabitsInfo.objects.filter(patientid=pk)  # Fetch habitsinfo queryset
            habitsinfo_serializer = HabitsInfoSerializer(data=habitsinfo_data, many=True, partial=True)
            habitsinfo_serializer.is_valid(raise_exception=True)
            for index, data in enumerate(habitsinfo_data):
                instance = habitsinfo[index] if index < len(habitsinfo) else None
                habitsinfo_serializer.save(patientid=patient, instance=instance)

            return Response({'message': 'Patient information updated successfully.'}, status=status.HTTP_200_OK)

        else:
            return Response({'message': 'Invalid request method. Use GET or PUT.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

#PhysicalProfile RestApi Views
    
    
class PhysicalProfileViewSet(viewsets.ModelViewSet):
    queryset = PhysicalProfile.objects.all()
    serializer_class = PhysicalProfileSerializer

#MedicalProfile RestApi Views
    
class MedicalProfileViewSet(viewsets.ModelViewSet):
    queryset = MedicalProfile.objects.all()
    serializer_class = MedicalProfileSerializer

#HabitsInfo RestApi Views
    
class HabitsInfoViewSet(viewsets.ModelViewSet):
    queryset = HabitsInfo.objects.all()
    serializer_class = HabitsInfoSerializer




#RestApi Views OP ASSESSMENT SYSTEM
    
#BasicInfoOp RestApi Views

class BasicInfoOpViewSet(viewsets.ModelViewSet):
    queryset = BasicInfoOp.objects.all()
    serializer_class = BasicInfoOpSerializer


#Vitals RestApi Views
    
class VitalsViewSet(viewsets.ModelViewSet):
    queryset = Vitals.objects.all()
    serializer_class = VitalsSerializer


#Pathology RestApi Views
    
class PathologyViewSet(viewsets.ModelViewSet):
    queryset = Pathology.objects.all()
    serializer_class = PathologySerializer

#AvPariksha RestApi Views

class AvParikshaViewSet(viewsets.ModelViewSet):
    queryset = AvPariksha.objects.all()
    serializer_class = AvParikshaSerializer

#Prescription  RestApi Views
    
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

#DIET PLAN  RestApi Views
    
class DietPlanViewSet(viewsets.ModelViewSet):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer

