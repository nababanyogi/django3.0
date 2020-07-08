from django.shortcuts import render

# Create your views here.
def index2(request):
    context = {
        'judul' : 'blog',
        'subjudul' : 'ini adalah sub judul',
        'banner' : 'blog/img/banner_blog.png',
        'app_css' : 'blog/css/styles.css',
    }
    return render(request,'index2.html',context)