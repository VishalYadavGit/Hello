from django.db import models
# from home.views import Contact



# Create your models here.
class Contact(models.Model):
    null=True
    name_surname=models.CharField(max_length=40)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    message=models.TextField()
    date=models.DateField()
    def __str__(self):
     return self.email



#lessss gooooo