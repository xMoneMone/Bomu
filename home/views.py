from django.shortcuts import render
from posts.models import CanvasPost


def home(request):
    posts = CanvasPost.objects.all()
    context = {'posts': posts}
    return render(request, template_name="home.html", context=context)
