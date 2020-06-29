from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    #hello world show the server without used any templates and files
    #return  HttpResponse('hello world')
    #return render(request,'app1/home.html')
    #html pages linked to the server used render functon..
    return render(request,'app1/home.html',{"name":"vanshita"})
