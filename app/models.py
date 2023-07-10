from django.db import models

# Create your models here.
class Department(models.Model):
    dno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.dname

class Employee(models.Model):
    dno=models.ForeignKey(Department,on_delete=models.CASCADE)
    eno=models.IntegerField()
    ename=models.CharField(max_length=100)
    ejob=models.CharField(max_length=25)
    esal=models.IntegerField()
    def __str__(self) -> str:
        return self.ename


