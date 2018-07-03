from django import forms
from HereticFamily.AppData import models

class AddTaskForm(forms.Form):
    class Meta:
      model=models.FactTasklist
      
fields=['taskname', 'taskdesc', 'assignedto']