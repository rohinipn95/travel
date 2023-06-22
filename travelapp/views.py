from django.shortcuts import render

from travelapp.models import  meet_team


def index(request):
    obj =meet_team.objects.all()
    return render(request,'index.html',{'result':obj})
