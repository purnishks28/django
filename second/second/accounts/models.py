from django.db import models
# default --> null = False, blank = False
GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
    ('not specified','not specified'))

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField()
    desc = models.TextField()
    salary = models.FloatField()
    is_verify = models.BooleanField(default=False)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=50,default='not specified')
    documents = models.FileField(upload_to='documents/', default='default.jpg')
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)


# Create your models here.
