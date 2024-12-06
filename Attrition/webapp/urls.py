"""WebC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [ 


    path('', views.homepage, name="WelcomeHome"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('adminloginaction/', views.adminloginaction, name="adminloginaction"),
    path('adminhome/', views.adminhome, name="adminhome"),
    path('userhome/', views.userhome, name="userhome"),
    path('adminlogout/', views.adminlogout, name="adminlogout"),
    path('usignupaction/', views.usignupaction, name="usignupaction"),
    path('user/', views.user, name="user"),
    path('userloginaction/', views.userloginaction, name="userloginaction"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('usersignup/', views.usersignup, name="usersignup"),
    path('feature_selection/', views.feature_selection, name="feature_selection"),
    path('classification/', views.classification, name="classification"),

    path('nbtrain/', views.nbtrain, name="nbtrain"),
    path('dttrain/', views.dttrain, name="dttrain"),
    path('rftrain/', views.rftrain, name="rftrain"),
    path('svmtrain/', views.svmtrain, name="svmtrain"),
    path('lrtrain/', views.lrtrain, name="lrtrain"),
    path('evaluation/', views.evaluation, name="evaluation"),

    path('newcompanies/', views.newcompanies, name="newcompanies"),
    path('accept/', views.accept, name="accept"),
    path('reject/', views.reject, name="reject"),
    path('viewcompanies/', views.viewcompanies, name="viewcompanies"),


    path('attrition/', views.attrition, name="attrition"),
    path('feedbackpost/', views.feedbackpost, name="feedbackpost"),
    path('viewfeedback/', views.viewfeedback, name="viewfeedback"),
    path('viewdata/', views.viewdata, name="viewdata"),
    
    

    


    
    
    
    


    
    

   
]
