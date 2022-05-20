from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('sendmail/', views.send_mail_to_all, name="sendmail"),
    path('schedulemail/', views.schedule_mail, name="sendmail"),
    # path('userreg/', views.registeruser, name="userreg"),
    # path('taskreg/', views.taskreg, name="taskreg"),
]
