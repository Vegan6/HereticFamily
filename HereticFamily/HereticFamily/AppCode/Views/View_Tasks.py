from django.shortcuts import render
from django.http import HttpRequest
from datetime import datetime, date
from django.contrib.auth.decorators import login_required
from HereticFamily.AppData import models
import json

@login_required
def tasks(request):
    """Renders the tasks page."""
    assert isinstance(request, HttpRequest)
    user = models.AuthUser.objects.get(id=request.user.id)
    users = models.AuthUser.objects.filter(is_active=True)
        
    """ Check if form submit """
    if request.method == 'POST':
        data = request.POST
        taskName = data['taskName']
        taskDesc = data['taskDescr']
        assignTo = data['assignedTo']
        assignedTo = models.AuthUser.objects.get(id=assignTo) 
        newTask = models.FactTasklist(taskname=taskName, taskdesc=taskDesc, taskcreateddate=date.today(), 
                                      completed=0, createdby=user, assignedto=assignedTo)
        newTask.save()
        
    tasks = models.FactTasklist.objects.filter(assignedto=user, completed=0)
    tasksMe = models.FactTasklist.objects.filter(createdby=user)
    
    context = {
            'title': 'Heretic Family',
            'Year': datetime.now().year,
            'User': user,
            'Tasks': tasks,
            'TasksMe': tasksMe,
            'Users': users,
        }
    return render(
        request,
        'tasks.html',
        context
    )
    
@login_required
def taskUpdate(request):
  """Ajax Call to Update Task"""
  assert isinstance(request, HttpRequest)
  #Need to check if task exists first
  data = json.loads(request.body.decode('utf-8'))
  TaskID = data['TaskID']
  TaskValue = data['Value']
  Task = models.FactTasklist.objects.get(taskid=TaskID)
    
  Task.completed = TaskValue
  Task.save()
  
  context = {
        'title': 'Heretic Family',
        'Year': datetime.now().year,
        
    }
  return render(
    request,
    'tasks.html',
    context
  )
    