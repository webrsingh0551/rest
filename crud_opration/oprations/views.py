
# Create your views here.
from django.shortcuts import render 
  
# relative import of forms 
from .models import Oprations_tutorial
from .forms import TutorialForm 
  
  
def create_view(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    form = TutorialForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
          
    context['form']= form 
    return render(request, "create.html", context) 


def list_view(request): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # add the dictionary during initialization 
    context["dataset"] = Oprations_tutorial.objects.all() 
          
    return render(request, "list_view.html", context) 

def detail_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
   
    # add the dictionary during initialization 
    context["data"] = Oprations_tutorial.objects.get(id = id) 
           
    return render(request, "detail_view.html", context) 
  
# update view for details 
def update_view(request, id): 
    # dictionary for initial data with  
    # field names as keys 
    context ={} 
  
    # fetch the object related to passed id 
    obj = get_object_or_404(Oprations_tutorial, id = id) 
  
    # pass the object as instance in form 
    form = GeeksForm(request.POST or None, instance = obj) 
  
    # save the data from the form and 
    # redirect to detail_view 
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/"+id) 
  
    # add form dictionary to context 
    context["form"] = form 
  
    return render(request, "update_view.html", context) 
