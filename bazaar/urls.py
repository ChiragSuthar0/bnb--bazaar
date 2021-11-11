from django.urls import path
from . import views
urlpatterns = [

    path('', views.index),
    path('loginsignup/', views.loginsignup),
    path('signup/', views.signup),
    path('loginuser/', views.loginuser),
    path('logoutuser/', views.logoutuser),
    path('profile/', views.profile),
    path('letsprofile/', views.letsprofile),
    path('buy/', views.buy),
    path('sell/', views.sell),
    path('letssell/', views.letssell),
    path('news/', views.news),
    path('winner1/', views.winner1),
    path('winner2/', views.winner2),
    path('winner3/', views.winner3),
    path('letsbuy/', views.letsbuy),
    path('letsbuymb/', views.letsbuymb),
    path('letsupdatetime/', views.letsupdatetime),
    path('letsupdatetext/', views.letsupdatetext),
]
