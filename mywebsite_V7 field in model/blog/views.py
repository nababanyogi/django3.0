from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    # print(posts)
    context ={
        'Title' : 'Blog',
        'Heading' : 'Blog di mywebsite',
        'Posts' : posts,
    }
    return render(request,'blog/index.html',context)