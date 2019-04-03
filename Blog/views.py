from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts=[dict((('author','Ya'),
            ('title','Blog POst 1'),
            ('content','First post content'),
            ('date_possted','May 11, 1991'))),
       dict((('author', 'Tu'),
            ('title', 'Blog POst 2'),
            ('content', 'Second post content'),
            ('date_possted', 'May 22, 1991')))
       ]

def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/blog.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
