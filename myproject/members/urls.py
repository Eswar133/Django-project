from django.urls import path
from . import views 
app_name = "myapp1"

urlpatterns=[
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
]