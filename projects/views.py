from django.shortcuts import render
from django.http import HttpResponse

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
    page = "projects"
    number = 9
    context = {
     'page': page,
     'number': number,
     'projects': projectsList, 
    }
    return render(request,'projects/projects.html', context)
    
def project(request,pk):
 projectObj = None
 for i in projectsList:
  if i['id'] == pk:
   projectObj = i

 return render(request,'projects/single-project.html',{'project':projectObj})

