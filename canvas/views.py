from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from posts.forms import CanvasPostForm
from canvas.forms import PaletteForm
from canvas.models import Palette, ActivePalette


@login_required(login_url='login')
def canvas(request):
    active_palette_id = ActivePalette.objects.get(id=1).palette
    if not Palette.objects.filter(id=active_palette_id):
        active_palette = Palette.objects.filter().first()
    else:
        active_palette = Palette.objects.get(id=active_palette_id)
    palette = str([active_palette.c1, active_palette.c2, active_palette.c3,
                   active_palette.c4, active_palette.c5, active_palette.c6,
                   active_palette.c7, active_palette.c8, active_palette.c9,
                   active_palette.c10, active_palette.c11, active_palette.c12]).replace(" ", '@').replace("'", '"')
    context = {"palette": palette}
    return render(request, template_name="canvas-create.html", context=context)


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


def palette_set(request, pk):
    if not request.user.is_superuser:
        return redirect('home')

    active_palette = ActivePalette.objects.get(id=1)
    active_palette.palette = pk
    active_palette.save()

    return redirect('canvas')
