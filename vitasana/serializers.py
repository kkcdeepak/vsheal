from rest_framework import serializers
from vitasana.models import BasicInfo,PhysicalProfile,MedicalProfile,HabitsInfo

#basicinfo Serializers
class BasinInfoSerializer(serializers.HyperlinkedModelSerializer):
    patientid=serializers.ReadOnlyField()
    class Meta:
        model = BasicInfo
        #fields = ['','']
        #exclude = ['',]
        fields = "__all__"

#validation for fields
    #duplicate record validation    
    def validate_MobileNumber(self, data):
        # Check if the MobileNumber already exists in the database
        mobile_number_exists = BasicInfo.objects.filter(MobileNumber=data).exists()

        # If the mobile number already exists, raise a validation error
        if mobile_number_exists:
            raise serializers.ValidationError("This mobile number already exists in the database.")
        
        return data
        
#Validation for null value of fields
    def validate(self, data):
        required_fields = ['FirstName', 'LastName', 'Age','Gender', 'Occupation', 'MaritialStatus', 'Address', 'City', 'State','Pincode','MobileNumber', 'AlternateNumber', 'EmailAddress','EmergencyContactPersonFirstName', 'EmergencyContactPersonLastName', 'EmergencyContactPersonMobileNumber', 'EmergencyContactPersonRelation']
        
        # Check if any of the required fields are missing or empty
        for field in required_fields:
            if field not in data or not data[field]:
                raise serializers.ValidationError(f"{field} field is required.")
        
        return data 
   
#PhysicalProfile Serializers
        
class PhysicalProfileSerializers(serializers.HyperlinkedModelSerializer):
    #patientid=serializers.ReadOnlyField()
    class Meta:
        model = PhysicalProfile
        fields = "__all__" 

#Validation for null value of fields
    def validate(self, data):
        required_fields = ['Height', 'Weight', 'Appetite','SleepCycle', 'FoodPreferences', 'DigestiveIssues', 'CuisinePreferred', 'Description1', 'Description2']
        
        # Check if any of the required fields are missing or empty
        for field in required_fields:
            if field not in data or not data[field]:
                raise serializers.ValidationError(f"{field} field is required.")
        
        return data 
   


#MedicalProfile Serializers

class MedicalProfileSerializers(serializers.HyperlinkedModelSerializer):
    #patientid=serializers.ReadOnlyField()
    class Meta:
        model = MedicalProfile

        fields = "__all__" 

#Validation for null value of fields
    def validate(self, data):
        required_fields = ['SupplementsTaken', 'RecentIllnessOrInjury', 'ChronicMedicalConditions','DiagnosedWithChronicDiseases', 'RespiratorySymptoms', 'NeurologicalSymptoms', 'DrugAllergiesOrAdverseReactions']
        
        # Check if any of the required fields are missing or empty
        for field in required_fields:
            if field not in data or not data[field]:
                raise serializers.ValidationError(f"{field} field is required.")
        
        return data 

#HabitsInfo Serializers

class HabitsInfoSerializers(serializers.HyperlinkedModelSerializer):
    #patientid=serializers.ReadOnlyField()
    class Meta:
        model = HabitsInfo
        fields = "__all__" 

#Validation for null value of fields
    def validate(self, data):
        required_fields = ['LevelOfActivity', 'SmokingHabit', 'AlcoholConsumption','CaffeineConsumption', 'TobaccoConsumption', 'OtherHabits']
        
        # Check if any of the required fields are missing or empty
        for field in required_fields:
            if field not in data or not data[field]:
                raise serializers.ValidationError(f"{field} field is required.")
        
        return data 