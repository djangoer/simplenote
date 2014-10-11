#admin.py
from django.contrib import admin
from note.models import Notes,Tag,Folder
admin.site.register(Notes)
admin.site.register(Tag)
admin.site.register(Folder)
from userprofile.models import ProfilePicture,GMapLocation,ProfileDetails

admin.site.register(ProfilePicture)
admin.site.register(ProfileDetails)
admin.site.register(GMapLocation)

