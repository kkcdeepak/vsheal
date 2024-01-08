from django.shortcuts import render
from rest_framework import viewsets
from vitasana.models import BasicInfo,PhysicalProfile,MedicalProfile,HabitsInfo,BasicInfoOp,Vitals,Pathology,AvPariksha,Prescription,WomenHealth,PersonalDetails_Dosa,PhysicalChar_Dosa,PhysiologicalChar_Dosa,PsychologicalChar_Dosa
from vitasana.serializers import BasinInfoSerializer,PhysicalProfileSerializer,MedicalProfileSerializer,HabitsInfoSerializer,DietPlanSerializer,WomenHealthSerializer
from vitasana.serializers import BasicInfoOpSerializer,VitalsSerializer,PathologySerializer,AvParikshaSerializer,DietPlan,PrescriptionSerializer
from vitasana.serializers import PersonalDetails_DosaSerializer,PhysicalChar_DosaSerializer,PhysiologicalChar_DosaSerializer,PsychologicalChar_DosaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
def index(request):
    return render(request,'welcome.html')

#RestApi Views HEALTH ASSESSMENT SYSTEM

#Record based on Mobilenumber

@api_view(['GET'])
def patient_records_mobnumber(request, mobile_number):
    # Check if the mobile number exists in BasicInfo
    try:
        # Check if the mobile number exists in BasicInfo
        basic_info = BasicInfo.objects.get(MobileNumber=mobile_number)
    except BasicInfo.DoesNotExist:
        #return Response("No matching records found for this mobile number.")
        return Response({'message': 'No matching records found for this mobile number'}, status=status.HTTP_404_NOT_FOUND)


    # Retrieve patient records related to the mobile number
    patient_id = basic_info.patientid

    basic_info_serializer = BasinInfoSerializer(basic_info, context={'request': request})
    phyprofile = PhysicalProfile.objects.filter(patientid=patient_id)
    phyprofile_serializer = PhysicalProfileSerializer(phyprofile, many=True, context={'request': request})
    medprofile = MedicalProfile.objects.filter(patientid=patient_id)
    medprofile_serializer = MedicalProfileSerializer(medprofile, many=True, context={'request': request})
    habitsinfo = HabitsInfo.objects.filter(patientid=patient_id)
    habitsinfo_serializer = HabitsInfoSerializer(habitsinfo, many=True, context={'request': request})

    return Response({
        'basic_info': basic_info_serializer.data,
        'physical_profile': phyprofile_serializer.data,
        'medical_profile': medprofile_serializer.data,
        'habits_info': habitsinfo_serializer.data,
    })

#BaicInfo RestApi Views
class BasicInfoViewSet(viewsets.ModelViewSet):
    queryset = BasicInfo.objects.all()
    serializer_class = BasinInfoSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Item deleted successfully."}, status=status.HTTP_200_OK)
    
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
#-----------------------------------
        
#BasicInfoOp RestApi Views

