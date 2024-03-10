from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import patient, appointments
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def index(request):
    # if request.method == "POST":
    #     firstname = request.POST["firstname"]
    #     lastname = request.POST["lastname"]
    #     insurance_no = request.POST["insurance_no"]
        
    #     new_patient = patient(firstname = firstname, lastname = lastname, insurance_no = insurance_no)
    #     new_patient.save()
    
    return render(request, "index.html")

def indexdoctor(request):
    appointment = appointments.objects.all()
    return render(request, "index-doctor.html", {'appointment':appointment})

def loginview(request):
    return render(request, "login.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = auth.authenticate(username= username, password= password)
        
        if user is not None:
            if user.is_staff == True:
                auth.login(request, user)
                return redirect("indexdoctor")
            else:
                auth.login(request, user)
                return redirect("index")
        
    return render(request, "login.html")


def registerview(request):
    return render(request, "register.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        jobtitle = request.POST["jobtitle"]
        
        if password1 == password2:
            password = make_password(password1)
            if jobtitle == "doctor":
                is_staff = True
            else:
                is_staff = False
            user = User.objects.create(first_name= first_name, last_name= last_name, username= username, email= email, password= password, is_staff= is_staff)
            user.save()
            # messages.success(request, "Registered successfully")
        
        
    return redirect("loginview")

def bookappointment(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        date = request.POST["date"]
        department = request.POST["department"]
        doctor = request.POST["doctor"]
        message = request.POST["message"]
        
        newappointment = appointments(patient= name, email= email, phone= phone, date= date, department= department, doctor= doctor, message= message)
        newappointment.save()
        
        return redirect("/", status=200)
        
        
