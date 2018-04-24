from django.contrib import admin
from django.urls import path
from forum import views

urlpatterns = [
    path('threads', views.ShortThreadList.as_view(), name="shortthread-list"),
    path('threads/<int:pk>', views.Thread.as_view(), name="thread"),
    path('add', views.Add.as_view(), name='Add')                                                                                              
]
