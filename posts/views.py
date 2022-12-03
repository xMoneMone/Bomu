from django.shortcuts import render
from posts.models import CanvasPost


def post_details(request, pk):
    cur_post = CanvasPost.objects.get(id=pk)
    context = {"post": cur_post}
    return render(request, 'post_details.html', context=context)


def post_edit(request, pk):
    cur_post = CanvasPost.objects.get(id=pk)
    context = {"post": cur_post}
    return render(request, 'post_details.html', context=context)
