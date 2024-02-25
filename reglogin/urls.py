from django.urls import path, include
from . import views


urlpatterns = [
   
   path ('',views.registration, name='registration'),
   
   path ('login/',views.UserLoginView.as_view(), name='login'),
   path ('profile/',views.profile, name='profile'),
   path ('userlogout/',views.user_logout, name='userlogout'),
   
   
]