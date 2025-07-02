from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Proyecto

class IndexView(ListView):  
    template_name = 'core/index.html'
    model = Proyecto
   


