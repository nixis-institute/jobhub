from django.shortcuts import render, render_to_response, HttpResponse
from app.models import *
# Create your views here.
def job_posting (request):
    job = JOB_POSTING.objects.all()
    return render_to_response("job_posting.html",{"job":job})

def job_application (request):
    job = job_application.objects.all()
    return render_to_response("job_application.html",{"job":job})
def home (request):
    return render_to_response("home.html")
def layout (request):
    return render_to_response ("layout.html")