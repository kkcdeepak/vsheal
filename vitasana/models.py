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

    patientid = models.AutoField(primary_key=True)
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



    phy_profile_id = models.IntegerField(primary_key=True)
    Height = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    Appetite = models.CharField(max_length=50, choices=APPETITE_CHOICES, null=True)
    SleepCycle = models.CharField(max_length=50, choices=SLEEP_CYCLE_CHOICES, null=True)
    FoodPreferences = models.CharField(max_length=500, null=True)
    DigestiveIssues = models.CharField(max_length=500, null=True)
    CuisinePreferred = models.CharField(max_length=500,null=True)
    Description1 = models.CharField(max_length=500, null=True)
    Description2 = models.CharField(max_length=500, null=True)
    patientid = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)


# HEALTH ASSESSMENT SYSTEM-MedicalProfile
    

class MedicalProfile(models.Model):

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]

    med_profile_id = models.IntegerField(primary_key=True)
    SupplementsTaken = models.CharField(max_length=500, null=True)
    RecentIllnessOrInjury = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True)
    ChronicMedicalConditions = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True)
    DiagnosedWithChronicDiseases = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True)
    RespiratorySymptoms = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True)
    NeurologicalSymptoms = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True)
    DrugAllergiesOrAdverseReactions = models.CharField(max_length=3, choices=YES_NO_CHOICES, null=True)
    patientid = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)



# HEALTH ASSESSMENT SYSTEM-HabitsInfo

class HabitsInfo(models.Model):

    YES_NO_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    hab_info_id = models.IntegerField(primary_key=True)
    LevelOfActivity = models.CharField(max_length=500, null=True)

    SmokingHabit = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No')
    CigarettesPerDay = models.IntegerField(null=True, blank=True)
    YearsOfSmoking = models.IntegerField(null=True, blank=True)

    AlcoholConsumption = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No')
    DrinksPerDay_Alcohol = models.IntegerField(null=True, blank=True)
    YearsOfDrinking_Alcohol = models.IntegerField(null=True, blank=True)

    
    CaffeineConsumption = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No')
    NumberOfCupsPerDay_Caffeine = models.IntegerField(null=True, blank=True)
    YearsOfDrinking_Caffeine = models.IntegerField(null=True, blank=True)

    TobaccoConsumption = models.CharField(max_length=3, choices=YES_NO_CHOICES, default='No')
    TimesPerDay_Tobacco = models.IntegerField(null=True, blank=True)

    OtherHabits = models.CharField(max_length=500, null=True)
    patientid = models.ForeignKey(BasicInfo , on_delete=models.CASCADE)  #here basic info changed from string to model name



#OP ASSESSMENT SYSTEM-Basicinfo
#------------------------------
    
class BasicInfoOp(models.Model):
    BasicInfoOpID = models.IntegerField(primary_key=True)
    Weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    Height = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=None)
    patientid = models.ForeignKey(BasicInfo , on_delete=models.CASCADE)

#OP ASSESSMENT SYSTEM-Vitals

class Vitals(models.Model):
    TEMPERATURE_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]

    BP_CHOICES = [
        ('Systolic', 'Systolic'),
        ('Diastolic', 'Diastolic'),
    ]

    PRESENT_ILLNESS_ONSET_CHOICES = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    SURGICAL_HISTORY_CHOICES = [
        ('emergency', 'emergency'),
        ('elective', 'elective'),
    ]

    FAMILY_HISTORY_CHOICES = [
        ('maternal family', 'maternal family'),
        ('paternal family', 'paternal family'),
    ]

    ADDICTION_HABITS_CHOICES = [
        ('alcohol', 'alcohol'),
        ('smoking', 'smoking'),
        ('tobacco', 'tobacco'),
    ]

    vitals_id = models.IntegerField(primary_key=True)
    Temperature = models.CharField(max_length=3, choices=TEMPERATURE_CHOICES, null=True)
    BP = models.CharField(max_length=9, choices=BP_CHOICES, null=True)
    GeneralBodyType = models.CharField(max_length=100, null=True)
    PulseRate = models.IntegerField(null=True)
    HeartRate = models.IntegerField(null=True)
    SpO2 = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    PresentIllnessOnset = models.CharField(max_length=1, choices=PRESENT_ILLNESS_ONSET_CHOICES, null=True)
    SurgicalHistory = models.CharField(max_length=9, choices=SURGICAL_HISTORY_CHOICES, null=True)
    FamilyHistory = models.CharField(max_length=16, choices=FAMILY_HISTORY_CHOICES, null=True)
    AddictionHabits = models.CharField(max_length=7, choices=ADDICTION_HABITS_CHOICES, null=True)
    MedicationHistoryMonth = models.IntegerField(null=True)
    patientid = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)

