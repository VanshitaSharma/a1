from .models import Notice
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    #hello world show the server without used any templates and files
    #return  HttpResponse('hello world')
    #return render(request,'app1/home.html')
    #html pages linked to the server used render functon..
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
class NoticeListView(ListView):
    model=Notice

@method_decorator(login_required,name="dispatch")
class NoticeDetailView(DetailView):
    model=Notice
