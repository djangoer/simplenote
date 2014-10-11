from django.db import models
from django.contrib.auth.models import User
#from django.template.defaultfilters import slugify
from datetime import datetime

class Tag(models.Model):
	name=models.CharField(max_length=100)
	#desc=models.TextField(blank=True)
	created = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return unicode(self.name)

class Folder(models.Model):
	user=models.ForeignKey(User)
	name=models.CharField(max_length=50)
	created = models.DateTimeField(auto_now_add=True)

class Notes(models.Model):
	#slug = models.SlugField(max_length=60, blank=True)
	user=models.ForeignKey(User)	
	tags=models.ManyToManyField(Tag)
	title=models.CharField(max_length=200)
	note=models.TextField(blank=True)
	folder=models.ForeignKey(Folder)
	created = models.DateTimeField(auto_now_add=True)
	modified= models.DateTimeField(blank=True,null=True)
	def save(self):
		self.modified = datetime.now()
		super(Notes, self).save()
	#	if not self.id:
			#Only set the slug when the object is created.
	#		self.slug = slugify(self.title[:59] if len(self.title) > 60  else self.title)
	#	super(Notes, self).save()

	def __unicode__(self):
		return unicode(self.title)

from django.db.models.signals import post_save
def create_folders(sender, **kwargs):
	curuser = kwargs["instance"]
	if kwargs["created"]:
		if not Folder.objects.filter(user=curuser):
			Folder(user=curuser,name='url').save()
			Folder(user=curuser,name='public').save()
		print ('Folders created succrssfully')
	else:
		print ("problems creating profile.")
post_save.connect(create_folders, sender = User, dispatch_uid="initial-foldercreation-signal")
