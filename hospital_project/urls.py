"""
URL configuration for hospital_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import (reg_details,log_details,home_page,
                        department_details,department_empty,department_update,department_delete,
                        doctor_details,doctor_empty,doctor_update,doctor_delete,
                        patient_details,patient_empty,patient_update,patient_delete,
                        patient_record_details,patient_record_empty,patient_record_update,patient_record_delete,verify_user)

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path("", reg_details, name="reg101"),
    path("login/", log_details, name="log101"),
    path("home/", home_page, name="home"),
   path('verify/<str:action>/<str:model_name>/<int:id>/',verify_user, name='verify_user'),

    # DEPARTMENT 
    path("department/", department_details, name="department_list"),
    path("department/add/", department_empty, name="department_add"),
    path("department/update/<int:id>/", department_update, name="department_update"),
    path("department/delete/<int:id>/", department_delete, name="department_delete"),

    #  DOCTOR 
    path("doctor/", doctor_details, name="doctor_list"),
    path("doctor/add/", doctor_empty, name="doctor_add"),
    path("doctor/update/<int:id>/", doctor_update, name="doctor_update"),
    path("doctor/delete/<int:id>/", doctor_delete, name="doctor_delete"),

    #  PATIENT 
    path("patient/", patient_details, name="patient_list"),
    path("patient/add/", patient_empty, name="patient_add"),
    path("patient/update/<int:id>/", patient_update, name="patient_update"),
    path("patient/delete/<int:id>/", patient_delete, name="patient_delete"),

    #  PATIENT RECORD
    path("patient-record/", patient_record_details, name="patient_record_list"),
    path("patient-record/add/", patient_record_empty, name="patient_record_add"),
    path("patient-record/update/<int:id>/", patient_record_update, name="patient_record_update"),
    path("patient-record/delete/<int:id>/", patient_record_delete, name="patient_record_delete"),

]
