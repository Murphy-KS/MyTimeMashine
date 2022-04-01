import imp
from django.http import HttpResponse
from django.shortcuts import render

from .models import Poll

def index(request):
    context = {'umfragen': Poll.objects.all()}
    return render(request=request, template_name='polls/index.html', context=context)