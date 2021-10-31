# Create your views here.
from PIL import Image as PImage
from os.path import join as pjoin
from userprofile.models import ProfilePicture,GMapLocation,ProfileDetails
from userprofile.forms import ProfilePictureForm,GMapLocationForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from django.http import HttpResponseRedirect
import os
from django.views.generic.base import View
from django.contrib import messages

def social_login(request):
	return render(request,'userprofile/login.html')

def profile(request):

	#p_details=ProfileDetails.objects.get()
	return render(request,"userprofile/home.html")

def resize_and_crop(fname,coords,oldfn):
    """
    Resize and crop profile picture.
    coords=33,44,22,33   ---x:33,y:22,x2:3,y2:4,w:33,h:32    
    >>> x=[int(i) for i in coords.split(',')]
    """
    im = PImage.open(fname)
    #box = (50, 50, 200, 300) #x1,y1,x2,y2
    box=[int(i) for i in coords.split(',')]
    region = im.crop(box)
    if oldfn:
    	#delete oldfiles    	
    	os.remove(oldfn[:-4]+'_crop.jpg')
    	os.remove(oldfn[:-4]+'_160.jpg')
    	os.remove(oldfn[:-4]+'_48.jpg')
    region.save(fname[:-4]+'_crop.jpg',"JPEG")
    region.thumbnail((160,160), PImage.ANTIALIAS)
    region.save(fname[:-4]+'_160.jpg', "JPEG")
    region.thumbnail((48,48), PImage.ANTIALIAS)
    region.save(fname[:-4]+'_48.jpg', "JPEG")
    #im.thumbnail((160,160), PImage.ANTIALIAS)
    #im.save(fname[:-4]+'_160.jpg', "JPEG")

@login_required
def uploadpic(request):
	#if created:img = pjoin(settings.MEDIA_URL,"nopicture.jpg")
	#else:img = settings.MEDIA_URL + profile.avatar.name
	if request.method == "POST":		
		try:
			pf = ProfilePictureForm(request.POST, request.FILES,instance=request.user.profilepicture)
			oldname=pjoin(settings.MEDIA_ROOT, request.user.profilepicture.avatar.name)
		except:
			profile = ProfilePicture(user=request.user)
			pf = ProfilePictureForm(request.POST, request.FILES,instance=profile)
			oldname = ''
		if pf.is_valid():
			pf.save()
			# resize and save image under same filename
			imfn = pjoin(settings.MEDIA_ROOT, request.user.profilepicture.avatar.name)			
			resize_and_crop(imfn,request.POST['cropcoords'],oldname)
			request.user.profilepicture.avatar.delete(save=False)		
			return HttpResponseRedirect(reverse('user_profile'))
	else:
		try:pf = ProfilePictureForm(instance=request.user.profilepicture)
		except:pf = ProfilePictureForm()
	return render(request,"userprofile/uploadpicture.html", {'pf':pf})


class profileUpdate(View):
	def get(self, request):
		try: 
			prof=request.user.profiledetails			
			d=dict(first_form=ProfileForm(instance=prof), 
				second_form=GMapLocationForm(instance=prof.location))
			#d['tempid']=prof.id
			d['loc']=prof.location.address
		except:
			d=dict(first_form=ProfileForm(),second_form=GMapLocationForm())
		return render(request,'userprofile/updateprofile.html',d)

	def post(self,request):
		print(request.POST['dob'])
		form1=ProfileForm(request.POST)
		form2=GMapLocationForm(request.POST)
		if form1.is_valid() and form2.is_valid():
			#obj, created = ProfileDetails.objects.get_or_create(name=tname)
			try:
				prof=request.user.profiledetails
				loc=prof.location
			except:
				loc=GMapLocation()
				prof=ProfileDetails(user=request.user)

			GMapLocationForm(request.POST,instance=loc).save()
			prof.location=loc
			frm_prof=ProfileForm(request.POST,instance=prof)
			obj=frm_prof.save()
			messages.add_message(request, messages.SUCCESS, 'Updated Profile Successfully.')
			return HttpResponseRedirect(reverse('user_profile'))
		d=dict(first_form=form1,second_form=form2)
		return render(request,'userprofile/updateprofile.html',d)