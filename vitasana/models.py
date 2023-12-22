from django.db import models
from django.utils import timezone

# Create your models here.

# HEALTH ASSESSMENT SYSTEM-BasicInfo

class BasicInfo(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
    ]

    RELATIONSHIP_CHOICES = [
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Husband', 'Husband'),
        ('Wife', 'Wife'),
        ('Son', 'Son'),
        ('Daughter', 'Daughter'),
        
    ]

    patientid = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=255, null=True)
    MiddleName = models.CharField(max_length=255, null=True)
    LastName = models.CharField(max_length=255, null=True)
    Age = models.IntegerField(null=True)
    Gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    Occupation = models.CharField(max_length=255, null=True)
    MaritialStatus = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES, null=True)
    Address = models.CharField(max_length=255, null=True)
    City = models.CharField(max_length=100, null=True)
    State = models.CharField(max_length=100, null=True)
    Pincode = models.CharField(max_length=20, null=True)
    MobileNumber = models.CharField(max_length=20, null=True)
    AlternateNumber = models.CharField(max_length=20, null=True)
    EmailAddress = models.EmailField(max_length=255, null=True)
    LandlineNumber = models.CharField(max_length=20, null=True)
    EmergencyContactPersonFirstName = models.CharField(max_length=255, null=True)
    EmergencyContactPersonLastName = models.CharField(max_length=255, null=True)
    EmergencyContactPersonMobileNumber = models.CharField(max_length=20, null=True)
    EmergencyContactPersonRelation = models.CharField(max_length=100, choices=RELATIONSHIP_CHOICES, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    

# HEALTH ASSESSMENT SYSTEM-PhysicalProfile


class PhysicalProfile(models.Model):
    APPETITE_CHOICES = [
        ('good', 'Good'),
        ('verygood', 'Very Good'),
        ('abnormally high', 'Abnormally High'),
        ('poor', 'Poor'),
        ('very poor', 'Very Poor'),
        ('absent', 'Absent'),
    ]

    SLEEP_CYCLE_CHOICES = [
        ('good', 'Good'),
        ('verygood', 'Very Good'),
        ('abnormally high', 'Abnormally High'),
        ('poor', 'Poor'),
        ('verypoor', 'Very Poor'),
        ('absent', 'Absent'),
    ]

    FOOD_PREFERENCES_CHOICES = [
        ('Vegetarian', 'Vegetarian'),
        ('Lacto Vegetarian', 'Lacto Vegetarian'),
        ('Lact-ovo-Vegetarian', 'Lact-ovo-Vegetarian'),
        ('Non-Vegetarian', 'Non-Vegetarian'),
    ]

    DIGESTIVE_ISSUES_CHOICES = [
        ('Constipation', 'Constipation'),
        ('Diarrhoea', 'Diarrhoea'),
        ('Bloating', 'Bloating'),
        ('Other', 'Other'),
        ('None', 'None'),
    ]

    CUISINE_PREFERRED_CHOICES = [
        ('South Indian', 'South Indian'),
        ('North Indian', 'North Indian'),
        ('Asian', 'Asian'),
        ('East Indian', 'East Indian'),
        ('West Indian', 'West Indian'),
        ('Mediterranean', 'Mediterranean'),
        ('Western', 'Western'),
        ('Others', 'Others'),
    ]

    DESCRIPTION1_CHOICES = [
        ('Cooking/eating at home mostly', 'Cooking/eating at home mostly'),
        ('Eating out/ordering food online atleast 2-3 times a week', 'Eating out/ordering food online atleast 2-3 times a week'),
        ('Eating out/ordering food online mostly', 'Eating out/ordering food online mostly'),
    ]

    DESCRIPTION2_CHOICES = [
        ('I have a cook', 'I have a cook'),
        ('A family member/friend cooks for me', 'A family member/friend cooks for me'),
        ('I make my own food', 'I make my own food'),
    ]

    phy_profile_id = models.IntegerField(primary_key=True)
    Height = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Appetite = models.CharField(max_length=50, choices=APPETITE_CHOICES, null=True)
    SleepCycle = models.CharField(max_length=50, choices=SLEEP_CYCLE_CHOICES, null=True)
    FoodPreferences = models.CharField(max_length=50, choices=FOOD_PREFERENCES_CHOICES, null=True)
    DigestiveIssues = models.CharField(max_length=50, choices=DIGESTIVE_ISSUES_CHOICES, null=True)
    CuisinePreferred = models.CharField(max_length=50, choices=CUISINE_PREFERRED_CHOICES, null=True)
    Description1 = models.CharField(max_length=100, choices=DESCRIPTION1_CHOICES, null=True)
    Description2 = models.CharField(max_length=100, choices=DESCRIPTION2_CHOICES, null=True)
    patientid = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)


# HEALTH ASSESSMENT SYSTEM-MedicalProfile
    

class MedicalProfile(models.Model):
    SUPPLEMENTS_TAKEN_CHOICES = [
        ('Multi-Vitamins', 'Multi-Vitamins'),
        ('Single Vitamins', 'Single Vitamins'),
        ('Herbs/herbal supplements', 'Herbs/herbal supplements'),
        ('Nutraceuticals', 'Nutraceuticals'),
        ('Protein supplements', 'Protein supplements'),
    ]

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    med_profile_id = models.IntegerField(primary_key=True)
    SupplementsTaken = models.CharField(max_length=50, choices=SUPPLEMENTS_TAKEN_CHOICES, null=True)
    RecentIllnessOrInjury = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True)
    ChronicMedicalConditions = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True)
    DiagnosedWithChronicDiseases = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True)
    RespiratorySymptoms = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True)
    NeurologicalSymptoms = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True)
    DrugAllergiesOrAdverseReactions = models.CharField(max_length=500, null=True)
    patientid = models.ForeignKey('BasicInfo', on_delete=models.CASCADE)



# HEALTH ASSESSMENT SYSTEM-HabitsInfo

class HabitsInfo(models.Model):
    LEVEL_OF_ACTIVITY_CHOICES = [
        ('Sedentary', 'Sedentary'),
        ('Lightly active', 'Lightly active'),
        ('Moderately active', 'Moderately active'),
        ('Very active', 'Very active'),
    ]

    YES_NO_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    hab_info_id = models.IntegerField(primary_key=True)
    LevelOfActivity = models.CharField(max_length=50, choices=LEVEL_OF_ACTIVITY_CHOICES, null=True)
    SmokingHabit = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True)
    AlcoholConsumption = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True)
    CaffeineConsumption = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True)
    TobaccoConsumption = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True)
    OtherHabits = models.CharField(max_length=500, null=True)
    patientid = models.ForeignKey('BasicInfo', on_delete=models.CASCADE)
