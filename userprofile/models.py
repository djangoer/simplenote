from django.db import models
from django.contrib.auth.models import User


class ProfilePicture(models.Model):
    avatar = models.ImageField("Profile Pic", upload_to="images/")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user = models.ForeignKey(User)
    #uploaddate=models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.user

class GMapLocation(models.Model):
    address=models.CharField(max_length=200, blank=True)
    locality=models.CharField(max_length=40, blank=True)#
    district=models.CharField(max_length=40, blank=True)#
    state=models.CharField(max_length=40, blank=True)#
    country=models.CharField(max_length=20, blank=True)#
    postal_code=models.CharField(max_length=20, blank=True)#
    lat=models.CharField(max_length=20, blank=True)#
    lng=models.CharField(max_length=20, blank=True)#


class ProfileDetails(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	dob = models.DateField(blank=True,null=True)
	#email = models.EmailField(max_length=50, blank=True)
	location =models.OneToOneField(GMapLocation, on_delete=models.CASCADE)
	website=models.CharField(max_length=50, blank=True)	
	summary=  models.TextField()
	phone=models.CharField(max_length=15, blank=True)



