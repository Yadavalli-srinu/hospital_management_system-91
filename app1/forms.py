from django import forms
from app1.models import department_model,doctor_model,patient_model,patient_record_model
class department_form(forms.ModelForm):
    class Meta:
        model = department_model
        fields = '__all__'

class doctor_form(forms.ModelForm):
    class Meta:
        model = doctor_model
        fields = '__all__'
class patient_form(forms.ModelForm):
    class Meta:
        model = patient_model
        fields = '__all__'
class patient_record_form(forms.ModelForm):
    class Meta:
        model = patient_record_model
        fields = '__all__'

