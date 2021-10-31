
from django.urls import include, path
from . import views

urlpatterns = [
	path('settings/', views.profile,name='user_profile'),
    path('uploadpic/', views.uploadpic,name='upload_pic'),
    path('update/', views.profileUpdate.as_view(), name='profile_update'),  
    path('login/', views.social_login,name="auth_login"),  
]