from django.db import models
# null=False,blank=False
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    dob = models.dateField(null=True,blank=True)
    email = models.EmailField()
    desc = models.TextField()
    desc = models.TextField()
    is_verify = models.BooleanFiled(default=False)