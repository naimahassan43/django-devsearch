from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse('Here are our products')
def project(request,pk):
    return HttpResponse('Here is our single product' +' '+ str(pk))
# Create your views here.
