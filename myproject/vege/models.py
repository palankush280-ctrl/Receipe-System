from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Receipe(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to ="receipe")
    receipe_view_count = models.IntegerField(default = 1)


class Department(models.Model):
    department = models.CharField(max_length = 100)

    def __str__(self):
        return self.department
    
    class meta:
        ordering = ['department']

class Student_id(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self):
        return self.student_id
    
class Student(models.Model):
    department = models.ForeignKey(Department,related_name = "depart",on_delete=models.CASCADE)
    student_id = models.OneToOneField(Student_id,related_name = "studentid",on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=20)
    student_address = models.TextField()

    def __str__(self):
        return self.student_name
    
    class meta():
        ordering = ['student_name']
        verbose_name = "student"