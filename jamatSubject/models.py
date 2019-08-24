from django.db import models

class Jamaat(models.Model):
    jamaatid = models.AutoField(primary_key=True)
    jamaatname = models.CharField(max_length=50)
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField()
    createuserid = models.IntegerField()
    updateuserid = models.IntegerField()

    class Meta:
        db_table = 'Jamaat'

class Subject(models.Model):

    SubjectID = models.AutoField(primary_key=True)
    SubjectName = models.CharField(max_length=50)
    SubjectNameUrdu = models.CharField(max_length=50)
    SubjectDescription = models.CharField(max_length=300)
    jamaatid = models.ForeignKey(Jamaat, models.DO_NOTHING, db_column='jamaatid')
    MaxMark = models.IntegerField()
    createtime = models.DateTimeField()
    updatetime = models.DateTimeField()
    createuserid = models.IntegerField()
    updateuserid = models.IntegerField()

    class Meta:
        db_table = 'Subject'
