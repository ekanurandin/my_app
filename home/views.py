from django.shortcuts import render

# Create your views here.
def beranda(req):
    return render(req, "menu.html")

def menu(req):
    return render(req, "myfisrt.html")