from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from posts.forms import CanvasPostForm
from posts.models import CanvasPost


@login_required(login_url='login')
def canvas(request):
    if request.method == 'POST':
        canvas_post = CanvasPost(user=request.user, drawing=r'static/images/no-drawing.png')
        canvas_post.save()
        return redirect('post-canvas')
    return render(request, template_name="canvas-create.html")


@login_required(login_url='login')
def post_canvas(request):
    print(request.GET.get('canvas'))
    return render(request, template_name="post-canvas.html")
