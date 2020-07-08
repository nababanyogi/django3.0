from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Kelas Terbuka',
        'heading' : 'selamat datang',
        'subheading' : 'di kelas terbuka',
    }
    return render(request, 'index.html', context)