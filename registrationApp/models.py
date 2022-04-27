import email
from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    firstName = models.CharField(max_length=24)
    lastName = models.CharField(max_length=24)
    age = models.IntegerField()
    sex = models.CharField(max_length=24)
    profession = models.CharField(max_length=24)
    phone = PhoneNumberField()
    email = models.EmailField(max_length=254)
    haveWork = models.BooleanField(default=False)
    createdDate = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("done")
    
    def changeWorkStatus(self):
        if self.haveWork == True:
            self.haveWork = False
        else:
            self.haveWork = True
        self.save()