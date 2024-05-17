from django.shortcuts import render
from .models import Project,Skill,Message
from .forms import Projectform,Skillform
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    project=Project.objects.all()
    
  
    skill=Skill.objects.all()
    context={'project':project,'skill':skill}
    return render(request,'index.html',context)

def project(request):
    if request.method == 'POST':
        form = Projectform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
              # Replace 'success_url' with your desired success URL
    else:
        form = Projectform()


    return render(request,'projects.html',{'form': form})
    
    
def delete(request,id):
    obj=Project.objects.filter(id=id)
    obj.delete() 
    return redirect(to='index') 
def skill(request):
    if request.method == 'POST':
        form = Skillform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
              # Replace 'success_url' with your desired success URL
    else:
        form = Skillform()
    return render(request, 'skill.html', {'form': form}) 
def dskill(request,id):
    obj=Skill.objects.filter(id=id)
    obj.delete()
    return redirect(to='index')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        message=request.POST.get('message')
        ins=Message(name=name,message=message)
        ins.save()
        return redirect('index')
    return render(request,'contact.html')
        

  
    
    
    
   
    