from django.db import models

class DepartmentModel(models.Model):
    name =models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
    
class TecharModel(models.Model):
    t_name = models.CharField(max_length=50,null=True)
    t_dept = models.CharField(max_length=50,null=True)
    t_email =models.EmailField(max_length=254,null=True)
    t_phone =models.IntegerField()
    bio =models.TextField()

    def __str__(self):
        return self.t_name
    
class StudentModel(models.Model):
    s_name = models.CharField(max_length=50, null=True)
    s_dept = models.CharField(max_length=50, null=True)
    s_email =models.EmailField(max_length=254, null=True)
    s_phone =models.IntegerField()

    def __str__(self):
        return self.s_name

    
    