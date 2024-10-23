from django.shortcuts import render
from django.http import HttpResponse 


# Create your views here.
def index(request): 
    print('inex function in hello world is running')
    if request.method == "GET":
        return request.method
    elif request.method == "POST":
        return HttpResponse("You have POSTed something.")
 