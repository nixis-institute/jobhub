from django.shortcuts import render, render_to_response, HttpResponse
from app.models import *
# Create your views here.
def job_posting (request):
    return render_to_response("job_posting.html")