#OP ASSESSMENT SYSTEM-pathology
    
class Pathology(models.Model):
    BLOOD_OUTCOME_CHOICES = [
        ('High', 'High'),
        ('Low', 'Low'),
    ]

    SCAN_OUTCOME_CHOICES = [
        ('Abnormality', 'Abnormality'),
        ('Risk', 'Risk'),
    ]

    DISEASE_PROGNOSIS_CHOICES = [
        ('good', 'good'),
        ('manageable', 'manageable'),
        ('bad', 'bad'),
        ('incurable', 'incurable'),
    ]

    pathology_id = models.IntegerField(primary_key=True)
    BloodTestsAdvisedDate = models.DateField(null=True)
    BloodReportsSummaryDate = models.DateField(null=True)
    MentionBloodOutcome = models.CharField(max_length=4, choices=BLOOD_OUTCOME_CHOICES, null=True)
    ScanReportsAdvisedDate = models.DateField(null=True)
    MentionScanOutcome = models.CharField(max_length=11, choices=SCAN_OUTCOME_CHOICES, null=True)
    SummaryOfReports = models.CharField(max_length=500, null=True)
    FinalDiagnosis = models.CharField(max_length=500, null=True)
    MedicationDosage = models.CharField(max_length=100, null=True)
    MedicationDurations = models.CharField(max_length=100, null=True)
    DietDos = models.CharField(max_length=500, null=True)
    DietDonts = models.CharField(max_length=500, null=True)
    LifestyleDos = models.CharField(max_length=500, null=True)
    LifestyleDonts = models.CharField(max_length=500, null=True)
    DiseasePrognosis = models.CharField(max_length=10, choices=DISEASE_PROGNOSIS_CHOICES, null=True)
    FollowUpScheduleDate = models.DateField(null=True)
    patientid = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)

#OP ASSESSMENT SYSTEM- ASHTA-VIDHA PARIKSHA

class AvPariksha(models.Model):
    STOOL_CONSISTENCY_CHOICES = [
        ('solid', 'solid'),
        ('semisolid', 'semisolid'),
        ('fluid', 'fluid'),
    ]

    STOOL_ODOUR_CHOICES = [
        ('present', 'present'),
        ('absent', 'absent'),
    ]

    STOOL_QUANTITY_CHOICES = [
        ('more', 'more'),
        ('less', 'less'),
    ]



    SOUND_CHOICES = [
        ('normal', 'normal'),
        ('abnormal', 'abnormal'),
    ]

    SOUND_SPEECH_CHOICES = [
        ('low voice', 'low voice'),
        ('muffled voice', 'muffled voice'),
        ('high pitched voice', 'high pitched voice'),
        ('hoarse voice', 'hoarse voice'),
    ]

    EYE_MENTION_CHOICES = [
        ('normal', 'normal'),
        ('abnormal', 'abnormal'),
    ]

    WHICH_EYE_CHOICES = [
        ('left eye', 'left eye'),
        ('right eye', 'right eye'),
    ]

    PALPEBRAL_CONJUNCTIVA_CHOICES = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]

    BULBAR_CONJUNCTIVA_CHOICES = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]

    UNDER_EYE_SACKS_CHOICES = [
        ('yes', 'yes'),
        ('no', 'no'),
		
    ]

    UNDER_EYE_BLACKISHNESS_CHOICES = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]

    PERIORBITAL_SWELLING_CHOICES = [
        ('yes', 'yes'),
        ('no', 'no'),
    ]

    APPEARANCE_CHOICES = [
        ('lean built', 'lean built'),
        ('moderate', 'moderate'),
    ]

    MUSCLE_STURDINESS_CHOICES = [
        ('good', 'good'),
        ('moderate', 'moderate'),
        ('flabby', 'flabby'),
    ]

    SPINE_CHOICES = [
        ('erect', 'erect'),
        ('hunk back', 'hunk back'),
    ]

    FACE_CHOICES = [
        ('pale', 'pale'),
        ('dull', 'dull'),
        ('active', 'active'),
        ('charming', 'charming'),
    ]

    av_pariksha_id = models.IntegerField(primary_key=True)
    StoolConsistency = models.CharField(max_length=10, choices=STOOL_CONSISTENCY_CHOICES, null=True)
    StoolOdour = models.CharField(max_length=7, choices=STOOL_ODOUR_CHOICES, null=True)
    StoolColour = models.CharField(max_length=50, null=True)
    StoolQuantity = models.CharField(max_length=4, choices=STOOL_QUANTITY_CHOICES, null=True)
    UrineVolume = models.CharField(max_length=20, null=True)
    UrineTurbidity = models.CharField(max_length=20, null=True)
    BurningPressure = models.CharField(max_length=20, null=True)
    AbnormalColorOfUrine = models.CharField(max_length=50, null=True)
    CoatingOnTheTongue = models.CharField(max_length=50, null=True)
    FissuresOnTheTongue = models.CharField(max_length=50, null=True)
    AbnormalColourOfTheTongue = models.CharField(max_length=50, null=True)
    Sound = models.CharField(max_length=8, choices=SOUND_CHOICES, null=True)
    SoundHearingCapacity = models.CharField(max_length=50, null=True)
    SoundSpeech = models.CharField(max_length=18, choices=SOUND_SPEECH_CHOICES, null=True)
    EyeMention = models.CharField(max_length=8, choices=EYE_MENTION_CHOICES, null=True)
    WhichEye = models.CharField(max_length=10, choices=WHICH_EYE_CHOICES, null=True)
    PalpebralConjunctiva = models.CharField(max_length=3, choices=PALPEBRAL_CONJUNCTIVA_CHOICES, null=True)
    BulbarConjunctiva = models.CharField(max_length=3, choices=BULBAR_CONJUNCTIVA_CHOICES, null=True)
    UnderEyeSacks = models.CharField(max_length=3, choices=UNDER_EYE_SACKS_CHOICES, null=True)
    UnderEyeBlackishsness = models.CharField(max_length=3, choices=UNDER_EYE_BLACKISHNESS_CHOICES, null=True)
    PeriorbitalSwelling = models.CharField(max_length=3, choices=PERIORBITAL_SWELLING_CHOICES, null=True)
    Appearance = models.CharField(max_length=10, choices=APPEARANCE_CHOICES, null=True)
    MuscleSturdiness = models.CharField(max_length=8, choices=MUSCLE_STURDINESS_CHOICES, null=True)
    Spine = models.CharField(max_length=9, choices=SPINE_CHOICES, null=True)
    Face = models.CharField(max_length=8, choices=FACE_CHOICES, null=True)
    patientid = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)