class BasicInfoOpViewSet(viewsets.ModelViewSet):
    queryset = BasicInfoOp.objects.all()
    serializer_class = BasicInfoOpSerializer

    @action(detail=True, methods=['get', 'put'])
    def patientop(self, request, pk=None):
        try:
            patient = BasicInfo.objects.get(patientid=pk)
        except BasicInfo.DoesNotExist:
            return Response({'message': 'Patient does not exist'}, status=status.HTTP_404_NOT_FOUND)

        basic_info_op = BasicInfoOp.objects.filter(patientid=pk).first()

        if request.method == 'GET':
            basic_info_serializer = BasinInfoSerializer(patient, context={'request': request})
            if basic_info_op:
                basic_info_op_serializer = BasicInfoOpSerializer(basic_info_op, context={'request': request})
                vitals = Vitals.objects.filter(patientid=pk)
                vitals_serializer = VitalsSerializer(vitals, many=True, context={'request': request})
                pathology = Pathology.objects.filter(patientid=pk)
                pathology_serializer = PathologySerializer(pathology, many=True, context={'request': request})
                av_pariksha = AvPariksha.objects.filter(patientid=pk)
                av_pariksha_serializer = AvParikshaSerializer(av_pariksha, many=True, context={'request': request})
                return Response({
                    'basic_info': basic_info_serializer.data,
                    'basic_info_op': basic_info_op_serializer.data,
                    'vitals': vitals_serializer.data,
                    'pathology': pathology_serializer.data,
                    'av_pariksha': av_pariksha_serializer.data,
                })
            else:
                return Response({'basic_info': basic_info_serializer.data})

        elif request.method == 'PUT':
            basic_info_serializer = BasicInfoOpSerializer(patient, data=request.data.get('basic_info'), partial=True)
            basic_info_serializer.is_valid(raise_exception=True)
            basic_info_serializer.save()

            if basic_info_op:
                vitals_data = request.data.get('vitals')
                vitals = Vitals.objects.filter(patientid=pk)
                vitals_serializer = VitalsSerializer(data=vitals_data, many=True, partial=True)
                vitals_serializer.is_valid(raise_exception=True)
                for index, data in enumerate(vitals_data):
                    instance = vitals[index] if index < len(vitals) else None
                    vitals_serializer.save(patientid=patient, instance=instance)

                pathology_data = request.data.get('pathology')
                pathology = Pathology.objects.filter(patientid=pk)
                pathology_serializer = PathologySerializer(data=pathology_data, many=True, partial=True)
                pathology_serializer.is_valid(raise_exception=True)
                for index, data in enumerate(pathology_data):
                    instance = pathology[index] if index < len(pathology) else None
                    pathology_serializer.save(patientid=patient, instance=instance)

                av_pariksha_data = request.data.get('av_pariksha')
                av_pariksha = AvPariksha.objects.filter(patientid=pk)
                av_pariksha_serializer = AvParikshaSerializer(data=av_pariksha_data, many=True, partial=True)
                av_pariksha_serializer.is_valid(raise_exception=True)
                for index, data in enumerate(av_pariksha_data):
                    instance = av_pariksha[index] if index < len(av_pariksha) else None
                    av_pariksha_serializer.save(patientid=patient, instance=instance)

            return Response({'message': 'Patient information updated successfully.'}, status=status.HTTP_200_OK)

        else:
            return Response({'message': 'Invalid request method. Use GET or PUT.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




#Vitals RestApi Views
    
class VitalsViewSet(viewsets.ModelViewSet):
    queryset = Vitals.objects.all()
    serializer_class = VitalsSerializer


#WomenHealth RestApi Views
class WomenHealthViewSet(viewsets.ModelViewSet):
    queryset = WomenHealth.objects.all()
    serializer_class = WomenHealthSerializer

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


#RestApi Views DOSHA QUESTIONAIREE SYSTEM
#-----------------------------------------
    
#PersonalDetails_Dosa RestApi Views
    
class PersonalDetails_DosaViewSet(viewsets.ModelViewSet):
    queryset = PersonalDetails_Dosa.objects.all()
    serializer_class = PersonalDetails_DosaSerializer
    
    @action(detail=True, methods=['get', 'put'])
    def personaldetails(self, request, pk=None):
        try:
            personaldetails = PersonalDetails_Dosa.objects.get(personalid=pk)
        except PersonalDetails_Dosa.DoesNotExist:
            return Response({'message': 'Patient does not exist'}, status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            personaldetails_serializer = PersonalDetails_DosaSerializer(personaldetails, context={'request': request})
            physicalchar = PhysicalChar_Dosa.objects.filter(personalid=pk)
            physicalchar_serializer = PhysicalChar_DosaSerializer(physicalchar, many=True, context={'request': request})
            physiologicalchar = PhysiologicalChar_Dosa.objects.filter(personalid=pk)
            physiologicalchar_serializer = PhysiologicalChar_DosaSerializer(physiologicalchar, many=True, context={'request': request})
            psychologicalchar = PsychologicalChar_Dosa.objects.filter(personalid=pk)
            psychologicalchar_serializer = PsychologicalChar_DosaSerializer(psychologicalchar, many=True, context={'request': request})

            return Response({
                'personaldetails_info': personaldetails_serializer.data,
                'physicalchar_info': physicalchar_serializer.data,
                'physiologicalchar_info': physiologicalchar_serializer.data,
                'psychologicalchar_info': psychologicalchar_serializer.data,
            })

        elif request.method == 'PUT':
            personal_details_serializer = PersonalDetails_DosaSerializer(personaldetails, data=request.data.get('personaldetails_info'), partial=True)
            personal_details_serializer.is_valid(raise_exception=True)
            personal_details_serializer.save()

            # Update PhysicalChar_Dosa records
            physicalchar_data = request.data.get('physicalchar_info')
            physicalchar = PhysicalChar_Dosa.objects.filter(personalid=pk)
            physicalchar_serializer = PhysicalChar_DosaSerializer(data=physicalchar_data, many=True, partial=True)
            physicalchar_serializer.is_valid(raise_exception=True)
            for index, data in enumerate(physicalchar_data):
                instance = physicalchar[index] if index < len(physicalchar) else None
                physicalchar_serializer.save(personalid=personaldetails, instance=instance)

            # Update PhysiologicalChar_Dosa records
            physiologicalchar_data = request.data.get('physiologicalchar_info')
            physiologicalchar = PhysiologicalChar_Dosa.objects.filter(personalid=pk)
            physiologicalchar_serializer = PhysiologicalChar_DosaSerializer(data=physiologicalchar_data, many=True, partial=True)
            physiologicalchar_serializer.is_valid(raise_exception=True)
            for index, data in enumerate(physiologicalchar_data):
                instance = physiologicalchar[index] if index < len(physiologicalchar) else None
                physiologicalchar_serializer.save(personalid=personaldetails, instance=instance)

            # Update PsychologicalChar_Dosa records
            psychologicalchar_data = request.data.get('psychologicalchar_info')
            psychologicalchar = PsychologicalChar_Dosa.objects.filter(personalid=pk)
            psychologicalchar_serializer = PsychologicalChar_DosaSerializer(data=psychologicalchar_data, many=True, partial=True)
            psychologicalchar_serializer.is_valid(raise_exception=True)
            for index, data in enumerate(psychologicalchar_data):
                instance = psychologicalchar[index] if index < len(psychologicalchar) else None
                psychologicalchar_serializer.save(personalid=personaldetails, instance=instance)


            return Response({'message': 'Patient information updated successfully.'}, status=status.HTTP_200_OK)

        else:
            return Response({'message': 'Invalid request method. Use GET or PUT.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


#PhysicalChar_Dosa RestApi Views
    
class PhysicalChar_DosaViewSet(viewsets.ModelViewSet):
    queryset = PhysicalChar_Dosa.objects.all()
    serializer_class = PhysicalChar_DosaSerializer


#PhysiologicalChar_Dosa RestApi Views
    
class PhysiologicalChar_DosaViewSet(viewsets.ModelViewSet):
    queryset = PhysiologicalChar_Dosa.objects.all()
    serializer_class = PhysiologicalChar_DosaSerializer

#PsychologicalChar_Dosa RestApi Views
    
class PsychologicalChar_DosaViewSet(viewsets.ModelViewSet):
    queryset = PsychologicalChar_Dosa.objects.all()
    serializer_class = PsychologicalChar_DosaSerializer


