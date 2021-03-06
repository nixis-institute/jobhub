"""jobhub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from app.views import *
from app.models import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('about',about,name="about"),
    path('job_application',job_application,name="job_application"),
    path('layout',layout,name="layout"),
    path("job/<int:pk>/",detail_job,name="detail"),
    path("accounts/login/",Login,name="login"),
    #path("accounts/registration/",Registration,name="login"),
    path("authentication/",auth,name="auth"),
    path("employer",employerhome,name="emp"),
    path("employer/create",create,name="create"),
    path("accounts/registration/",reg,name="reg"),
    path("/registration/suc_reg/",suc_reg,name="suc_reg"),
    path('applied/<int:pk>/',application,name="applied"),
    path("accounts/logout/",logout,name="logout"),
    path("accounts/profile/",profile,name="profile"),
    path("posting/",posting,name="posting"),
    path("searching/",searching,name="searching"),
    ]
