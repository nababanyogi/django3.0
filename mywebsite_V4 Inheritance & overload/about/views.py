from django.shortcuts import render

def index(request):
    context = {
        'title' : 'About',
        'heading' : 'About This Chapter',
        'subheading' : 'About kelas terbuka',
    }
    return render(request, 'about/index.html', context)