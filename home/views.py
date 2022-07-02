from django.shortcuts import render, HttpResponse
from home.models import Task
# Create your views here.

def home(request):
    #return HttpResponse('works')
    context={'success':False}  
    if request.method == "POST":
        #Handle the form
        title= request.POST['title']
        desc=  request.POST['desc']
        print(title, desc)
        #instance is equal to the new task title and desc
        ins=Task(taskTitle=title,taskDescription=desc)
        ins.save()
        context = {'success':True}
    
    return render(request,'index.html',context)
def tasks(request):
    return render(request,'tasks.html')
