from django.db import models

# Create your models here.
class employeedetails(models.Model):

    emp_name=models.CharField(max_length=30)
    emp_address=models.CharField(max_length=20)
    emp_id=models.IntegerField()
    emp_contact_no=models.IntegerField()
    def __str__(self):
        return self.emp_name