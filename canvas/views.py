from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from posts.forms import CanvasPostForm
from posts.models import CanvasPost


@login_required(login_url='login')
def canvas(request):
    if request.method == 'POST':
        canvas_post = CanvasPost(user=request.user, drawing=r'art/download_4.png')
        canvas_post.save()
        return redirect('post-canvas')
    return render(request, template_name="canvas-create.html")


@login_required(login_url='login')
def post_canvas(request):
    canvas_post = CanvasPost.objects.filter(user=request.user).last()
    if request.method == 'GET':
        form = CanvasPostForm(instance=canvas_post, initial=canvas_post.__dict__)
    else:
        form = CanvasPostForm(request.POST or None, request.FILES or None, instance=canvas_post)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {"form": form,
               "canvas_post": canvas_post}
    return render(request, template_name="post-canvas.html", context=context)
