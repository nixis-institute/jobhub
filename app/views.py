from django.shortcuts import render, render_to_response, HttpResponse,HttpResponseRedirect
from app.models import *
from django.contrib.auth.models import User  # to get user table
from django.contrib.auth import authenticate, login
#from django.views.decorators import login_required
from django.contrib.auth.decorators import login_required

# Create your views here.
def job_posting (request):
    job = JOB_POSTING.objects.all()
    return render_to_response("job_posting.html",{"job":job})



def job_application (request):
    job = job_application.objects.all()
    return render_to_response("job_application.html",{"job":job})

@login_required
def home (request):
    data = JOB_POSTING.objects.all()
    return render_to_response('home.html',{"job":data})


def layout (request):
    return render_to_response ("layout.html")
def detail_job (request,pk):
    data=JOB_POSTING.objects.get(id=pk)       #to get a single record
    return render_to_response ('detail.html',{"JOB_POSTING": data})
def Login(request):
    return render(request,"registration/login.html")

def auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(username = username,password = password)

    if user is not None:
        login(request,user)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/accounts/login/")    