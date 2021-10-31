from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from note.models import Notes,Folder,Tag
from note.views import limit_data
from django.db.models import Q
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.generic.base import View
from django.contrib import messages
from django.contrib.auth import authenticate, login

class MyHome(View):        
    '''The user home page. For root url this view will be called.'''
    def get(self, request):
    	if not request.user.is_active:
    		return HttpResponseRedirect(reverse('documentation'))
    	tg=Folder.objects.filter(user=request.user).exclude(name__regex=r'^(public|url)$').order_by('name')	
    	
    	#if somebody called simlenote.in/?tags=1&curfolder=all
    	#i need to pass `curfolder as next,page,tags` to `home.html`
    	#Home.html will call on ajax:
    	#var url='/ajx/?curfolder='+ $(this).data('ajxurl'); $('#ajaxBox').load(url); 
    	#view ajax supports - tags,curfolder
    	#/ajx/?curfolder={{next}}&page={{page}}{% if tags %}&tags={{tags}}{% endif %}
    	return render(request,'home.html',{'folders':tg,
			'next':request.GET.get('curfolder','all'),'page':request.GET.get('page',1),
			'tags':request.GET.get('tags','')})

#ajax loading into lovely-things-list
@login_required
def ajx(request):
	curfolder=request.GET['curfolder']
	tag=''
	if curfolder=='all':nts=Notes.objects.filter(user=request.user).order_by('-created')
	else:
		#if 'tags' in request.GET:
		#	print('tags')
		#	nts=Notes.objects.filter(user=request.user,tags__in=request.GET.getlist('tags'),folder__name=curfolder).distinct()
		nts=Notes.objects.filter(user=request.user,folder__name=curfolder).order_by('-created')
	if 'tags' in request.GET:
		nts=nts.filter(tags__in=request.GET.getlist('tags'))
		tag=Tag.objects.filter(id__in=request.GET.getlist('tags'))
	notes=limit_data(request.GET.get('page',1),nts)
	return render(request,'folder_contents.html',{'notes':notes,'cfolder':curfolder,'tag':tag,
			'mainfolders':['all','url','public']})
		
@login_required
def url_note(request,urlnote):
	# splitted=urlnote.split('/',1)
	# note=splitted[0] 
	
	m_folder=Folder.objects.get(user=request.user,name='url')
	Notes(user=request.user,title="Note Saved through URL.",folder=m_folder, note= urlnote).save()	
	messages.success(request, 'Notes saved successfully')
	
	return HttpResponseRedirect(reverse('home'))

#save note from browser extension.
def loadforms(usr):
	folders=Folder.objects.filter(user=usr)
	tags=Tag.objects.all()
	folderlist=[i.name for i in folders]
	taglist=[i.name for i in tags]
	return {"islogin": 'yes','folderlist':folderlist,'taglist':taglist}

@csrf_exempt
def ext_note(request):
	#login check
	print('called ext_note')
	if 'username' in request.POST:
		username = request.POST['username']
		password = request.POST['password']
		print(username,password)
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				print('login success')
				n=loadforms(user)
				# Redirect to a success page.	
			else:
				# Return a 'disabled account' error message
				n={"islogin": 'no','msg':'disabled account' }				
		else:
			# Return an 'invalid login' error message.
			n={"islogin": 'no','msg':'invalid username or password' }
		return HttpResponse(json.dumps(n), content_type="application/json")

	if 'type' in request.POST:
		if request.user.is_authenticated():
			n=loadforms(request.user)
			return HttpResponse(json.dumps(n), content_type="application/json")
			#return HttpResponse('yes')
		#return HttpResponse('no')		
		return HttpResponse(json.dumps({"islogin": 'no','msg':'Please Login.'}), content_type="application/json")
	#print(request.POST['folder'],request.user.username)
	m_folder=Folder.objects.get(user=request.user,name=request.POST['folder'])
	print('going to prin taglist')
	tgs=request.POST.getlist('tag')
	for t in tgs[0].split(','):
		print(t)

	tags=Tag.objects.filter(name__in=tgs[0].split(','))
	print(tags)
	try:
		nt=Notes(user=request.user,title=request.POST['title'],folder=m_folder, note=request.POST['note'])
		nt.save()
		for tg in tags:nt.tags.add(tg)
		return HttpResponse('success')
	except:
		return HttpResponse('failed')
	
@login_required
def deletefolder(request):	
	if request.method=='POST':
		if request.POST['fname1']==request.POST['fname2']:
			fd=Folder.objects.get(user=request.user,name=request.POST['fname1'])
			Notes.objects.filter(user=request.user,folder=fd).delete()
			fd.delete()
			messages.success(request, 'folder deleted successfully.')
			return HttpResponseRedirect(reverse('home'))
		messages.error(request, 'Folders did not match.')
	return render(request,'folder_delete.html',{'fn':request.GET['fname']})