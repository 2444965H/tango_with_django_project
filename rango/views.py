from django.shortcuts import render, redirect

from django.http import HttpResponse

def index(request): 
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context = context_dict)
    
def about(request): 
    context_dict = {'boldmessage': ' This tutorial has been put together by Diem Linh Huynh'}
    return render(request, 'rango/about.html', context = context_dict) 