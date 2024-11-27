from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def users(request):
    return HttpResponse('<h1> Sachin Tendulkar uses MRF bat</h1>')
def user2(request):
    return HttpResponse('<h1> Virat Kohli uses MRF bat</h1>')