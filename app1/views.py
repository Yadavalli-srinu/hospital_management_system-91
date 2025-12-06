from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from app1.models import department_model,doctor_model,patient_model,patient_record_model
from app1.forms import department_form,doctor_form,patient_form,patient_record_form
from app1.forms1 import department_u_form,doctor_u_form,patient_u_form,patient_u_record_form




#AUTHENTICATION

def reg_details(request):
    message=''
    if request.method=='POST':
        username = request.POST.get("reg_username")
        useremail=request.POST.get("reg_useremail")
        userp1 = request.POST.get("reg_password")
        userp2=request.POST.get("reg_conpassword")
        if userp1!=userp2:
            message='Invalid Password'
        elif User.objects.filter(email=useremail).exists():
            message='Email Already Exists'
        else:
            user = User.objects.create_user(username=username,email=useremail,password=userp1)
            user.save()
            message="User Created Successfully"
            return redirect('log101')
    return render(request,"frontend_app1/reg.html",{"message":message})
    
def log_details(request):
    message=''
    if request.method=='POST':
        username = request.POST.get("log_username")
        password = request.POST.get("log_password")

        user = authenticate(request,username=username,password=password)
        if  user is not None:
            login(request,user)
            
        else:
            message='Invalid Details'
            return redirect('home')
    return render(request,'frontend_app1/log.html',{"message":message})
    
#HOME PAGE

def home_page(request):
    return render(request,'frontend_app1/home.html')







#DEPARTMENT
def department_details(requst):
    data = department_model.objects.all()
    content={
        "data":data
    }
    return render(requst,'frontend_app1/department_table.html',content)

def department_empty(request):
     form= department_form()  
     if request.method=="POST":
         form=department_form(request.POST)
         if form.is_valid():
             form.save()
             return redirect('department_list')
     else:
      form= department_form()
      content={
         "form":form
     }
     return render(request,'frontend_app1/department_form.html',content)

def department_update(request,id):
     data=department_model.objects.get(id=id)  
     if request.method=="POST":
         form=department_u_form(request.POST,instance=data)
         if form.is_valid():
             form.save()
             return redirect('department_list')
     else:
      form= department_u_form(instance=data)
      content={
         "form":form
     }
     return render(request,'frontend_app1/department_u_form.html',content)

def department_delete(request,id):
    data = department_model.objects.get(id=id)
    data.delete()
    return redirect('department_list')

#DOCTOR

def doctor_details(request):
    data = doctor_model.objects.all()
    content = {
        "data": data
    }
    return render(request, 'frontend_app1/doctor_table.html', content)


def doctor_empty(request):
    form = doctor_form()
    if request.method == "POST":
        form = doctor_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = doctor_form()
    content = {
        "form": form
    }
    return render(request, 'frontend_app1/doctor_form.html', content)


def doctor_update(request, id):
    data = doctor_model.objects.get(id=id)
    if request.method == "POST":
        form = doctor_u_form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = doctor_u_form(instance=data)
    content = {
        "form": form
    }
    return render(request, 'frontend_app1/doctor_u_form.html', content)


def doctor_delete(request, id):
    data = doctor_model.objects.get(id=id)
    data.delete()
    return redirect('doctor_list')

#PATIENT

def patient_details(request):
    data = patient_model.objects.all()
    content = {
        "data": data
    }
    return render(request, 'frontend_app1/patient_table.html', content)


def patient_empty(request):
    form = patient_form()
    if request.method == "POST":
        form = patient_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = patient_form()
    content = {
        "form": form
    }
    return render(request, 'frontend_app1/patient_form.html', content)


def patient_update(request, id):
    data = patient_model.objects.get(id=id)
    if request.method == "POST":
        form = patient_u_form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = patient_u_form(instance=data)
    content = {
        "form": form
    }
    return render(request, 'frontend_app1/patient_u_form.html', content)


def patient_delete(request, id):
    data = patient_model.objects.get(id=id)
    data.delete()
    return redirect('patient_list')

#PATIENT_RECORD

def patient_record_details(request):
    data = patient_record_model.objects.all()
    content = {
        "data": data
    }
    return render(request, 'frontend_app1/patient_record_table.html', content)


def patient_record_empty(request):
    form = patient_record_form()
    if request.method == "POST":
        form = patient_record_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_record_list')
    else:
        form = patient_record_form()
    content = {
        "form": form
    }
    return render(request, 'frontend_app1/patient_record_form.html', content)


def patient_record_update(request, id):
    data = patient_record_model.objects.get(id=id)
    if request.method == "POST":
        form = patient_u_record_form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('patient_record_list')
    else:
        form = patient_u_record_form(instance=data)
    content = {
        "form": form
    }
    return render(request, 'frontend_app1/patient_record_u_form.html', content)


def patient_record_delete(request, id):
    data = patient_record_model.objects.get(id=id)
    data.delete()
    return redirect('patient_record_list')