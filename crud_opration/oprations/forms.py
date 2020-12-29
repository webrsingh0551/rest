from django import forms 
from .models import Oprations_tutorial
  
  
# creating a form 
class TutorialForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Oprations_tutorial
  
        # specify fields to be used 
        fields = [ 
            "title", 
            "description", 
            "published",
        ] 