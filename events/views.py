from django.shortcuts import render
from django.views.generic import ListView
from .models import *
# Create your views here.
class EventListView(ListView):
    model=Event