#OP ASSESSMENT SYSTEM- Prescription
    

class Prescription(models.Model):
    prescription_id = models.IntegerField(primary_key=True)
    Complaints = models.TextField(null=True)
    Investigation_Findings = models.TextField(null=True)
    Preliminary_Diagnosis = models.TextField(null=True)
    Final_Diagnosis = models.TextField(null=True)
    MedName = models.CharField(max_length=255, null=True)
    Dose = models.CharField(max_length=50, null=True)
    Timing = models.CharField(max_length=50, null=True)
    Frequency = models.CharField(max_length=50, null=True)
    RelationWithFood = models.CharField(max_length=50, null=True)
    Duration = models.CharField(max_length=50, null=True)
    Adjuvant = models.CharField(max_length=50, null=True)
    Investigations_Advised = models.TextField(null=True)
    Date_of_Next_Visit = models.DateField(null=True)
    DietDos = models.TextField(null=True)
    DietDont = models.TextField(null=True)
    Life_Style_Dos = models.TextField(null=True)
    Life_Style_Dont = models.TextField(null=True)
    Yoga_Pranayam_Exercise_Dos = models.TextField(null=True)
    Yoga_Pranayam_Exercise_Dont = models.TextField(null=True)
    Additional_Notes = models.TextField(null=True)
    patientid = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)



#OP ASSESSMENT SYSTEM- DIET PLAN
    

class DietPlan(models.Model):
    dietplan_id = models.IntegerField(primary_key=True)
    Dietician = models.CharField(max_length = 50, null=True)
    MON_MEAL = models.TextField(max_length = 1000, null=True)
    TUE_MEAL = models.TextField(max_length = 1000, null=True)
    WED_MEAL = models.TextField(max_length = 1000, null=True)
    THU_MEAL = models.TextField(max_length = 1000, null=True)
    FRI_MEAL = models.TextField(max_length = 1000, null=True)
    SAT_MEAL = models.TextField(max_length = 1000, null=True)
    SUN_MEAL = models.TextField(max_length = 1000, null=True)
    DietryGuidance = models.TextField(null=True)
    RECIPES = models.TextField(null=True)
    ANALYSISOFDIET = models.TextField(null=True)
    patientid = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)    

    

