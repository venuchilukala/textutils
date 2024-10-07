from django.http import HttpResponse
from django.shortcuts import render 



def index(request):
    
    params = {'name' : 'venu', 'place' : 'hyderabad'}
    
    return render(request, 'index.html', params)
    # return HttpResponse('<h1>Home</h1>')

def removepunc(request):
    return HttpResponse('<p>Remove punctuation</p>')

def capfirst(request):
    return HttpResponse('<p>Capitalize first character</p>')

def newlineremove(request):
    return HttpResponse('<p>New line removed</p>')

def spaceremove(request):
    return HttpResponse('<p>Space is removed</p>')

def charcount(request):
    return HttpResponse('<p>Character count</p>')