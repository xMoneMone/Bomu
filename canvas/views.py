from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from posts.forms import CanvasPostForm
from django.contrib.auth.models import User


@login_required(login_url='login')
def canvas(request):
    return render(request, template_name="canvas-create.html")


@login_required(login_url='login')
def post_canvas(request):
    form = CanvasPostForm()
    if request.method == 'POST':
        form = CanvasPostForm(request.POST, request.FILES or None)
        if form.is_valid():
            posted_drawing = form.save(commit=False)
            posted_drawing.user = request.user
            posted_drawing.save()
            return redirect('home')

    context = {"form": form}
    return render(request, template_name="post-canvas.html", context=context)
