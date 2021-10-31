
from django.urls import include, path
from . import views

urlpatterns = [
    
    path('addnote/<ntid>/', views.addnote,name='add_note'), # url(r'^addnote/(new|\d+)/$', 'addnote',name='add_note'),
    path('deletenote/', views.delnote,name='delete_note'),   
    path('publicnote/', views.public,name='public_home'),
    path('note/<int:userpk>/', views.publicnote,name='public_note'),
    path('users/', views.userlist,name='user_list'),
    path('user/<int:userpk>/', views.usernotes,name='user_notes'),    
    path('tags/', views.taglist, name='tags'),
    path('addtag/', views.addtag, name='add_tag'), 
    path('addfolder/', views.addfolder, name='add_folder'), 
]
