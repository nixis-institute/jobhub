from django.shortcuts import render, render_to_response, HttpResponse,HttpResponseRedirect
from app.models import *
from app.models import job_application as japp
from django.contrib.auth.models import User  # to get user table
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from app.forms import *

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
    return render_to_response ('detail.html',{"job": data})
def Login(request):
    return render(request,"registration/login.html")

def auth(request):                 #use to create a user
    username = request.POST.get('username')
    password = request.POST.get('password')    
    user = authenticate(username = username,password = password)

    if user is not None:
        login(request,user)
        return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/accounts/login/")
def employerhome(request):
    data = JOB_POSTING.objects.all()
    return render_to_response("employer/employerhome.html",{"job":data})

def create (request):
    return render_to_response ("employer/create.html")

def application(request,pk):
    userid = request.user.id
    jobid = pk
    japp.objects.create(user_applied_id = userid,job_id_id = jobid)
    return HttpResponse("You are successfully applied job")

def Registration(request):
    form=Registrationform(request.POST or None)
    c = {'form':form}
    if request.method =='POST':
        #print(form)
        form=Registrationform(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/accounts/login/")
        else:
            return HttpResponseRedirect('/accounts/registration/')    
    else:
        return render(request,'registration/registration.html',c);
             


def abc(request):
    return render_to_response("xyz.html")




    #icons
    #banner
    #rupees
    #alignment
    #calender
    #screenbtn
    