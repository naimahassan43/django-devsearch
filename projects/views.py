from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects

projectsList = [
 {
  'id': '1',
  'title': 'Ecommerce Website',
  'description': 'Fully functional website',
 },
  {
  'id': '2',
  'title': 'Multivendor Ecommerce Website',
  'description': 'Fully functional website',
 },
  {
  'id': '3',
  'title': 'Portfolio Website',
  'description': 'Fully functional Portfolio website',
 }
]
def projects(request):
    projects = Projects.objects.all()
    context = { 'projects': projects}
    return render(request,'projects/projects.html', context)
    
def project(request,pk):
 projectObj = Projects.objects.get(id=pk)
 return render(request,'projects/single-project.html',{'project':projectObj})

