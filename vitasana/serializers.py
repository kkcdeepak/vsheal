from rest_framework import serializers
from vitasana.models import BasicInfo,PhysicalProfile,MedicalProfile,HabitsInfo,BasicInfoOp,Vitals,Pathology,AvPariksha,DietPlan,Prescription


#HEALTH ASSESSMENT SYSTEM Serialization

#basicinfo Serializers
class BasinInfoSerializer(serializers.ModelSerializer):
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
        
class PhysicalProfileSerializer(serializers.ModelSerializer):
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

class MedicalProfileSerializer(serializers.ModelSerializer):
    #patientid=serializers.ReadOnlyField()
    class Meta:
        model = MedicalProfile

        fields = "__all__" 

#Validation for null value of fields
    def validate(self, data):
        required_fields = ['SupplementsTaken', 'RecentIllnessOrInjury', 'ChronicMedicalConditions', 'DiagnosedWithChronicDiseases', 'RespiratorySymptoms', 'NeurologicalSymptoms', 'DrugAllergiesOrAdverseReactions']
        
        for field in required_fields:
            if field not in data or not data[field]:
                raise serializers.ValidationError(f"{field} field is required.")

        # Check if 'Yes' is selected for specific fields and their corresponding detail fields are provided
        yes_fields = ['RecentIllnessOrInjury', 'ChronicMedicalConditions', 'DiagnosedWithChronicDiseases', 'RespiratorySymptoms', 'NeurologicalSymptoms', 'DrugAllergiesOrAdverseReactions']
        for field in yes_fields:
            if data.get(field) == 'yes' and f"{field}_details" not in data:
                raise serializers.ValidationError(f"{field}_details field is required when {field} is 'yes'.")

        return data 

#HabitsInfo Serializers

class HabitsInfoSerializer(serializers.ModelSerializer):
    #patientid=serializers.ReadOnlyField()
    class Meta:
        model = HabitsInfo
        fields = "__all__" 

    def create(self, validated_data):
        patient_id = validated_data.get('patientid')

        try:
            existing_instance = HabitsInfo.objects.get(patientid=patient_id)
            for attr, value in validated_data.items():
                setattr(existing_instance, attr, value)
            existing_instance.save()
            return existing_instance
        except HabitsInfo.DoesNotExist:
            return HabitsInfo.objects.create(**validated_data)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        # Handle conditional representation for SmokingHabit
        smoking_habit = data.get('SmokingHabit')
        if smoking_habit == 'No':
            data.pop('CigarettesPerDay', None)
            data.pop('YearsOfSmoking', None)

        # Handle conditional representation for AlcoholConsumption
        alcohol_consumption = data.get('AlcoholConsumption')
        if alcohol_consumption == 'No':
            data.pop('DrinksPerDay_Alcohol', None)
            data.pop('YearsOfDrinking_Alcohol', None)

        # Handle conditional representation for CaffeineConsumption
        caffeine_consumption = data.get('CaffeineConsumption')
        if caffeine_consumption == 'No':
            data.pop('NumberOfCupsPerDay_Caffeine', None)
            data.pop('YearsOfDrinking_Caffeine', None)

        # Handle conditional representation for TobaccoConsumption
        tobacco_consumption = data.get('TobaccoConsumption')
        if tobacco_consumption == 'No':
            data.pop('TimesPerDay_Tobacco', None)

        return data



#Validation for null value of fields
    def validate(self, data):
        required_fields = ['LevelOfActivity', 'SmokingHabit', 'AlcoholConsumption','CaffeineConsumption', 'TobaccoConsumption', 'OtherHabits']
        
        # Check if any of the required fields are missing or empty
        for field in required_fields:
            if field not in data or not data[field]:
                raise serializers.ValidationError(f"{field} field is required.")
        
        return data 


#OUT PATIENT ASSESSMENT SYSTEM  Serialization
#---------------------------------------------

#BASIC INFO-OP ASSESSMENT
    
class BasicInfoOpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BasicInfoOp
        fields = '__all__'

#Vitals OP ASSESSMENT
        
class VitalsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vitals
        fields = '__all__'

#Pathology OP ASSESSMENT

class PathologySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pathology
        fields = '__all__'

#AvPariksha OP ASSESSMENT

class AvParikshaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AvPariksha        
        fields = '__all__'

#OP ASSESSMENT SYSTEM- PRESCRIPTION

class PrescriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prescription        
        fields = '__all__'




#OP ASSESSMENT SYSTEM- DIET PLAN

class DietPlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DietPlan        
        fields = '__all__'
