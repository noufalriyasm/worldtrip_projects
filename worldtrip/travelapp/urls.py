

from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    #path('add/',views.result,name="result"),
    #path('contact/',views.contact,name="contact")
]
