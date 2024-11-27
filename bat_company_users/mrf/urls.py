from mrf.views import *
from django.urls import path
urlpatterns=[
    path('users/',users,name='users'),
    path('user2/',user2,name='user2')
]