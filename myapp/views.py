# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

def index(request):
    message="Hello, world."
    return render_to_response('index.html',{'message' : message})

def welcome(request,username):
    message="Welcome"
    return render_to_response('welcome.html',{'message' : message, 'username': username})

def create_user(request):
    pass
