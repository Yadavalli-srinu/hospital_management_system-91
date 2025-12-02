from django.contrib import admin

from app1.models import department_model, doctor_model, patient_model, patient_record_model



class department_admin(admin.ModelAdmin):
    list_display = ['name', 'code', 'hod']
admin.site.register(department_model,department_admin)  


class doctor_admin(admin.ModelAdmin):
    list_display = ['name', 'department']
admin.site.register(doctor_model,doctor_admin)
    

class patient_admin(admin.ModelAdmin):
    list_display = [ 'name', 'age', 'gender', 'phone','emg_phone','address', 'doctor']
admin.site.register(patient_model,patient_admin)


class patient_record_admin(admin.ModelAdmin):
    list_display = ['patient', 'disease', 'treatment','prescription','created_date']
admin.site.register(patient_record_model,patient_record_admin)
    