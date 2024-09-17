from django.db import models

# Create your models here.
class Job(models.Model):
    clientid=models.AutoField(primary_key=True)
    clientname=models.CharField(max_length=150)
    contact=models.CharField(max_length=150)
    rdate=models.CharField(max_length=150)
    inventry=models.CharField(max_length=150)
    image=models.ImageField()
    issue=models.TextField(max_length=5000)
    cnotes=models.TextField(max_length=5000)
    technician=models.CharField(max_length=150)
    ddate=models.CharField(max_length=100)
    amount=models.CharField(max_length=20)
    status=models.CharField(max_length=50)

    def __str__(self):
        return self.clientname