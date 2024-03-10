from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class department(models.Model):
    departmentname = models.CharField(max_length=50)
    
class doctor(models.Model):
    doctorfname = models.CharField(max_length=100)
    doctorlname = models.CharField(max_length=100)
    doctorphone = models.CharField(max_length=20)
    department = models.ForeignKey(department, on_delete = models.CASCADE)
    
class pharmacy(models.Model):
    pharmacynamme = models.CharField(max_length=50)
    pharmacyaddress = models.CharField(max_length=100)
    pharmacyphone = models.IntegerField()
    
class patient(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    insurance_no = models.IntegerField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    pharmacy = models.ForeignKey(pharmacy, on_delete= models.CASCADE, default=0)
    

class appointments(models.Model):
    #patient = models.ForeignKey(patient, on_delete= models.CASCADE)
    patient = models.CharField(max_length=100)
    # doctor = models.ForeignKey(doctor, on_delete= models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    doctor = models.CharField(max_length=100)
    date = models.DateField()
    
class staff(models.Model):
    stafffname = models.CharField(max_length=100)
    stafflname = models.CharField(max_length=100)
    staffaddress = models.CharField(max_length=100)
    staffphone = models.CharField(max_length=20)
    department = models.ForeignKey(department, on_delete= models.CASCADE)


class invoice(models.Model):
    patient = models.ForeignKey(patient, on_delete= models.CASCADE)
    servicedescription = models.CharField(max_length=100)
    cost = models.IntegerField()
    
class room(models.Model):
    patient = models.ForeignKey(patient, on_delete= models.CASCADE)
    staff = models.ForeignKey(staff, on_delete= models.CASCADE)
    admissiondate = models.DateTimeField()
    
class prescription(models.Model):
    patient = models.ForeignKey(patient, on_delete= models.CASCADE)
    medication = models.CharField(max_length=100)
    date = models.DateTimeField()
    cost = models.IntegerField()
    

    