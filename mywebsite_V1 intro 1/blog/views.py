from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'kelas terbuka',
        'kontributor':'Sandro',
        'nav' : [
            ['/blog/news','News'],
            ['/blog/recent','Recent'],
            ['/blog/testing','Testing']
        ]
    }
    # context isinya dictionary
    return render(request, 'blog/index.html',context)

def news(request):
    context = {
        'judul' : 'kelas terbuka 2',
        'kontributor':'Jean'
    }
    return render(request, 'blog/news.html',context)

def recent(request):
    context = {
        'judul' : 'kelas terbuka 2',
        'kontributor':'Jean'
    }
    return render(request, 'blog/recent.html',context)

# def recent(request):
#     return render(request, 'recent.html')