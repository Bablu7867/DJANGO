from django.shortcuts import render

# Create your views here.
def expression(request):
    d={'age':18,'name':'BABLU','runs':23}
    return render(request,'xml.html',d)