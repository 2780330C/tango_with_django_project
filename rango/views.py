from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)

def about(index):
    context_dict = {'boldmessage': 'This tutorial has been put together by Mark Campbell'}

    return render(index, 'rango/about.html', context=context_dict)
