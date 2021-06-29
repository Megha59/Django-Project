from django.db import models
    
class doctor(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=10)
    doctorid= models.IntegerField()
    def __str__(self) :
        return self.firstname	

class patient(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=10)
    patientid= models.IntegerField()
    doctorid = models.ForeignKey(doctor, on_delete=models.CASCADE)

    def __str__(self) :
        return self.firstname