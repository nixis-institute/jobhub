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


def logout(request):
    return render_to_response("registration/logout.html")


def job_application (request):
    job = job_application.objects.all()
    return render_to_response("job_application.html",{"job":job})

@login_required
def home (request):
    data = JOB_POSTING.objects.all().order_by('-date')
    return render(request,'home.html',{"job":data})
def post (request):
    return render_to_response('post.html',{"job":data})
def about(request):
    if request.method=="POST":
        title= request.post.get("title")
        name= request.post.get("name")
        address= request.post.get("address")
        phone_no= request.post.get("phone_no")
        return render_to_response("/")


    return render_to_response('about.html')

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
    if request.method=="POST":
        title = request.POST.get("title")
        name = request.POST.get("name")
        des = request.POST.get("description")
        mail = request.POST.get('email')
        contact = request.POST.get("contact")
        exp = request.POST.get('exp')
        loc = request.POST.get('location')
        JOB_POSTING.objects.create(title=title,name=name,discription=des,mail=mail,contact=contact,exp=exp,location=loc,employer_id=request.user.id)
        return HttpResponseRedirect("/employer")
        
    else:    
        return render(request,"employer/create.html")

def application(request,pk):
    userid = request.user.id
    jobid = pk
    japp.objects.create(user_applied_id = userid,job_id_id = jobid)
    return HttpResponse("<h2 style='text-align:center'>You are successfully applied job click <a href='/'>here</a> to home page</h2>")

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
def suc_reg(request):
    return render_to_response('/registration/suc_reg')
             
def searching(request):
    search=request.POST.get("search")
    data = JOB_POSTING.objects.filter(title__contains=search)
    return render(request,"home.html",{"search":data,"key":search})
    
    #return HttpResponse(data)
@login_required
def profile(request):
    #data = User.objects.get(request)
    data = request.user
    return render_to_response("registration/profile.html",{'user':data})
@login_required
def reg(request):
    if request.method=="POST":
        user_name = request.POST.get("user_name")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password_1 = request.POST.get("password_1")
        password_2 = request.POST.get("password_2")
        user_type = request.POST.get("user_type")
        return render_to_response ("registration/suc_reg.html")
        #JOB_POSTING.objects.create(user_name=user_name,first_name=first_name,last_name=last_name,email=email,password_1=password_1,password_2=password_2,user_type=user_type)
        #return render_to_response ("registration/profile.html",{'user':data})
        
    else:    
        return render(request,"registration/reg.html")


 

def posting (request):
    if request.method=="POST":
        title = request.POST.get("title")
        name = request.POST.get("name")
        des = request.POST.get("description")
        mail = request.POST.get('email')
        contact = request.POST.get("contact")
        exp = request.POST.get('exp')
        loc = request.POST.get('location')

        JOB_POSTING.objects.create(title=title,name=name,discription=des,mail=mail,contact=contact,exp=exp,location=loc,employer_id=1)
        return HttpResponseRedirect("/")
        
    else:    
        return render(request,"registration/posting.html")


