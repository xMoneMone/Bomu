from django.shortcuts import render, redirect
from posts.models import CanvasPost, CanvasLike, CanvasComment
from posts.forms import CanvasPostForm
from django.contrib.auth.decorators import login_required
from django.views import View


class PostDetails(View):
    def get(self, request, pk):
        form = CanvasComment()
        cur_post = CanvasPost.objects.get(id=pk)
        context = {"post": cur_post,
                   "form": form}
        return render(request, 'post_details.html', context=context)


@login_required(login_url='login')
def post_edit(request, pk):
    cur_post = CanvasPost.objects.get(id=pk)

    if cur_post.user != request.user:
        return redirect('home')

    if request.method == 'GET':
        form = CanvasPostForm(instance=cur_post, initial=cur_post.__dict__)
    else:
        form = CanvasPostForm(request.POST or None, request.FILES or None, instance=cur_post)
        if form.is_valid():
            form.save()
            return redirect('post-details', pk)

    context = {"form": form,
               "post": cur_post}

    return render(request, 'post_edit.html', context=context)


@login_required(login_url='login')
def post_delete(request, pk):
    cur_post = CanvasPost.objects.get(id=pk)
    if cur_post.user != request.user:
        return redirect('home')
    else:
        cur_post.delete()
        return redirect('home')


@login_required(login_url='login')
def post_like(request, pk):
    cur_post = CanvasPost.objects.get(id=pk)
    liked_object = CanvasLike.objects.filter(user=request.user, to_post=cur_post).first()

    if liked_object:
        liked_object.delete()
    else:
        like = CanvasLike(to_post=cur_post)
        like.save()
        like.user.add(request.user)

    return redirect(request.META['HTTP_REFERER'])
