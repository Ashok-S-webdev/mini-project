from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
   email = models.EmailField(unique=True)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []
   is_donor = models.BooleanField("Is Donor", default=False)
   is_recipient = models.BooleanField("Is Recipient", default=False)


class Organs(models.Model):
   name = models.CharField(max_length=20)
   is_checked = models.BooleanField(default=True)


class Recipient(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
   email = models.EmailField(max_length=150, null=True)
   first_name = models.CharField(max_length=60)
   last_name = models.CharField(max_length=60)
   dob = models.DateField(null=True)
   age = models.IntegerField(null=True)
   gender = models.CharField(max_length=10)
   mobile = models.CharField(max_length=10)
   blood_group = models.CharField(max_length=3)
   aadhaar = models.CharField(max_length=12)
   addr_line = models.CharField(max_length=100)
   city = models.CharField(max_length=60)
   district = models.CharField(null=True ,max_length=60)
   state = models.CharField(max_length=60)
   pincode = models.CharField(max_length=6)
   organ_needed = models.CharField(max_length=20)
   medical_history = models.TextField(max_length=200)
   medical_condition = models.TextField(max_length=200)


   def __str__(self):
      return (f"{self.first_name} {self.last_name}")
   

class Donor(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
   email = models.EmailField(max_length=150, null=True)
   first_name = models.CharField(max_length=60)
   last_name = models.CharField(max_length=60)
   dob = models.DateField(null=True)
   age = models.CharField(max_length=2 ,null=True)
   gender = models.CharField(max_length=10)
   mobile = models.CharField(max_length=10)
   blood_group = models.CharField(max_length=3)
   aadhaar = models.CharField(max_length=12)
   addr_line = models.CharField(max_length=100)
   city = models.CharField(max_length=60)
   district = models.CharField(null=True, max_length=60)
   state = models.CharField(max_length=60)
   pincode = models.CharField(max_length=6)
   organ = models.ManyToManyField(Organs, related_name='organ')
   medical_history = models.TextField(max_length=200)
   social_history = models.TextField(max_length=200)


   def __str__(self):
      return (f"{self.first_name} {self.last_name}")


