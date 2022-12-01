from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='login')
def canvas(request):
    return render(request, template_name="canvas-create.html")


@login_required(login_url='login')
def post_canvas(request):
    print(request.GET.get('canvas'))
    return render(request, template_name="post-canvas.html")
