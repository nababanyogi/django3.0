from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'about',
        'subjudul' : 'ini adalah sub about',
        'banner' : 'about/img/banner_about.png',
        'app_css' :'about/css/styles.css',
    }
    return render(request,'index.html',context)