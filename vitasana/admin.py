from django.contrib import admin

from vitasana.models import BasicInfo,PhysicalProfile,MedicalProfile,HabitsInfo
# Register your models here.

admin.site.register(BasicInfo)
admin.site.register(PhysicalProfile)
admin.site.register(MedicalProfile)
admin.site.register(HabitsInfo)