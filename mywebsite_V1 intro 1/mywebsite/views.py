from django.http import HttpResponse
from django.shortcuts import render

# # method view
# def index(request):
#     return render(request, 'index.html')

def index(request):
    context = {
        'judul' : 'Home',
        'kontributor':'Yogi'
    }
    # context isinya dictionary
    return render(request, 'index.html',context)

def help(request):
    return HttpResponse("<h1>helo Help</h1>")

def about(request):
    return HttpResponse("<h1>helo About</h1>")
