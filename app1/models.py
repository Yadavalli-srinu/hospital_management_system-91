from django.db import models



class department_model(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    hod = models.CharField(max_length=50)

    def __str__(self):
        return self.name    


class doctor_model(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(department_model, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class patient_model(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    emg_phone=models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    doctor = models.ForeignKey(doctor_model, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class patient_record_model(models.Model):
    patient = models.OneToOneField(patient_model, on_delete=models.CASCADE)
    disease = models.CharField(max_length=255)
    treatment = models.CharField(max_length=150)
    prescription = models.CharField(max_length=150)
    created_date = models.DateField()

    def __str__(self):
        return f"Record for {self.patient.name}"
