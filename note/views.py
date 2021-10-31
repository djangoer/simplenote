# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from note.models import Notes,Folder,Tag
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from userprofile.models import ProfilePicture
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json,re
from django.contrib import messages

@login_required
def addnote(request,ntid):	
	if request.method=='POST':		
		if 'noteid' in request.POST:
			#update note
			nt=Notes.objects.get(id=request.POST['noteid'])
			nt.folder_id=request.POST['folder']			
			nt.note=request.POST['note']
			nt.title=request.POST['title']			
			nt.tags.clear()			
		else:
			#create new note
			nt=Notes(user=request.user,folder_id=request.POST['folder'], note=request.POST['note'],title=request.POST['title'])
		nt.save()
		for tagid in request.POST.getlist('tags'):
			nt.tags.add(Tag.objects.get(id=tagid))
		return HttpResponseRedirect(reverse('home'))	
	d={'folders':Folder.objects.filter(user=request.user),'tags':Tag.objects.all()}
	if ntid != 'new':d['nt']=Notes.objects.get(id=ntid)
	return render(request,'addnote.html',d)

def delnote(request):
	try:
		Notes.objects.get(pk=request.GET['delnote']).delete()		
		resp='1'
	except:resp='Failed'
	return HttpResponse(resp)#json.dumps({"flag": resp}), mimetype="application/json")



def limit_data(page,data,n=10):
	paginator = Paginator(data,n) # Show 10 notes per page
	try:
		p_data = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		p_data = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		p_data = paginator.page(paginator.num_pages)
	return p_data

## we need to build this
def public(request):
	#Person.objects.raw('SELECT id,user,RIGHT(note,10),created FROM note_notes WHERE folder_name=')
	tags=''
	if 'tags' in request.GET:
		# get note list base on tags in post, only public notes
		#tags=request.GET.getlist('tags')
		nt=Notes.objects.filter(tags__in=request.GET.getlist('tags'),folder__name='public').order_by('-created')
		tags=Tag.objects.filter(id__in=request.GET.getlist('tags'))	
	else:nt=Notes.objects.filter(folder__name='public').order_by('-created')
	notes=limit_data(request.GET.get('page'),nt,30)
	return render(request,'public/home.html',{'notes':notes,'tags':tags})

def usernotes(request,userpk):
	usr=User.objects.get(id=userpk)
	tags=''
	folder=Folder.objects.get(user=usr,name='public')
	if 'tags' in request.GET:		
		nts=Notes.objects.filter(tags__in=request.GET.getlist('tags'),folder=folder).order_by('-created')
		tags=Tag.objects.filter(id__in=request.GET.getlist('tags'))	#filterd by	
	else:nts=Notes.objects.filter(folder=folder).order_by('-created')
	notes=limit_data(request.GET.get('page'),nts,30)#pagination	
	return render(request,'userprofile/usernotes.html',{'notes':notes,'usr':usr,'tags':tags})
##########

def publicnote(request,notepk):	
	#Person.objects.raw('SELECT id,user,RIGHT(note,10),created FROM note_notes WHERE folder_name=')
	nt=Notes.objects.get(pk=notepk)
	return render(request,'public/note.html',{'note':nt})

def userlist(request):
	usrs=User.objects.filter(is_active=True,is_superuser=False)
	return render(request,'public/users.html',{'users':usrs})

def create_new_tag(tag):
	tname = tag.lower()
	if re.match(r"\w{3,20}$", tname):
		obj, created = Tag.objects.get_or_create(name=tname)
		if created:	return 1,obj.pk
		return 0,'Error: Tag with name: %s already exist.' %tname
	return 0,'The Tag name must be between 3 and 20 Alphanumeric characters.'


@login_required
def addtag(request):
	status,message = create_new_tag(request.GET.get('tag')) 	
	return HttpResponse(json.dumps(dict(flag=status,msg=message)), content_type="application/json")

@login_required
def taglist(request):	
	if request.method=="POST":
		status,message = create_new_tag(request.POST.get('name')) 		
		if status == 1:
			messages.success(request, 'Tag added successfully.')
			return HttpResponseRedirect(reverse('tags'))
		else:
			messages.error(request, message)
	tags=Tag.objects.order_by('name')
	return render(request,'tags.html',{'tags':tags})

@login_required
def addfolder(request):
	foldername=request.GET['folder'].lower()
	if re.match(r"\w{3,20}$", foldername):
		if Folder.objects.filter(user=request.user,name=foldername):
			status,message=0,'Folder name already exist.'
		else:
			fd=Folder(user=request.user,name=foldername)
			fd.save()
			status,message=1,fd.pk
	else:status,message=0,'The Folder name must be between 3 and 20 Alphanumeric characters.'
	return HttpResponse(json.dumps(dict(flag=status,msg=message)), content_type="application/json")
