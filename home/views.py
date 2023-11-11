from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
  template = loader.get_template('beranda.html')
  return HttpResponse(template.render())

def menu(request):
  template = loader.get_template('menu.html')
  return HttpResponse(template.render())