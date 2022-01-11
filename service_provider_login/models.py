from django.db import models
from django.forms import ModelForm
# Create your models here.
class ServiceCreds(models.Model):
    full_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=10)
    service = models.CharField(max_length=20)
    details=models.CharField(max_length=300,default="We are great at what we do!")
    total_slots=models.IntegerField(default=0)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.user_name

class ServiceCredsForm(ModelForm):
    class Meta:
        model=ServiceCreds
        fields='__all__'
