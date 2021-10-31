from django.urls import include, path, re_path
from django.contrib import admin
from django.views.generic import TemplateView
from notes import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.MyHome.as_view(), name='home'),
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')), 
    path('doc/', TemplateView.as_view(template_name="graphics.html"),name='documentation'),  
    path('notes/', include('note.urls')),
    path('profile/', include('userprofile.urls')),
    path('logout/', LogoutView.as_view(),name="auth_logout"),
    
    # path('logout/', 'django.contrib.auth.views.logout',name="auth_logout"),
    # path('schools/', include(('schools.urls','schools'),namespace='schools')),

    path('accounts/profile/', views.MyHome.as_view(), name="profile"),    
    path('ext/',views.ext_note),
    path('ajx/',views.ajx,name="ajax_load_to_div"),
    path('deletefolder/',views.deletefolder,name="delete_folder"), 
    re_path(r'^\+(?P<urlnote>.{5,500})$',views.url_note),
]


# site map stuffs
from django.contrib.sitemaps.views import sitemap
from note.sitemap import NoteSitemap
sitemaps = {
    'static': NoteSitemap,
}
from django.contrib.sitemaps.views import sitemap
urlpatterns += [
  re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()