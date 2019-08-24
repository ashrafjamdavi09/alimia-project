from django.db import models

class Student(models.Model):
    StudentID = models.AutoField(primary_key=True)
    StudentFirstName = models.CharField(max_length=50)
    StudentMiddleName = models.CharField(max_length=50, blank=True, null=True)
    StudentLastName = models.CharField(max_length=50, blank=True, null=True)
    FathersName = models.CharField(max_length=50)
    RollNumber = models.CharField(max_length=50)
    RegistrationID = models.IntegerField()
    studentemailid = models.CharField(max_length=50, blank=True, null=True)
    studentphonenumber = models.CharField(max_length=13, blank=True, null=True)
    homephonenumber = models.CharField(max_length=13, blank=True, null=True)
    aadharnumber = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, blank=True, null=True)
    pincode = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        db_table = 'Student'
