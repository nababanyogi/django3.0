from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Blog',
        'heading' : 'My Blog',
        'subheading' : 'Blog kelas terbuka',
    }
    return render(request, 'blog/index.html', context)