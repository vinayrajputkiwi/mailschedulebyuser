from datetime import datetime
from celery.schedules import crontab
from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
from .models import Task
from .forms import TaskSchedul
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic.base import TemplateView
# Create your views here.

def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")

def schedule_mail(request):
    if request.method == 'POST':
        form=TaskSchedul(request.POST)
        task_name=request.POST['task_name']
        minute=request.POST['minute']
        hour=request.POST['hour']
        day_of_week=request.POST['day_of_week']
        day_of_month=request.POST['day_of_month']
        month_of_year=request.POST['month_of_year']
        schedule, created = CrontabSchedule.objects.get_or_create(minute = minute,hour=hour, day_of_week= day_of_week,day_of_month=day_of_month, month_of_year= month_of_year)
        # schedule, created = ClockedSchedule.objects.get_or_create(time)
        task = PeriodicTask.objects.create(crontab=schedule, name=task_name, task='send_mail_app.tasks.send_mail_func') #, args = json.dumps([[2,3]]))
        # task = PeriodicTask.objects.create(crontab=schedule, name='schedule_mail'+'2', task='send_mail_app.tasks.send_mail_func') #, args = json.dumps([[2,3]]))
        if form.is_valid():
            form.save()
        return HttpResponse("Done")

    else:
        form=TaskSchedul()
    return render(request,'task.html',{'form':form})

# def taskreg(request):
#     if request.method == 'POST':
#         fm =TaskSchedul(request.POST)
#         if fm.is_valid():
#             fm.save()
#             fm=TaskSchedul()
#     else:
#         fm=TaskSchedul()
#     return render(request,'task.html',{'form':fm})