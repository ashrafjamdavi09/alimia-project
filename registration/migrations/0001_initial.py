# Generated by Django 2.2.4 on 2019-09-12 14:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jamatSubject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('registrationid', models.AutoField(primary_key=True, serialize=False)),
                ('studentfirstname', models.CharField(max_length=50)),
                ('studentmiddlename', models.CharField(blank=True, max_length=50, null=True)),
                ('studentlastname', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(default=datetime.date.today)),
                ('fathersname', models.CharField(max_length=50)),
                ('studentemailid', models.CharField(blank=True, max_length=50, null=True)),
                ('studentphonenumber', models.CharField(max_length=13)),
                ('homephonenumber', models.CharField(max_length=13)),
                ('aadharnumber', models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True)),
                ('address1', models.CharField(max_length=250)),
                ('address2', models.CharField(blank=True, max_length=250, null=True)),
                ('pincode', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('jamaatid', models.ForeignKey(db_column='jamaatid', on_delete=django.db.models.deletion.DO_NOTHING, to='jamatSubject.Jamaat')),
            ],
            options={
                'db_table': 'Registration',
            },
        ),
    ]
