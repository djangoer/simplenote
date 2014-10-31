from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
admin.autodiscover()


urlpatterns = patterns('',    
    url(r'^login/$','django_cas_ng.views.login',name='auth_login'),
    url(r'^logout/$','django_cas_ng.views.logout',name='auth_logout'),
    url(r'^admin/', include(admin.site.urls)),
)
from notes.views import MyHome
urlpatterns += patterns('notes.views',
    url(r'^$', MyHome.as_view(), name='home'),     
    url(r'^accounts/profile/$',MyHome.as_view(), name="profile"),
    url(r'^\+(.{5,500})$','url_note'),
    url(r'^ext/$','ext_note'),
    url(r'^ajx/$','ajx',name="ajax_load_to_div"),
    url(r'^deletefolder/$','deletefolder',name="delete_folder") 
)

urlpatterns += patterns('note.views',
    #plese check whar is addnote//
    url(r'^doc/$', TemplateView.as_view(template_name="graphics.html"),name='documentation'),    
    url(r'^addnote/(new|\d+)/$', 'addnote',name='add_note'),
    url(r'^deletenote/$', 'delnote',name='delete_note'),   
    url(r'^publicnote/$', 'public',name='public_home'),
    url(r'^note/(\d+)/', 'publicnote',name='public_note'),
    url(r'^users/$', 'userlist',name='user_list'),
    url(r'^user/(\d+)/$', 'usernotes',name='user_notes'),    
    url(r'^tags/$', 'taglist', name='tags'),
    url(r'^addfolder/$', 'addfolder', name='add_folder'), 
)
from userprofile.views import profileUpdate
urlpatterns += patterns('userprofile.views',
    url(r'^profile/settings/$', 'profile',name='user_profile'),
    url(r'^profile/uploadpic/$', 'uploadpic',name='upload_pic'),
    url(r'^profile/update/$', profileUpdate.as_view(), name='profile_update'),    
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#########################
 #       existing_user_email=User.objects.filter(email__iexact=email)
 #       if existing_user_email:
 #           if existing_user_email[0].password=='!' and existing_user_email[0].is_active:
 #               print ('this user already regiterred using some other socialauth')


        ########################
#@receiver(user_activated)
#def testmsg(**kwargs):
    #if kwargs['user'].username=='!':
    #folder1, created1 = Folder.objects.get_or_create(user = instance,name='url')
    #folder2, created2 = Folder.objects.get_or_create(user = instance,name='public')
    #print "profile %s created = %s" % (str(folder2), str(created2))


# site map stuffs
from note.sitemap import NoteSitemap
sitemaps = {
    'static': NoteSitemap,
}

urlpatterns += patterns('',
 url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
 )
