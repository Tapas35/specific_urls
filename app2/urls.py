from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path('fun1/',fun1,name='fun1')
]