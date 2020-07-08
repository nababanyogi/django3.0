from django.shortcuts import render


def index2(request):
    context = {
        'judul' : 'Kelas Terbuka',
        'subjudul' : 'selamat datang',
        'banner' : 'img/banner_home.png',
    }
    return render(request, 'index2.html', context)

def index(request):
    context = {
        'title' : 'Kelas Terbuka',
        'heading' : 'selamat datang',
        'subheading' : 'di kelas terbuka',
    }
    return render(request, 'index.html', context)