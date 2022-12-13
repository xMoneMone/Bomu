from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from posts.forms import CanvasPostForm
from canvas.forms import PaletteForm
from canvas.models import Palette


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


def palettes(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('home')

    all_palettes = Palette.objects.all().order_by('-id')
    context = {
        "palettes": all_palettes
    }
    return render(request, template_name="palettes.html", context=context)


def palette_add(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('home')

    form = PaletteForm()
    if request.method == 'POST':
        form = PaletteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('palettes')

    context = {"form": form}
    return render(request, template_name="add-palette.html", context=context)


def palette_edit(request, pk):
    if not request.user.is_staff and not request.user.is_superuser:
        return redirect('home')

    cur_palette = Palette.objects.get(id=pk)

    if request.method == 'GET':
        form = PaletteForm(instance=cur_palette, initial=cur_palette.__dict__)
    else:
        form = PaletteForm(request.POST or None, instance=cur_palette)
        if form.is_valid():
            form.save()
            return redirect('palettes')

    context = {"form": form}
    return render(request, 'add-palette.html', context=context)


def palette_delete(request, pk):
    if not request.user.is_superuser:
        return redirect('home')

    cur_palette = Palette.objects.get(id=pk)
    cur_palette.delete()

    return redirect('palettes')
