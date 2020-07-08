from django.shortcuts import render

# Create your views here.
def khusus(request, slug):
    context = {
        'judul' : slug,
    }
    return render(request, 'blog/index.html', context)

def categoryPost(request):
    context = {
        'judul' : 'category Post',
    }
    return render(request, 'blog/index.html', context)

def singlePost(request):
    context = {
        'judul' : 'single Post',
    }
    return render(request, 'blog/index.html', context)

def index(request):
    context = {
        'judul' : 'home blog',
    }
    return render(request, 'blog/index.html', context)