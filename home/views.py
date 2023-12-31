from django.shortcuts import render 
from django.http import HttpResponse
from django.template import loader
from .models import Beranda, Menu 

def login (request):
  template = loader.get_template('beranda.html')
  return HttpResponse(template.render())

def beranda(request):
  data = Beranda.objects.all()
  template = loader.get_template('beranda.html')
  context = {
    'kulkul' : 'Macam - Macam es Kul-Kul',
    'beranda' : data
  }
  return HttpResponse(template.render(context, request))

def menu(request):
  data = Menu.objects.all()
  template = loader.get_template('menu.html')
  context = {
    'list' : 'Menu di Kul-Kul YMM :',
    'menu' : data 

  }
  return HttpResponse(template.render(context, request))