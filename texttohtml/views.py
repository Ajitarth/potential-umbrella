from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    form = PostForm()
    return render(request, 'texttohtml/home.html',{'form':form})