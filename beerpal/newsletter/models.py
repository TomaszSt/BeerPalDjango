from django.db import models

# Create your models here.

class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=255,blank=False,null=False)
    date_created = models.DateTimeField(auto_now_add=True,auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    agreement = models.IntegerField()

    def __unicode__(self):
        return self.email