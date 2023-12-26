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
    def validate_FirstName(self, value):
        if not value:
            raise serializers.ValidationError("First Name cannot be empty.")
        return value

    def validate_LastName(self, value):
        if not value:
            raise serializers.ValidationError("Last Name cannot be empty.")
        return value
    
    def validate_Age(self, value):
        if not value:
            raise serializers.ValidationError("Age cannot be empty.")
        return value

    def validate_Gender(self, value):
        if not value:
            raise serializers.ValidationError("Gender cannot be empty.")
        return value
    def validate_Occupation(self, value):
        if not value:
            raise serializers.ValidationError("Occupation cannot be empty.")
        return value
    
    def validate_MaritialStatus(self, value):
        if not value:
            raise serializers.ValidationError("MaritialStatus cannot be empty.")
        return value
    
    def validate_Address(self, value):
        if not value:
            raise serializers.ValidationError("Address cannot be empty.")
        return value
    
    def validate_City(self, value):
        if not value:
            raise serializers.ValidationError("City cannot be empty.")
        return value
    
    def validate_State(self, value):
        if not value:
            raise serializers.ValidationError("State cannot be empty.")
        return value
    
    def validate_Pincode(self, value):
        if not value:
            raise serializers.ValidationError("Pincode cannot be empty.")
        return value

    def validate_MobileNumber(self, value):
        if not value:
            raise serializers.ValidationError("Mobile Number cannot be empty.")
        return value
    
    def validate_AlternateNumber(self, value):
        if not value:
            raise serializers.ValidationError("AlternateNumber cannot be empty.")
        return value

    def validate_EmailAddress(self, value):
        if not value:
            raise serializers.ValidationError("Email Address cannot be empty.")
        return value
    
    def validate_EmergencyContactPersonFirstName(self, value):
        if not value:
            raise serializers.ValidationError("EmergencyContactPersonFirstName cannot be empty.")
        return value
    
    def validate_EmergencyContactPersonLastName(self, value):
        if not value:
            raise serializers.ValidationError("EmergencyContactPersonLastName cannot be empty.")
        return value

    def validate_EmergencyContactPersonMobileNumber(self, value):
        if not value:
            raise serializers.ValidationError("EmergencyContactPersonMobileNumber cannot be empty.")
        return value
    
    def validate_EmergencyContactPersonRelation(self, value):
        if not value:
            raise serializers.ValidationError("EmergencyContactPersonRelation cannot be empty.")
        return value
 
   
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
