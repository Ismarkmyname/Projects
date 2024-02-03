from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.home, name="home"), # don't put the location of the home page so that it can be the landing page i tried it already a million times it did not work that's why you created a duplicated that do the exact opposite
    path("home/", views.home, name="home"),# we can put the link of the home page so when you click the home button on the other page you can still go back and won't how the error 404 it's basically the same code on the first one
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("todos/", views.todos, name="Todos"),
    path("videos/", views.videos, name="videos")
    
]   