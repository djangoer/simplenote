from django import template
from BeautifulSoup import BeautifulSoup
import markdown as mkdn
from django.utils.safestring import mark_safe
from note.models import Notes,Tag
from django.conf import settings
from django.core.urlresolvers import reverse
register = template.Library()

@register.filter
def markdown(value,smode=None):
    return mark_safe(mkdn.markdown(value, safe_mode='escape'))

@register.filter
def markdown_to_plaintext(value):	
	html = mkdn.markdown(value)
	return ''.join(BeautifulSoup(html).findAll(text=True))

@register.filter
def note_count_in_folder(fdid,usr):	
	return Notes.objects.filter(user_id=usr,folder_id=fdid).count()

@register.filter
def getthumbnail(usr,pixel):
    try:
        pix='_%s.jpg' %pixel
        profile=usr.profilepicture
        prof=settings.MEDIA_URL +profile.avatar.name[:-4]+pix
    except:prof=settings.STATIC_URL +'images/no_avatar'+pix
    return prof

#template tag
@register.simple_tag
def create_pagination(paginator,curpage):
	#p.num_pages
    totalp=paginator.num_pages()#pages.total_count()
    head='<div id="light-pagination" class="pagination light-theme simple-pagination"><ul>'
    if totalp < 8:
        for page in range(1,totalp+1):
            if page==curpage:
                head+='<li class="active"><span class="current">%s</span></li>' %page
            else:
                head+='<li><a href="?page=%s" class="page-link">%s</a></li>' %(page,page)    
    return head+'</ul></div>'

def seperate_ActiveInactiveTags(taglist):
    #INPUT
    #taglist=[(3,1,'git'),(0,4,'os'),........]
    taglist.sort(reverse=True)
    #nonotes_tag,notes_tag='',''
    for c,i in enumerate(taglist):
        if i[0]==0:
            if c==0:return (taglist,'')
            notes_tag= taglist[:c]
            nonotes_tag=taglist[c:]
            return (nonotes_tag,notes_tag)
    return ('',taglist)


@register.simple_tag
def create_tagmenu(usr=None):
    tgs=Tag.objects.all()
    if not tgs:return ''
    taglist=[(Notes.objects.filter(tags=tg,user__id=usr).distinct().count(),tg.pk,tg.name) for tg in tgs]
    nonotes_tag,notes_tag=seperate_ActiveInactiveTags(taglist)
    str_html=''
    turl=reverse('home')
    for tg in notes_tag:
        str_html+='<li><a href="{url}?tags={tag[1]}&curfolder=all"><span class="label label-warning">{tag[2]}</span> x {tag[0]}</a></li>'.format(tag=tg,url=turl)
    return str_html

@register.simple_tag
def create_taglist(usr=None,private=None):
    tgs=Tag.objects.all()
    if not tgs:return ''  
    if private:
        taglist=[(Notes.objects.filter(tags=tg,user=usr).distinct().count(),tg.pk,tg.name) for tg in tgs]
        turl=reverse('home')
    elif usr:
        taglist=[(Notes.objects.filter(tags=tg,folder__name='public',user__id=usr).distinct().count(),tg.pk,tg.name) for tg in tgs]
        turl=reverse('user_notes', args=[usr])#neeed to chage
    else:
        taglist=[(Notes.objects.filter(tags=tg,folder__name='public').distinct().count(),tg.pk,tg.name) for tg in tgs]
        turl=reverse('public_home')
    nonotes_tag,notes_tag=seperate_ActiveInactiveTags(taglist)
    str_html=''
    for tg in notes_tag:
        #<a href="{% url 'home' %}?tags={{ tag.pk }}&curfolder=all">
        str_html+='<a href="{url}?tags={tag[1]}" style="text-decoration:none;"><span class="label label-info">{tag[2]}</span></a> x {tag[0]}, '.format(tag=tg,url=turl)
    if private and nonotes_tag:
        str_html+='<hr /><p class="lead">Tags that not used for any notes:</p>'
        for tg in nonotes_tag:str_html+=' <span class="label label-default">{0}</span>'.format(tg[2])
        str_html+='<p class="text-danger"> Warning if a tag does not used for any notes for one month it will be automatically deleted.</p>'    
    return str_html
