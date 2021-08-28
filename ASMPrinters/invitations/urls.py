
from django.urls import path, include
from invitations import views


urlpatterns = [ 
    #html
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('order/', views.orderbook, name='orderbook'),
    path('ordersts/', views.ordersts, name='ordersts'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('user/', views.userpage, name='userpage'),
    path('visit/', views.visit, name='visit'),
    

    #backend
    path('add/', views.addC, name='addC'),
    path('view/', views.viewall, name='viewall'),
    path('getone/<fetchid>', views.getSingle, name='getSingle'),
    path('status/', views.search, name='search'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.updatepro, name = 'updatepro'),
    path('updateaction/', views.updateact, name = 'updateact'),
    path('del/', views.delete, name = 'delete'),
    path('deleteact/', views.delact, name = 'delact'),

    
]