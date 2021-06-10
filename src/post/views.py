from django.http.request import HttpRequest
from django.shortcuts import render

from .models import Post
# Create your views here.

#CRUD -> Create Retrive Update Delete

def post_list_view(request:HttpRequest):
    post_ojects = Post.objects.all() 
    context = {
        'post_objects':post_ojects
    }
    return render(request,"posts/index.html",context)