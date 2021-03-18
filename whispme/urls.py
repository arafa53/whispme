from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home.html'),
    path('contact',views.contact, name='contact.html'),
    path('service',views.service, name='service.html'),
    path('about',views.about, name='about.html'),
    path('signup',views.handleSignup, name='handleSignup'),
    path('login',views.handleLogin, name='handleLogin'),
    path('logout',views.handleLogout, name='handleLogout'),
    path('comment',views.homeComment, name='homeComment'),
    path('<str:slug>',views.homeviews, name='homeviews'),

]