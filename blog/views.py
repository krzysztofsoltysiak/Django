from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'KS',
        'title': 'First post',
        'content': 'First post content',
        'date_posted': '06.07.2020'
    },
    {
        'author': 'KS',
        'title': 'Second post',
        'content': 'Second post content',
        'date_posted': '06.07.2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})